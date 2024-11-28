from typing import Optional, Dict, List, Union
from datetime import datetime, timedelta

def database_tool(query: str, **kwargs) -> str:
    """
    Executes a SQL query on the database.

    Available columns:
    - `user_id`
    - `number_of_posts`
    - `registered_at`
    - `last_login`
    - `country`
    - `city`
    - `language`
    - `gender`

    Args:
        query (str): The SQL query to execute.

    Returns:
        str: database query results
    """
    print("running database_tool")
    # Structured mock data for internal use
    structured_data = {
        "users": [
            {
                "user_id": 1,
                "number_of_posts": 156,
                "registered_at": "2023-01-15T10:30:00",
                "last_login": "2024-03-10T15:45:00",
                "country": "USA",
                "city": "Seattle",
                "language": "en",
                "gender": "F",
                "engagement_score": 0.85
            },
            {
                "user_id": 2,
                "number_of_posts": 89,
                "registered_at": "2023-03-20T14:20:00",
                "last_login": "2024-03-09T11:30:00",
                "country": "Canada",
                "city": "Toronto",
                "language": "en",
                "gender": "M",
                "engagement_score": 0.72
            },
            {
                "user_id": 3,
                "number_of_posts": 234,
                "registered_at": "2023-02-01T09:15:00",
                "last_login": "2024-03-10T16:20:00",
                "country": "UK",
                "city": "London",
                "language": "en",
                "gender": "M",
                "engagement_score": 0.93
            }
        ]
    }

    # Format SELECT results as table
    def format_select_results(data: List[Dict]) -> str:
        if not data:
            return "No results found"
            
        # Get all columns from first row
        columns = list(data[0].keys())
        
        # Create header
        header = " | ".join(f"{col:15}" for col in columns)
        separator = "-" * len(header)
        
        # Create rows
        rows = []
        for row in data:
            formatted_row = " | ".join(f"{str(row[col]):15}" for col in columns)
            rows.append(formatted_row)
            
        return f"{header}\n{separator}\n" + "\n".join(rows) + f"\nTotal rows: {len(data)}"

    # Mock query responses
    mock_results = {
        "SELECT": format_select_results(structured_data["users"]),
        "INSERT": "Insert: Successfully inserted 1 row",
        "UPDATE": "Update: Successfully updated 5 rows",
        "DELETE": "Delete: Successfully deleted 2 rows",
        "error": "Error: Invalid SQL query syntax"
    }

    # Determine query type from the first word
    query_type = query.strip().upper().split()[0]
    
    # Return result based on query type
    return mock_results.get(
        query_type,
        f"Invalid query type. Available types: {', '.join(mock_results.keys())}"
    )