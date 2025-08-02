"""
Web search tool for searching the internet.
"""

import requests
from typing import Dict, Any
from .base import BaseTool


class WebSearchTool(BaseTool):
    """
    Tool for searching the web for information.
    
    Uses DuckDuckGo API for web searches.
    """
    
    def get_description(self) -> str:
        return "Search the web for information using DuckDuckGo. Useful for finding current information, news, or facts."
    
    def get_properties(self) -> Dict[str, Any]:
        return {
            "query": {
                "type": "string",
                "description": "The search query to look up on the web"
            },
            "max_results": {
                "type": "integer",
                "description": "Maximum number of results to return (default: 3)",
                "default": 3
            }
        }
    
    def get_required_properties(self) -> list:
        return ["query"]
    
    def _run(self, query: str, max_results: int = 3) -> str:
        """Search the web for information."""
        try:
            # Use DuckDuckGo Instant Answer API
            url = "https://api.duckduckgo.com/"
            params = {
                "q": query,
                "format": "json",
                "no_html": "1",
                "skip_disambig": "1"
            }
            
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            
            # Extract results
            results = []
            
            # Get instant answer if available
            if data.get("Abstract"):
                results.append(f"Instant Answer: {data['Abstract']}")
            
            # Get related topics
            if data.get("RelatedTopics"):
                for topic in data["RelatedTopics"][:max_results]:
                    if isinstance(topic, dict) and topic.get("Text"):
                        results.append(f"• {topic['Text']}")
            
            if not results:
                return f"No results found for '{query}'. Try rephrasing your search."
            
            return "\n\n".join(results)
            
        except requests.RequestException as e:
            return f"Error performing web search: {str(e)}"
        except Exception as e:
            return f"Unexpected error: {str(e)}"
    
    def _search_with_duckduckgo(self, query: str) -> Dict[str, Any]:
        """Alternative search method using DuckDuckGo."""
        try:
            # This is a simplified version - in production you might want to use
            # a more robust search API like SerpAPI or Google Custom Search
            url = f"https://duckduckgo.com/html/?q={query}"
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            }
            
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            
            # Parse HTML response (simplified)
            # In a real implementation, you'd use BeautifulSoup or similar
            return {"status": "success", "data": response.text[:500]}
            
        except Exception as e:
            return {"status": "error", "message": str(e)} 