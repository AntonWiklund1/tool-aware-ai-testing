TOOL_METADATA = {
    "statistical_analysis_tool": {
        "description": "Performs statistical analysis on numerical data",
        "capabilities": [
            "Calculate mean, median, mode, standard deviation",
            "Process numerical arrays",
            "Analyze time series data",
            "Generate statistical reports"
        ],
        "input_types": ["numerical arrays", "time series", "user scores"],
        "common_use_cases": [
            "Analyzing user engagement metrics",
            "Processing performance data",
            "Calculating averages and distributions"
        ],
        "input_format": """
- List of numbers: [0.92, 0.85, 0.78, 0.95]
- List of dictionaries with numerical fields:
  [{"duration": 30, "participants": 8}, {"duration": 60, "participants": 12}]""",
        "output_format": {
            "all_stats": """Statistical Analysis Results:
- Mean: 45.7
- Median: 42.0
- Mode: 37.5
- Standard Deviation: 12.3
- Sample Size: 10
- Total: 457""",
            "single_stat": "Mean: 45.7"
        }
    },
    "calendar_tool": {
        "description": "Manages and queries calendar events",
        "capabilities": [
            "Retrieve events by date range",
            "Filter events by category",
            "Track meeting participants",
            "Manage event durations"
        ],
        "input_types": ["dates", "time ranges", "event categories"],
        "common_use_cases": [
            "Meeting scheduling",
            "Event planning",
            "Availability checking"
        ],
        "input_format": """
- start_date: "2024-03-20" (YYYY-MM-DD)
- days: 7 (optional, default: 7)
- category: "meetings" (optional)""",
        "output_format": """Calendar Events (2024-03-20 to +7 days):
- Monday: Team Planning Meeting (9:00 AM) [category: meetings]
- Tuesday: Client Review (2:00 PM) [category: meetings]"""
    },
    "database_tool": {
        "description": "Executes database queries and manages data",
        "capabilities": [
            "Execute SQL queries",
            "Filter user data",
            "Generate reports",
            "Track user metrics"
        ],
        "input_types": ["SQL queries", "user IDs", "metrics"],
        "common_use_cases": [
            "User analytics",
            "Data reporting",
            "Metric tracking"
        ],
        "input_format": """SQL Queries:
- SELECT: "SELECT * FROM users WHERE posts > 100"
- INSERT: "INSERT INTO users (name, posts) VALUES ('John', 120)"
- UPDATE: "UPDATE users SET posts = 150 WHERE id = 1"
- DELETE: "DELETE FROM users WHERE id = 1" """,
        "output_format": {
            "select": """user_id | posts | country | city   
1       | 156   | USA     | Seattle
2       | 89    | Canada  | Toronto
Total rows: 2""",
            "modify": """Insert: Successfully inserted 1 row
Update: Successfully updated 5 rows
Delete: Successfully deleted 2 rows"""
        }
    },
    "task_management_tool": {
        "description": "Manages tasks and to-do lists",
        "capabilities": [
            "Create and track tasks",
            "Set priorities",
            "Manage deadlines",
            "Categorize tasks"
        ],
        "input_types": ["task details", "priorities", "dates"],
        "common_use_cases": [
            "Project management",
            "Personal task tracking",
            "Team coordination"
        ],
        "input_format": """
- date: "2024-03-20" (YYYY-MM-DD)
- category: "meetings" (optional)
- priority: "high" | "medium" | "low" (optional)""",
        "output_format": """Task List for 2024-03-20:
- Team standup (10:00 AM) [category: meetings] [priority: high]
- Client presentation (2:00 PM) [category: meetings] [priority: high]"""
    },
    "search_web_tool": {
        "description": "Performs web searches and retrieves information",
        "capabilities": [
            "Search web content",
            "Filter by categories",
            "Sort by relevance",
            "Track publication dates"
        ],
        "input_types": ["search queries", "keywords", "topics"],
        "common_use_cases": [
            "Research",
            "Information gathering",
            "News tracking"
        ],
        "input_format": "query: 'search term or phrase'",
        "output_format": """Search Results for: AI developments
1. Latest Developments in AI Technology
   Recent breakthroughs in artificial intelligence...
   Source: https://example.com/ai-developments
   Published: 2024-03-01"""
    },
    "code_tool": {
        "description": "Executes and analyzes code",
        "capabilities": [
            "Execute Python code",
            "Run TypeScript",
            "Track performance metrics",
            "Handle errors"
        ],
        "input_types": ["code snippets", "script files", "commands"],
        "common_use_cases": [
            "Code testing",
            "Script execution",
            "Performance analysis"
        ],
        "input_format": """
- code: String containing code to execute
- language: "python" | "typescript" (default: "python")
- timeout: Number of seconds (default: 30)""",
        "output_format": {
            "success": """Python Execution Result:
> Output: Hello, World!
> Execution time: 0.023s
> Memory usage: 12.4 MB
> CPU usage: 2.1%""",
            "error": """Python Execution Error:
> Error Type: SyntaxError
> Message: invalid syntax
> Line: 3"""
        }
    },
    "summary_tool": {
        "description": "Generates document summaries",
        "capabilities": [
            "Summarize documents",
            "Extract key points",
            "Identify main topics"
        ],
        "input_types": ["documents", "text content", "articles"],
        "common_use_cases": [
            "Legal document analysis",
            "Report summarization",
            "Content briefing"
        ],
        "input_format": "text: Optional[str] - The text to summarize",
        "output_format": """- The document discusses various topics.
- Key points include the importance of data analysis and effective communication.
- Concludes with future trends in technology."""
    }
}