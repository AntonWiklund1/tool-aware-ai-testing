from datetime import datetime
from src.agents import swarm_response
from src.tools import summary_tool, search_web_tool, task_managment_tool, code_tool, database_tool, calendar_tool, statistical_analysis_tool
from src.tools.schemas import SearchWebToolParams, TaskManagmentToolParams, CodeToolParams, DatabaseToolParams, StatisticalAnalysisToolParams
from src.utils.tracking import ToolTracker
from src.database.queries import get_all_prompts
from src.database.connection import get_connection
import json

def print_header(text: str, char: str = "=", length: int = 80):
    """Print a formatted header"""
    print(f"\n{char * length}")
    print(f"{text.center(length)}")
    print(f"{char * length}\n")

def print_tool_summary(call: dict):
    """Print a formatted tool call summary"""
    print(f"🔧 Tool: {call['tool_name']}")
    print(f"⏱️  Duration: {call['duration']:.3f}s")
    print(f"📝 Arguments: {json.dumps(call['arguments'], indent=2)}")
    print(f"🕒 Timestamp: {call['timestamp']}\n")

def create_test_run(model_name: str, instructions: str) -> int:
    """Create a new test run and return its ID"""
    conn, cur = get_connection()
    try:
        cur.execute("""
            INSERT INTO test_runs (model_name, instructions, started_at, configuration)
            VALUES (%s, %s, %s, %s::jsonb)
            RETURNING id;
        """, (model_name, instructions, datetime.now(), json.dumps({})))
        test_run_id = cur.fetchone()[0]
        conn.commit()
        return test_run_id
    finally:
        cur.close()
        conn.close()

def save_result(prompt_id: int, test_run_id: int, tool_calls: list, time_taken: float, success_rate: bool, error_type: str = None):
    """Save the result of a prompt execution"""
    conn, cur = get_connection()
    try:
        cur.execute("""
            INSERT INTO results 
            (prompt_id, test_run_id, tool_calls, time_taken, success_rate, error_type, created_at)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (prompt_id, test_run_id, tool_calls, time_taken, success_rate, error_type, datetime.now()))
        conn.commit()
    finally:
        cur.close()
        conn.close()

def main():
    tracker = ToolTracker()
    
    MODEL = "gpt-4o-mini"
    INSTRUCTIONS = """You are a helpful AI assistant."""
    AVAILABLE_TOOLS = [
        {
            "name": "summary_tool",
            "function": summary_tool,
            "description": summary_tool.__doc__,
            "enabled": True,
        },
        {
            "name": "search_web",
            "function": search_web_tool,
            "description": search_web_tool.__doc__,
            "schema": SearchWebToolParams,
            "enabled": True,
        },
        {
            "name": "task_managment_tool",
            "function": task_managment_tool,
            "schema": TaskManagmentToolParams,
            "description": task_managment_tool.__doc__,
            "enabled": True,
        },
        {
            "name": "code_tool",
            "function": code_tool,
            "description": code_tool.__doc__,
            "schema": CodeToolParams,
            "enabled": True,
        },
        {
            "name": "database_tool",
            "function": database_tool,
            "description": database_tool.__doc__,
            "schema": DatabaseToolParams,
            "enabled": True,
        },
        {
            "name": "calendar_tool",
            "function": calendar_tool,
            "description": calendar_tool.__doc__,
            "enabled": True,
        },
        {
            "name": "statistical_analysis_tool",
            "function": statistical_analysis_tool,
            "description": statistical_analysis_tool.__doc__,
            "schema": StatisticalAnalysisToolParams,
            "enabled": True,
        },
    ]

    # Create a new test run
    test_run_id = create_test_run(MODEL, INSTRUCTIONS)
    print_header(f"Test Run ID: {test_run_id}")

    # Get all prompts from database
    prompts = get_all_prompts()
    total_prompts = len(prompts)
    print_header(f"Processing {total_prompts} Prompts", "-")

    # Process each prompt
    for index, prompt in enumerate(prompts, 1):
        if index > 5:
            break
            
        print_header(f"Prompt {index}/{total_prompts}", "•")
        print("📋 Prompt:")
        print(f"{prompt['prompt']}\n")
        
        try:
            tracker.clear()
            response = swarm_response(prompt['prompt'], MODEL, AVAILABLE_TOOLS, INSTRUCTIONS)
            
            print("🤖 Response:")
            print(f"{response}\n")
            
            tool_calls = tracker.get_tool_calls()
            correct_tools = prompt['correct_tools']
            tools_used = [call['tool_name'] for call in tool_calls]
            success = all(tool in tools_used for tool in correct_tools)
            total_time = sum(call['duration'] for call in tool_calls)
            
            print_header("Tool Usage Summary", "-")
            for call in tool_calls:
                print_tool_summary(call)
                
            print(f"✨ Success: {'✅ Yes' if success else '❌ No'}")
            print(f"⏱️  Total Time: {total_time:.3f}s")
            print(f"🎯 Expected Tools: {', '.join(correct_tools)}")
            print(f"🔧 Used Tools: {', '.join(tools_used)}")
            
            save_result(
                prompt_id=prompt['id'],
                test_run_id=test_run_id,
                tool_calls=[call['tool_name'] for call in tool_calls],
                time_taken=total_time,
                success_rate=success
            )
            
        except Exception as e:
            print("\n❌ Error:")
            print(f"{str(e)}")
            print_header("Error Details", "!")
            print(f"❌ Error processing prompt {prompt['id']}:")
            print(f"{str(e)}")
            save_result(
                prompt_id=prompt['id'],
                test_run_id=test_run_id,
                tool_calls=[],
                time_taken=0,
                success_rate=False,
                error_type=str(e)
            )

    # Update test run completion
    conn, cur = get_connection()
    try:
        cur.execute("""
            UPDATE test_runs 
            SET completed_at = %s 
            WHERE id = %s
        """, (datetime.now(), test_run_id))
        conn.commit()
    finally:
        cur.close()
        conn.close()

if __name__ == "__main__":
    main()