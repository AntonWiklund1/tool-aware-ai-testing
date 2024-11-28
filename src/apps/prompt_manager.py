import streamlit as st
import json
import sys
from pathlib import Path
from typing import Dict, Any

# Add the root directory to sys.path
root_dir = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(root_dir))

from src.database.connection import get_connection
from src.tools import DEFAULT_TOOLS

def insert_prompts_from_json(data: Dict[str, Any]) -> tuple[int, str]:
    """Insert prompts from JSON data and return count of inserted prompts and any error message"""
    try:
        conn, cursor = get_connection()
        inserted_count = 0
        
        for prompt_data in data['prompts']:
            # Use default tools if tools_available is not provided
            tools_available = prompt_data.get('tools_available', DEFAULT_TOOLS)
            
            cursor.execute("""
                INSERT INTO prompts (prompt, prompt_category, correct_tools, tools_available)
                VALUES (%s, %s, %s, %s)
            """, (
                prompt_data['prompt'],
                prompt_data['prompt_category'],
                prompt_data['correct_tool'],
                tools_available
            ))
            inserted_count += 1
        
        conn.commit()
        return inserted_count, ""
        
    except Exception as e:
        return 0, str(e)
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()

def get_prompt_count() -> tuple[int, str]:
    """Get total number of prompts in database"""
    try:
        conn, cursor = get_connection()
        cursor.execute("SELECT COUNT(*) FROM prompts")
        count = cursor.fetchone()[0]
        return count, ""
    except Exception as e:
        return 0, str(e)
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()

def main():
    st.title("Prompt Manager")
    
    # Display total prompts
    total_prompts, error = get_prompt_count()
    if error:
        st.error(f"Error getting prompt count: {error}")
    else:
        st.metric("Total Prompts in Database", total_prompts)
    
    st.divider()
    
    # File upload
    st.subheader("Upload Prompts")
    uploaded_file = st.file_uploader("Choose a JSON file", type=['json'])
    
    # Text input
    st.subheader("Or paste JSON directly")
    json_text = st.text_area("JSON Content", height=300)
    
    # Process data
    if st.button("Insert Prompts"):
        try:
            if uploaded_file is not None:
                data = json.load(uploaded_file)
            elif json_text:
                data = json.loads(json_text)
            else:
                st.warning("Please either upload a file or paste JSON content")
                return
                
            # Validate JSON structure
            if 'prompts' not in data:
                st.error("Invalid JSON structure. Must contain a 'prompts' array.")
                return
                
            inserted_count, error = insert_prompts_from_json(data)
            
            if error:
                st.error(f"Error inserting prompts: {error}")
            else:
                st.success(f"Successfully inserted {inserted_count} prompts!")
                
                # Update total prompts display
                new_total, _ = get_prompt_count()
                st.metric("Total Prompts in Database", new_total)
                
        except json.JSONDecodeError:
            st.error("Invalid JSON format. Please check your input.")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

    # Show example JSON format
    with st.expander("Show Example JSON Format"):
        st.code("""
{
  "prompts": [
    {
      "prompt": "What meetings do I have next week?",
      "prompt_category": "calendar",
      "correct_tools": ["calendar_tool"],
      "tools_available": ["calendar_tool", "task_managment_tool"] // Optional, will default to all tools if not provided
    }
  ]
}
""", language="json")

if __name__ == "__main__":
    main()