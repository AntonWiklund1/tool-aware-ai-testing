from typing import Dict, List, Optional, Union
import json

def search_web_tool(query: str, **kwargs) -> str:
    """Search the web for information.

    **Description**:
    This tool searches the web for information based on the user's query.
    
    Args:
        query (str): The search query to look up information about
    
    Returns:
        str: Search results formatted as a readable string
    """
    # Structured mock data for internal use
    mock_search_data = {
        "technology": {
            "results": [
                {
                    "title": "Latest Developments in AI Technology",
                    "snippet": "Recent breakthroughs in artificial intelligence have led to significant improvements in natural language processing and computer vision...",
                    "link": "https://example.com/ai-developments",
                    "published_date": "2024-03-01"
                },
                {
                    "title": "The Future of Cloud Computing",
                    "snippet": "Cloud computing continues to evolve with new serverless architectures and edge computing solutions becoming mainstream...",
                    "link": "https://example.com/cloud-future",
                    "published_date": "2024-02-28"
                }
            ]
        },
        "business": {
            "results": [
                {
                    "title": "Global Market Trends 2024",
                    "snippet": "Analysis of emerging market trends shows a shift towards sustainable business practices and digital transformation...",
                    "link": "https://example.com/market-trends",
                    "published_date": "2024-03-05"
                }
            ]
        },
        "default": {
            "results": [
                {
                    "title": "General Information",
                    "snippet": "This is a general search result that provides basic information about the queried topic...",
                    "link": "https://example.com/info",
                    "published_date": "2024-03-10"
                }
            ]
        }
    }

    try:
        if isinstance(query, dict) and 'query' in query:
            query = query['query']

        # Determine category based on keywords in query
        category = "default"
        if any(tech_term in query.lower() for tech_term in ["ai", "technology", "software", "computer"]):
            category = "technology"
        elif any(business_term in query.lower() for business_term in ["market", "business", "economy"]):
            category = "business"

        # Get results for the category
        results = mock_search_data.get(category, mock_search_data["default"])

        # Format results as string
        output = f"Search Results for: {query}\n\n"
        for idx, result in enumerate(results["results"], 1):
            output += f"{idx}. {result['title']}\n"
            output += f"   {result['snippet']}\n"
            output += f"   Source: {result['link']}\n"
            output += f"   Published: {result['published_date']}\n\n"

        return output

    except Exception as e:
        return f"Error searching the web: {str(e)}"