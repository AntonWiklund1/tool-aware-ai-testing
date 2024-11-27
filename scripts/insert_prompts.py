import json
import psycopg2

from src.database.connection import close_connection, get_connection
from src.tools import DEFAULT_TOOLS

def insert_prompts(json_file_path: str) -> None:
    """
    Insert prompts from a JSON file into the database.
    
    JSON format should be:
    {
        "prompts": [
            {
                "prompt": "What's the weather like?",
                "prompt_category": "weather",
                "correct_tool": "search_web_tool",
                "tools_available": ["search_web_tool", "calendar_tool"]  // Optional
            }
        ]
    }
    """
    try:
        # Read JSON file
        with open(json_file_path, 'r') as file:
            data = json.load(file)
        
        # Connect to database
        conn, cursor = get_connection()
        
        # Insert each prompt
        for prompt_data in data['prompts']:
            # Use default tools if tools_available is not provided
            tools_available = prompt_data.get('tools_available', DEFAULT_TOOLS)
            
            cursor.execute("""
                INSERT INTO prompts (prompt, prompt_category, correct_tool, tools_available)
                VALUES (%s, %s, %s, %s)
            """, (
                prompt_data['prompt'],
                prompt_data['prompt_category'],
                prompt_data['correct_tool'],
                tools_available
            ))
        
        # Commit the transaction
        conn.commit()
        print(f"Successfully inserted {len(data['prompts'])} prompts into the database.")
        
    except json.JSONDecodeError as e:
        print(f"Error reading JSON file: {e}")
    except psycopg2.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        close_connection(conn, cursor)

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python insert_prompts.py <path_to_json_file>")
        sys.exit(1)
    
    insert_prompts(sys.argv[1])