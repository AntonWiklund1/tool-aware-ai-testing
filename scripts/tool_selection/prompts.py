from langchain.prompts import FewShotPromptTemplate, PromptTemplate

# Example data
EXAMPLES = [
    {
        "example": """Prompt: Calculate the average engagement score and standard deviation for these user scores: [0.92, 0.85, 0.78, 0.95]
Prompt Category: statistical_analysis
Correct Tools: ['statistical_analysis_tool']"""
    },
    {
        "example": """Prompt: Find all calendar events labeled as 'meetings' for next week with more than 5 participants
Prompt Category: calendar_query
Correct Tools: ['calendar_tool', 'statistical_analysis_tool']"""
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

You will generate exactly {num_samples} diverse examples. Each example must follow this exact format:

Prompt: [the user's request]
Prompt Category: [category of the request]
Correct Tools: [list of required tools]
Expected Outcome: [what the tool should achieve]

Make sure to:
1. Number each example (1 to {num_samples})
2. Include diverse scenarios that test different tool capabilities
3. Sometimes use multiple tools when appropriate
4. Make the prompts realistic and practical
5. Consider the specific capabilities of each tool
6. when the code tool is used, the code should be in a code block or a prompt that tells what code to make and execute using the code tool

So dont use the code tool to execute code that is not in a code block or a prompt that tells what code to make and execute using the code tool
""",
        examples=EXAMPLES,
        suffix="Now, please generate exactly {num_samples} new, diverse examples. Number them from 1 to {num_samples}.",
        input_variables=["num_samples", "tool_descriptions"],
        example_prompt=EXAMPLE_TEMPLATE,
    )