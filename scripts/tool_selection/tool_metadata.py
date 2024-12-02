TOOL_METADATA = {
    "summary_tool": {
        "description": """Get a summary of the user's uploaded documents to the database. So no need to provide a text argument.""",
        "capabilities": [
            "Get a summary of the user's uploaded documents to the database. So no need to provide a text argument.",
        ],
        "input_types": [
        ],
        "common_use_cases": [
        ],
        "input_format": """No input format available""",
        "output_format": """str:  summary of the text.

Example:
Summary Results:
- The document discusses various topics
- Key points include data analysis and communication
- Concludes with recommendations""",
    },
    "search_web_tool": {
        "description": """Search the web for information. **Description**: This tool searches the web for information based on the user's query.""",
        "capabilities": [
            "Search the web for information. **Description**: This tool searches the web for information based on the user's query.",
            "Handle query (str) parameter",
        ],
        "input_types": [
            "str",
        ],
        "common_use_cases": [
        ],
        "input_format": """- query: str (optional) (default: PydanticUndefined) - The search query to look up information about""",
        "output_format": """str: Search results formatted as a readable string

Example:
Search Results for: AI developments
1. Latest Developments in AI Technology
   Recent breakthroughs in artificial intelligence...
   Source: https://example.com/ai-developments
   Published: 2024-03-01""",
    },
    "statistical_analysis_tool": {
        "description": """This tool performs statistical analysis on numerical data and returns results.""",
        "capabilities": [
            "This tool performs statistical analysis on numerical data and returns results.",
            "Handle data parameter",
            "Handle analysis_type parameter",
            "Handle confidence_level parameter",
        ],
        "input_types": [
            "List",
            "str",
            "Optional",
        ],
        "common_use_cases": [
            "Data analysis",
        ],
        "input_format": """- data: List (optional) (default: PydanticUndefined) - List of numerical data points to analyze
- analysis_type: str (optional) (default: PydanticUndefined) - Type of analysis to perform (mean, median, mode, std_dev, all)
- confidence_level: Optional (optional) (default: 0.95) - Confidence level for statistical calculations (0-1)""",
        "output_format": """str: Statistical analysis results

Example:
Statistical Analysis Results:
- Mean: 85.6
- Median: 82.5
- Mode: 80.0
- Standard Deviation: 12.4
- Sample Size: 50
- Total: 4280""",
    },
    "task_management_tool": {
        "description": """Task management tool with advanced filtering and organization. Use this tool to manage your tasks and to-do lists. Not for calendar management.""",
        "capabilities": [
            "Task management tool with advanced filtering and organization. Use this tool to manage your tasks and to-do lists. Not for calendar management.",
            "Handle date parameter",
            "Handle category parameter",
            "Handle priority parameter",
            "Handle assignee parameter",
            "Handle status parameter",
            "Handle due_within_days parameter",
        ],
        "input_types": [
            "str",
            "Optional",
        ],
        "common_use_cases": [
            "Filtering and searching",
            "Date-based operations",
        ],
        "input_format": """- date: str (optional) (default: PydanticUndefined) - The date to get tasks for (YYYY-MM-DD)
- category: Optional (optional) - Filter tasks by category
- priority: Optional (optional) - Filter tasks by priority (low, medium, high)
- assignee: Optional (optional) - Filter tasks by assigned person
- status: Optional (optional) - Filter tasks by status (pending, in_progress, completed)
- due_within_days: Optional (optional) - Filter tasks due within specified days""",
        "output_format": """Task List for 2024-03-15:
- Team standup (10:00 AM) [category: meetings] [priority: high] [assignee: John] [status: pending]
- Client presentation (2:00 PM) [category: meetings] [priority: high] [assignee: Sarah] [status: in_progress]""",
    },
    "code_tool": {
        "description": """Executes code snippets in python or typescript.""",
        "capabilities": [
            "Executes code snippets in python or typescript.",
            "Handle code parameter",
            "Handle language parameter",
            "Handle timeout parameter",
        ],
        "input_types": [
            "str",
            "Optional",
        ],
        "common_use_cases": [
        ],
        "input_format": """- code: str (optional) (default: PydanticUndefined) - The code to execute
- language: str (optional) (default: python) - Programming language of the code
- timeout: Optional (optional) (default: 30) - Maximum execution time in seconds""",
        "output_format": """str: Execution results

Example:
Python Execution Result:
> Output: Hello, World!
> Execution time: 0.023s
> Memory usage: 12.4 MB
> CPU usage: 2.1%""",
    },
    "database_tool": {
        "description": """Executes a SQL query on the database. Available columns: - `user_id` - `number_of_posts` - `registered_at` - `last_login` - `country` - `city` - `language` - `gender` - `engagement_score`""",
        "capabilities": [
            "Executes a SQL query on the database. Available columns: - `user_id` - `number_of_posts` - `registered_at` - `last_login` - `country` - `city` - `language` - `gender` - `engagement_score`",
            "Handle query (str) parameter",
        ],
        "input_types": [
            "str",
        ],
        "common_use_cases": [
        ],
        "input_format": """- query: str (optional) (default: PydanticUndefined) - The SQL query to execute""",
        "output_format": """str: database query results

Example:
user_id | posts | engagement
1       | 156   | 0.85
2       | 89    | 0.72
3       | 234   | 0.93
Total rows: 3""",
    },
    "calendar_tool": {
        "description": """Gets calendar events for a specified date range with advanced filtering.""",
        "capabilities": [
            "Gets calendar events for a specified date range with advanced filtering.",
            "Handle start_date parameter",
            "Handle days parameter",
            "Handle category parameter",
            "Handle location parameter",
            "Handle min_participants parameter",
            "Handle max_duration parameter",
        ],
        "input_types": [
            "str",
            "Optional",
        ],
        "common_use_cases": [
            "Filtering and searching",
            "Date-based operations",
        ],
        "input_format": """- start_date: str (optional) (default: PydanticUndefined) - Start date for calendar events (YYYY-MM-DD)
- days: Optional (optional) (default: 7) - Number of days to look ahead
- category: Optional (optional) - Filter events by category
- location: Optional (optional) - Filter events by location
- min_participants: Optional (optional) - Filter events by minimum number of participants
- max_duration: Optional (optional) - Filter events by maximum duration in minutes""",
        "output_format": """str: Calendar events for the specified period

Example:
Calendar Events (2024-03-15 to +7 days):
- Monday: Team Planning Meeting (9:00 AM, 60 mins) [category: meetings] [location: Conference Room A] [participants: 10]
- Tuesday: Client Review (2:00 PM, 90 mins) [category: meetings] [location: Virtual] [participants: 5]""",
    },
}
