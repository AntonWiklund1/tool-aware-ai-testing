import logging
from typing import List, Dict, Any
from langchain_openai import ChatOpenAI
from langchain_core.tools import StructuredTool
from langchain_core.messages import HumanMessage
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import SystemMessage
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(level=logging.ERROR)

# Load environment variables
load_dotenv()

def react_response(
    prompt: str,
    model: str,
    available_tools: List[Dict[str, Any]],
    instructions: str
) -> str:
    """
    Gets a response from the AI using the basic framework.

    Args:
        prompt: The user's input prompt
        model: The OpenAI model to use
        available_tools: List of tools to use with their configurations
        instructions: System instructions

    Returns:
        AI response as string
    """
    try:
        # Initialize LLM
        llm = ChatOpenAI(
            model=model,
            temperature=0
        )
        
        # Convert available_tools to LangChain StructuredTool format
        tools = [
            StructuredTool(
                name=tool["name"].replace("_tool", ""),
                description=tool["description"],
                func=tool["function"],
                args_schema=tool.get("schema", None)
            )
            for tool in available_tools
            if tool.get("enabled", True)
        ]

        # Create the agent
        agent_executor = create_react_agent(
            llm,
            tools,
            state_modifier=SystemMessage(content=instructions)
        )

        # Run the agent with a specific recursion limit
        config = {"recursion_limit": 7}
        
        final_response = None
        
        # Run the agent and capture the final response
        for chunk in agent_executor.stream(
            {"messages": [HumanMessage(content=prompt)]},
            config=config
        ):
            if "agent" in chunk and "messages" in chunk["agent"]:
                messages = chunk["agent"]["messages"]
                if messages and hasattr(messages[-1], "content"):
                    final_response = messages[-1].content
        
        return final_response if final_response else "I apologize, but I couldn't generate a complete response."

    except Exception as e:
        logging.error(f"Error in basic_response: {e}")
        return "I apologize, but an error occurred while processing your request. Please try again."

if __name__ == "__main__":
    # Example usage
    from src.tools import (
        summary_tool,
        search_web_tool,
        task_management_tool,
        code_tool,
        database_tool,
        calendar_tool,
        statistical_analysis_tool
    )
    from src.tools.schemas import (
        SearchWebToolParams,
        TaskManagmentToolParams,
        CodeToolParams,
        DatabaseToolParams,
        StatisticalAnalysisToolParams
    )

    PROMPT = "What's on my calendar for next week and are there any high priority tasks?"
    MODEL_NAME = "gpt-4o-mini"
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
            "name": "task_management_tool",
            "function": task_management_tool,
            "schema": TaskManagmentToolParams,
            "description": task_management_tool.__doc__,
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
    INSTRUCTIONS = "You are a helpful AI assistant."

    TEST_RESPONSE = react_response(PROMPT, MODEL_NAME, AVAILABLE_TOOLS, INSTRUCTIONS)
    print(TEST_RESPONSE)
