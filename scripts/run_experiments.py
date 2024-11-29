from src.agents import swarm_response
from src.tools import summary_tool, search_web_tool, task_managment_tool, code_tool, database_tool, calendar_tool, statistical_analysis_tool
from src.tools.schemas import SearchWebToolParams, TaskManagmentToolParams, CodeToolParams, DatabaseToolParams, StatisticalAnalysisToolParams
from src.utils.tracking import ToolTracker

if __name__ == "__main__":
    tracker = ToolTracker()
    
    PROMPT = """
Retrieve all upcoming tasks categorized as 'meetings' with high priority for tomorrow
"""
    MODEL = "gpt-4o-mini"
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
    INSTRUCTIONS = """You are a helpful AI assistant."""
    response = swarm_response(PROMPT, MODEL, AVAILABLE_TOOLS, INSTRUCTIONS)
    # Get tool usage data
    tool_calls = tracker.get_tool_calls()
    
    # Print or store the results
    print("\nTool Usage Summary:")
    for call in tool_calls:
        print(f"\nTool: {call['tool_name']}")
        print(f"Duration: {call['duration']:.3f}s")
        print(f"Arguments: {call['arguments']}")
        print(f"Timestamp: {call['timestamp']}")
    
    # Clear tracker for next run if needed
    tracker.clear()