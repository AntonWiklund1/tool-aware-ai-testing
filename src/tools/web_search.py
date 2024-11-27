from langchain_community.utilities import GoogleSerperAPIWrapper
import dotenv
dotenv.load_dotenv()

serper = GoogleSerperAPIWrapper()

def search_web_tool(query: str, **kwargs) -> str:
    """Search the web for information.

    **Description**:
    This tool searches the web for information based on the user's query.
    
    Args:
        query (str): The search query to look up information about
    """
    print(f"Searching the web for: {query}")
    try:
        if isinstance(query, dict) and 'query' in query:
            query = query['query']
            
        results = serper.run(query)
        return results
    except Exception as e:
        return f"Error searching the web: {str(e)}"