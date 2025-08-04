"""
Weaviate tool for searching similar tech support tickets.
"""

import os
import weaviate
from weaviate.classes.init import Auth
from dotenv import load_dotenv

load_dotenv()

def search_similar_tickets(query: str, k: int = 1) -> str:
    """
    Search for similar tech support tickets in Weaviate.
    
    Args:
        query: The search query
        k: Number of results to return (default: 1)
    
    Returns:
        str: The closest matching ticket with its solution or error message
    """
    try:
        # Get Weaviate config
        weaviate_url = os.getenv("WEAVIATE_URL")
        weaviate_api_key = os.getenv("WEAVIATE_API_KEY")
        class_name = os.getenv("WEAVIATE_CLASS_NAME", "TechSupport").strip()
        
        if not weaviate_url:
            return "Error: WEAVIATE_URL not configured"
        
        # Connect to Weaviate
        client = weaviate.connect_to_weaviate_cloud(
            cluster_url=weaviate_url,
            auth_credentials=Auth.api_key(weaviate_api_key),
        )
        
        # Search for similar tickets using originalMessage field
        collection = client.collections.get(class_name)
        response = collection.query.near_text(
            query=query,
            limit=k,
            return_properties=["originalMessage", "repliesAggregated"]
        )
        
        if response.objects:
            obj = response.objects[0]
            original_message = obj.properties.get("originalMessage", "No original message found")
            solution = obj.properties.get("repliesAggregated", "No solution found")
            
            client.close()
            return f"📋 Original Issue:\n{original_message}\n\n💡 Solution:\n{solution}"
        else:
            client.close()
            return f"No similar tickets found for query: '{query}'"
            
    except Exception as e:
        return f"Error searching Weaviate: {str(e)}"
