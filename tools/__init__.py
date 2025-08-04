"""
Tools package for the tech support agent.
Only Weaviate search function is included.
"""

import warnings
# Suppress protobuf warnings
warnings.filterwarnings("ignore", message="Protobuf gencode version.*")

from .weaviate_tool import search_similar_tickets
from langchain.tools import tool

@tool
def search_similar_tickets_tool(query: str) -> str:
    """Search for similar tech support tickets in the database"""
    return search_similar_tickets(query)

def get_all_tools():
    """Get all available tools for the agent."""
    return [search_similar_tickets_tool]

__all__ = [
    'search_similar_tickets',
    'get_all_tools'
] 