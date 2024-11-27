import logging
import os
from typing import List, Dict, Any
from .core import Swarm
from .types import Agent
from dotenv import load_dotenv
# Configure logging
logging.basicConfig(level=logging.ERROR)

# Load environment variables
load_dotenv()

client = Swarm()

def swarm_response(
    prompt: str,
    model: str,
    available_tools: List[Dict[str, Any]],
    instructions: str
) -> str:
    """
    Gets a response from the AI using the Swarm framework.

    Returns:
        AI response as string
    """
    try:
        # Create main agent
        main_agent = Agent(
        name="AI Assistant",
        instructions=instructions,
        functions=[
            tool["function"] 
            for tool in available_tools 
            if tool["enabled"]
        ],
        model=model,
    )
        
        # Get response from Swarm
        response = client.run(
            agent=main_agent,
            messages=[{"role": "user", "content": prompt}],
            model_override=model,
        )
        
        if response is None or not response.messages:
            logging.error("Invalid response from client.run")
            return "I apologize, but I couldn't generate a response at this time. Please try again."

        # Get the last assistant message
        for message in reversed(response.messages):
            if message.get("role") == "assistant" and message.get("content"):
                return message["content"]
        
        logging.error("No assistant message found in response")
        return "I apologize, but I couldn't generate a response at this time. Please try again."
        
    except Exception as e:
        logging.error(f"Error in get_response: {e}")
        return "I apologize, but an error occurred while processing your request. Please try again."
    
