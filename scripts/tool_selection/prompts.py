from langchain.prompts import FewShotPromptTemplate, PromptTemplate

# Example data
EXAMPLES = [
    {
        "example": """Prompt: Calculate the average engagement score and standard deviation for these user scores: [0.92, 0.85, 0.78, 0.95]
Prompt Category: statistical_analysis
Correct Tools: ['statistical_analysis_tool']"""
    },
    {
        "example": """Prompt: Get all users from the database who have posted more than 100 times and have an engagement score above 0.8
Prompt Category: database_query
Correct Tools: ['database_tool']"""
    },
    {
        "example": """Prompt: Create a summary of all my legal documents related to case #123
Prompt Category: document_summary
Correct Tools: ['summary_tool']"""
    },
    {
        "example": """Prompt: Calculate the average meeting duration and create a summary report for all meetings that had more than 5 participants last week
Prompt Category: meeting_analysis
Correct Tools: ['calendar_tool', 'statistical_analysis_tool']"""
    },
    {
        "example": """Prompt: Find all high-priority tasks assigned to developers, analyze their completion rates, and generate a code snippet to visualize the data
Prompt Category: developer_productivity
Correct Tools: ['task_management_tool', 'statistical_analysis_tool', 'code_tool']"""
    }
]

EXAMPLE_TEMPLATE = PromptTemplate(
    input_variables=["example"],
    template="{example}"
)

def create_prompt_template() -> FewShotPromptTemplate:
    return FewShotPromptTemplate(
        prefix="""You are generating synthetic data for testing AI agents in tool selection. 
The available tools and their capabilities are:

{tool_descriptions}

You will generate exactly {num_samples} diverse and challenging examples. Each example must follow this exact format:

Prompt: [the user's request]
Prompt Category: [category of the request]
Correct Tools: [list of required tools]

Make sure to:
1. Number each example (1 to {num_samples}).
2. Include diverse scenarios that test different tool capabilities, including edge cases and error handling.
3. Sometimes use multiple tools when appropriate, and sometimes no tools.
4. Make the prompts realistic and challenging by including:
   - Common typos and misspellings (e.g., "calender" instead of "calendar")
   - Informal language and abbreviations (e.g., "pls", "asap", "tmrw")
   - Ambiguous requests that require tool inference
   - Run-on sentences with multiple requests
   - Mixed capitalization and punctuation
   - Implicit tool requirements (e.g., "compare these numbers" implies statistical_analysis_tool)
   - Regional spelling variations (e.g., "analyse" vs "analyze")
5. Consider the specific capabilities and limitations of each tool.
6. When the code tool is used:
   - Include requests with incorrect code syntax
   - Mix programming languages in the same request
   - Include requests for code optimization or debugging
7. Vary complexity levels:
   - Simple single-tool tasks
   - Multi-step workflows requiring tool coordination
   - Complex scenarios with conditional logic
8. Include domain-specific jargon and technical terminology.
9. Add noise to requests with:
   - Irrelevant information
   - Emotional context ("urgently need", "frustrated with")
   - Conversational fillers ("um", "like", "you know")
10. Test edge cases:
    - Requests at the boundary between two tools
    - Overlapping tool capabilities
    - Invalid or incomplete parameters""",
        examples=EXAMPLES,
        suffix="generate exactly {num_samples} new, diverse examples following these guidelines. Number them from 1 to {num_samples}. Make sure to include a good mix of simple and complex cases, with various types of challenges from the guidelines above.",
        input_variables=["num_samples", "tool_descriptions"],
        example_prompt=EXAMPLE_TEMPLATE,
    )