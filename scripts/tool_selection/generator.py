from typing import List, Optional
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
        print("-" * 100)
        print("response", response.content)
        print("-" * 100)
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
    # Remove asterisks and number prefixes from the text
    example_text = example_text.replace('**', '')
    # Remove numbered prefixes like "1.", "2.", etc.
    example_text = ' '.join(example_text.split('.', 1)[1:]).strip()
    
    try:
        # Split the text by double newlines to separate sections
        sections = example_text.split('\n')
        sections = [s.strip() for s in sections if s.strip()]
        
        # Extract the required fields
        prompt = ''
        category = ''
        tools = []
        
        for section in sections:
            if section.startswith('Prompt:'):
                prompt = section.replace('Prompt:', '').strip()
            elif section.startswith('Prompt Category:'):
                category = section.replace('Prompt Category:', '').strip()
            elif section.startswith('Correct Tools:'):
                tools_str = section.replace('Correct Tools:', '').strip()
                # Clean up the tools string and parse it
                tools = tools_str.strip('[]').replace("'", '').replace('"', '')
                tools = [t.strip() for t in tools.split(',') if t.strip()]
        
        if prompt and category and tools:
            return ToolSelectionData(
                prompt=prompt,
                prompt_category=category,
                correct_tools=tools
            )
            
    except Exception as e:
        print(f"Error parsing example: {e}")
        return None
    
    return None