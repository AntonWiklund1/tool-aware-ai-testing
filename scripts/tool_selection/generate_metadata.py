from typing import Dict, Any, get_type_hints, Union
import inspect
from src.tools import DEFAULT_TOOLS
import importlib
from pydantic import BaseModel
from src.tools.schemas import *

def extract_docstring_sections(docstring: str) -> Dict[str, str]:
    """Extract sections from a docstring."""
    if not docstring:
        return {}
    
    sections = {
        "description": "",
        "args": [],
        "returns": "",
        "capabilities": []
    }
    
    current_section = "description"
    lines = [line.strip() for line in docstring.split('\n')]
    
    for line in lines:
        if line.lower().startswith('args:'):
            current_section = "args"
            continue
        elif line.lower().startswith('returns:'):
            current_section = "returns"
            continue
        
        if line and not line.startswith('"""'):
            if current_section == "args" and ':' in line:
                sections["args"].append(line.split(':')[0].strip())
            elif current_section == "returns":
                sections["returns"] += line + "\n"
            elif current_section == "description":
                sections["description"] += line + " "
    
    sections["description"] = sections["description"].strip()
    sections["returns"] = sections["returns"].strip()
    return sections

def get_schema_for_tool(tool_name: str) -> BaseModel:
    """Get the Pydantic schema for a tool."""
    schema_map = {
        "calendar_tool": CalendarToolParams,
        "code_tool": CodeToolParams,
        "database_tool": DatabaseToolParams,
        "statistical_analysis_tool": StatisticalAnalysisToolParams,
        "task_management_tool": TaskManagmentToolParams,
        "search_web_tool": SearchWebToolParams
    }
    return schema_map.get(tool_name)

def format_input_format(schema: BaseModel) -> str:
    """Format input format from a Pydantic schema."""
    if not schema:
        return "No input format available"
    
    schema_fields = schema.model_fields
    input_format = []
    
    for field_name, field in schema_fields.items():
        # Get field type
        field_type = field.annotation.__name__ if hasattr(field.annotation, '__name__') else str(field.annotation)
        
        # Check if field is optional (Union with None or has default value)
        is_optional = field.default is not None or (
            hasattr(field.annotation, '__origin__') and 
            field.annotation.__origin__ is Union and 
            type(None) in field.annotation.__args__
        )
        
        # Format field information
        default = f" (default: {field.default})" if field.default is not None else ""
        optional = " (optional)" if is_optional else ""
        description = f" - {field.description}" if field.description else ""
        
        input_format.append(f"- {field_name}: {field_type}{optional}{default}{description}")
    
    return "\n".join(input_format)

def get_example_output(tool_name: str) -> str:
    """Get example output format for a tool."""
    example_outputs = {
        "calendar_tool": """Calendar Events (2024-03-15 to +7 days):
- Monday: Team Planning Meeting (9:00 AM, 60 mins) [category: meetings] [location: Conference Room A] [participants: 10]
- Tuesday: Client Review (2:00 PM, 90 mins) [category: meetings] [location: Virtual] [participants: 5]""",

        "statistical_analysis_tool": """Statistical Analysis Results:
- Mean: 85.6
- Median: 82.5
- Mode: 80.0
- Standard Deviation: 12.4
- Sample Size: 50
- Total: 4280""",

        "database_tool": """user_id | posts | engagement
1       | 156   | 0.85
2       | 89    | 0.72
3       | 234   | 0.93
Total rows: 3""",

        "task_management_tool": """Task List for 2024-03-15:
- Team standup (10:00 AM) [category: meetings] [priority: high] [assignee: John] [status: pending]
- Client presentation (2:00 PM) [category: meetings] [priority: high] [assignee: Sarah] [status: in_progress]""",

        "code_tool": """Python Execution Result:
> Output: Hello, World!
> Execution time: 0.023s
> Memory usage: 12.4 MB
> CPU usage: 2.1%""",

        "search_web_tool": """Search Results for: AI developments
1. Latest Developments in AI Technology
   Recent breakthroughs in artificial intelligence...
   Source: https://example.com/ai-developments
   Published: 2024-03-01""",

        "summary_tool": """Summary Results:
- The document discusses various topics
- Key points include data analysis and communication
- Concludes with recommendations"""
    }
    
    return example_outputs.get(tool_name, "String output")

def generate_tool_metadata() -> Dict[str, Dict[str, Any]]:
    """Generate TOOL_METADATA dictionary from tool functions."""
    metadata = {}
    
    for tool_name in DEFAULT_TOOLS:
        try:
            # Import the tool module
            module_name = tool_name.replace('_tool', '')
            module = importlib.import_module(f"src.tools.{module_name}")
            tool_function = getattr(module, tool_name)
            
            # Get docstring info
            docstring = inspect.getdoc(tool_function)
            docstring_sections = extract_docstring_sections(docstring)
            
            # Get schema
            schema = get_schema_for_tool(tool_name)
            
            # Generate capabilities from docstring and type hints
            capabilities = []
            if docstring_sections["description"]:
                capabilities.append(docstring_sections["description"])
            for arg in docstring_sections["args"]:
                capabilities.append(f"Handle {arg} parameter")
            
            # Generate common use cases based on capabilities
            common_use_cases = []
            if "filter" in str(capabilities).lower():
                common_use_cases.append("Filtering and searching")
            if "date" in str(capabilities).lower():
                common_use_cases.append("Date-based operations")
            if "analysis" in str(capabilities).lower():
                common_use_cases.append("Data analysis")
            
            # Get input types from schema
            input_types = []
            if schema:
                for field in schema.model_fields.values():
                    field_type = field.annotation.__name__ if hasattr(field.annotation, '__name__') else str(field.annotation)
                    input_types.append(field_type)
            
            # Get output format
            output_format = get_example_output(tool_name)
            if docstring_sections["returns"]:
                output_format = f"{docstring_sections['returns']}\n\nExample:\n{output_format}"
            
            # Create metadata entry
            metadata[tool_name] = {
                "description": docstring_sections["description"],
                "capabilities": capabilities,
                "input_types": list(set(input_types)),
                "common_use_cases": common_use_cases,
                "input_format": format_input_format(schema) if schema else "No input format available",
                "output_format": output_format
            }
            
        except ImportError as e:
            print(f"Warning: Could not import module for {tool_name}: {e}")
            continue
        except Exception as e:
            print(f"Error processing {tool_name}: {e}")
            continue
    
    return metadata

def update_tool_metadata_file():
    """Update the tool_metadata.py file with generated metadata."""
    metadata = generate_tool_metadata()
    
    output = "TOOL_METADATA = {\n"
    for tool_name, tool_data in metadata.items():
        output += f"    \"{tool_name}\": {{\n"
        for key, value in tool_data.items():
            if isinstance(value, list):
                output += f"        \"{key}\": [\n"
                for item in value:
                    output += f"            \"{item}\",\n"
                output += "        ],\n"
            else:
                output += f"        \"{key}\": \"\"\"{value}\"\"\",\n"
        output += "    },\n"
    output += "}\n"
    
    # Write to file
    with open("scripts/tool_selection/tool_metadata.py", "w") as f:
        f.write(output)

if __name__ == "__main__":
    update_tool_metadata_file()