import os
from typing import Dict, Any
from langsmith import traceable

@traceable
def web_mcp_search(query: str, include_raw_content=True, max_results=3):
    """ Search the web using the web-mcp webscraper.
    
    Args:
        query (str): The search query to execute
        include_raw_content (bool): Whether to include the raw_content in the formatted string
        max_results (int): Maximum number of results to return
        
    Returns:
        dict: Search response containing:
            - results (list): List of search result dictionaries, each containing:
                - title (str): Title of the search result
                - url (str): URL of the search result
                - content (str): Snippet/summary of the content
                - raw_content (str): Full content of the page if available
    """
    try:
        from langchain_core.messages import HumanMessage, SystemMessage
        from langchain_ollama import ChatOllama

        # Use the webscraper MCP to analyze the website
        response = {
            "tool_name": "analyze_website",
            "server_name": "webscraper",
            "arguments": {
                "url": query,
                "selectors": []  # Optional CSS selectors to extract specific elements
            }
        }

        # Format the results to match the expected structure
        results = []
        if response and 'content' in response:
            results.append({
                'title': response.get('title', 'Web Page'),
                'url': query,
                'content': response.get('content', ''),
                'raw_content': response.get('raw_content', '')
            })

        return {"results": results[:max_results]}

    except Exception as e:
        print(f"Error in web_mcp_search: {str(e)}")
        # Return empty results on error
        return {"results": []}}
