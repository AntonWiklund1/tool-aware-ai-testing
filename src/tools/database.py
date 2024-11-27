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
        str:  database query results
    """
    #  responses based on query type
    mock_results = {
        "SELECT": """
| user_id | number_of_posts | country | city    |
|---------|----------------|---------|---------|
| 1       | 156            | USA     | Seattle |
| 2       | 89             | Canada  | Toronto |
| 3       | 234            | UK      | London  |
Total rows: 3
""",
        "INSERT": "Insert: Successfully inserted 1 row",
        "UPDATE": "Update: Successfully updated 5 rows",
        "DELETE": "Delete: Successfully deleted 2 rows",
        "error": "Error: Invalid SQL query syntax"
    }

    # Determine query type from the first word
    query_type = query.strip().upper().split()[0]
    
    # Return  result based on query type
    return mock_results.get(
        query_type,
        f"Invalid query type. Available types: {', '.join(mock_results.keys())}"
    )