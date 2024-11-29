from typing import List, Optional
import json
from langchain_openai import ChatOpenAI
from langchain.prompts import FewShotPromptTemplate
from .models import ToolSelectionData
from .tool_metadata import TOOL_METADATA

def format_tool_descriptions(metadata: dict) -> str:
    descriptions = []
    for tool_name, info in metadata.items():
        desc = f"- {tool_name}:\n"
        desc += f"  Description: {info['description']}\n"
        desc += f"  Capabilities: {', '.join(info['capabilities'])}\n"
        desc += f"  Input Format: {info['input_format']}\n"
        desc += f"  Output Format:\n{info['output_format']}"
        desc += f"\n  Common Uses: {', '.join(info['common_use_cases'])}\n"
        descriptions.append(desc)
    return "\n".join(descriptions)

def generate_examples(
    llm: ChatOpenAI,
    prompt_template: FewShotPromptTemplate,
    num_samples: int
) -> List[ToolSelectionData]:
    """Generate synthetic examples using direct LLM calls."""
    
    tool_descriptions = format_tool_descriptions(TOOL_METADATA)
    formatted_prompt = prompt_template.format(
        num_samples=num_samples,
        tool_descriptions=tool_descriptions
    )
    
    try:
        response = llm.invoke(formatted_prompt)
        examples_text = response.content.split('\n\n')
        examples = []
        
        for example_text in examples_text:
            if not example_text.strip():
                continue
            
            try:
                example = parse_example(example_text)
                if example:
                    examples.append(example)
            except Exception as e:
                print(f"Error parsing example: {e}")
                continue
                
        return examples
        
    except Exception as e:
        print(f"Error generating examples: {e}")
        return []

def parse_example(example_text: str) -> Optional[ToolSelectionData]:
    """Parse a single example from text into a ToolSelectionData object."""
    lines = example_text.strip().split('\n')
    if len(lines) < 3:
        return None
        
    try:
        prompt_line = [l for l in lines if l.startswith('Prompt:')][0].replace('Prompt:', '').strip()
        category_line = [l for l in lines if l.startswith('Prompt Category:')][0].replace('Prompt Category:', '').strip()
        tools_line = [l for l in lines if l.startswith('Correct Tools:')][0].replace('Correct Tools:', '').strip()
        
        tools = json.loads(tools_line.replace("'", '"'))
        
        return ToolSelectionData(
            prompt=prompt_line,
            prompt_category=category_line,
            correct_tools=tools
        )
    except Exception:
        return None