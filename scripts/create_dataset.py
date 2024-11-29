from dotenv import load_dotenv
import pandas as pd
from langchain_openai import ChatOpenAI
from src.database.connection import get_connection
from src.database.models import Prompt
from .tool_selection.models import SimpleCache
from .tool_selection.prompts import create_prompt_template
from .tool_selection.generator import generate_examples
from src.tools import DEFAULT_TOOLS

load_dotenv()

SAMPLES_PER_RUN = 10
RUNS = 2

def save_to_database(synthetic_data):
    """Save the generated data to PostgreSQL database."""
    conn, cur = get_connection()
    try:
        # Prepare the insert query
        insert_query = """
            INSERT INTO prompts (prompt, prompt_category, correct_tools, tools_available)
            VALUES (%s, %s, %s, %s::text[])
        """
        
        # Insert each record
        for item in synthetic_data:
            # Take the first tool as the correct_tool
            correct_tool = item['correct_tools'][0] if isinstance(item['correct_tools'], list) else item['correct_tools']
            
            # Format DEFAULT_TOOLS as a proper PostgreSQL array
            tools_array = '{' + ','.join(f'"{tool}"' for tool in DEFAULT_TOOLS) + '}'
            correct_tool_array = '{' + f'"{correct_tool}"' + '}'

            cur.execute(insert_query, (
                item['prompt'],
                item['prompt_category'],
                correct_tool_array,
                tools_array
            ))
        
        conn.commit()
        print(f"Successfully saved {len(synthetic_data)} records to database")
    
    except Exception as e:
        conn.rollback()
        print(f"Error saving to database: {str(e)}")
    finally:
        cur.close()
        conn.close()

def main():
    # Create cache instance
    cache = SimpleCache()
    
    # Setup prompt template
    prompt_template = create_prompt_template()
    
    # Initialize LLM
    llm = ChatOpenAI(name="gpt-4o-mini", temperature=0, cache=cache)
    
    # Generate examples
    all_results = []
    for run in range(RUNS):
        print(f"\nGenerating run {run + 1}/{RUNS}...")
        results = generate_examples(llm, prompt_template, SAMPLES_PER_RUN)
        print(f"Generated {len(results)} examples in this run")
        all_results.extend(results)
    
    # Process results
    synthetic_data = [
        {
            'prompt': item.prompt,
            'prompt_category': item.prompt_category,
            'correct_tools': item.correct_tools
        }
        for item in all_results
    ]
    
    # Create DataFrame for statistics
    synthetic_df = pd.DataFrame(synthetic_data)
    
    # Print statistics
    print_statistics(synthetic_df)
    
    # Save to database
    save_to_database(synthetic_data)

def print_statistics(df: pd.DataFrame):
    """Print debug information about the generated data."""
    print("-"*100)
    print(f"Total number of unique examples generated: {len(df)}")
    print("\nDistribution of tools used:")
    
    tool_counts = {}
    for tools in df['correct_tools']:
        for tool in tools:
            tool_counts[tool] = tool_counts.get(tool, 0) + 1

    for tool, count in tool_counts.items():
        print(f"{tool}: {count} times")
    
    print("\nFirst few examples:")
    # Print the first 5 rows of the DataFrame with no truncation
    pd.set_option('display.max_columns', None)
    print(df.head())

if __name__ == "__main__":
    main()