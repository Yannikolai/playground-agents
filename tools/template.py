"""
Template for creating new tools.
Copy this file and modify it to create your own tool.
"""

from typing import Dict, Any
from .base import BaseTool


class TemplateTool(BaseTool):
    """
    Template tool - replace this with your tool description.
    
    This is a template showing how to create new tools.
    Copy this file and modify it for your specific use case.
    """
    
    def get_description(self) -> str:
        return "Template tool description - replace with your tool's description"
    
    def get_properties(self) -> Dict[str, Any]:
        return {
            "parameter1": {
                "type": "string",
                "description": "Description of the first parameter"
            },
            "parameter2": {
                "type": "integer",
                "description": "Description of the second parameter (optional)",
                "default": 10
            }
        }
    
    def get_required_properties(self) -> list:
        return ["parameter1"]  # List only required parameters
    
    def _run(self, parameter1: str, parameter2: int = 10) -> str:
        """
        Main tool logic goes here.
        
        Args:
            parameter1: First parameter description
            parameter2: Second parameter description (optional)
            
        Returns:
            str: The result of the tool execution
        """
        try:
            # Your tool logic here
            result = f"Processed {parameter1} with value {parameter2}"
            
            # Example processing
            if parameter2 > 5:
                result += " (high value)"
            else:
                result += " (low value)"
            
            return result
            
        except Exception as e:
            return f"Error in template tool: {str(e)}"
    
    def validate_input(self, **kwargs) -> bool:
        """
        Custom validation logic (optional).
        Override this method if you need custom validation.
        """
        # Example validation
        if 'parameter1' in kwargs and len(kwargs['parameter1']) < 3:
            return False
        return True


# Example of a more specific tool
class ExampleAPITool(BaseTool):
    """
    Example API tool - shows how to integrate with external APIs.
    """
    
    def get_description(self) -> str:
        return "Example tool that demonstrates API integration patterns"
    
    def get_properties(self) -> Dict[str, Any]:
        return {
            "endpoint": {
                "type": "string",
                "description": "API endpoint to call"
            },
            "method": {
                "type": "string",
                "description": "HTTP method (GET, POST, etc.)",
                "enum": ["GET", "POST", "PUT", "DELETE"],
                "default": "GET"
            }
        }
    
    def get_required_properties(self) -> list:
        return ["endpoint"]
    
    def _run(self, endpoint: str, method: str = "GET") -> str:
        """Example API call implementation."""
        try:
            import requests
            
            # Example API call
            response = requests.request(
                method=method,
                url=endpoint,
                timeout=10
            )
            
            if response.status_code == 200:
                return f"API call successful: {response.text[:200]}..."
            else:
                return f"API call failed with status {response.status_code}"
                
        except Exception as e:
            return f"Error making API call: {str(e)}"


# Example of a data processing tool
class DataProcessingTool(BaseTool):
    """
    Example data processing tool - shows how to handle data operations.
    """
    
    def get_description(self) -> str:
        return "Example tool for data processing operations"
    
    def get_properties(self) -> Dict[str, Any]:
        return {
            "data": {
                "type": "string",
                "description": "Data to process (JSON string or text)"
            },
            "operation": {
                "type": "string",
                "description": "Operation to perform",
                "enum": ["sort", "filter", "count", "unique"],
                "default": "count"
            }
        }
    
    def get_required_properties(self) -> list:
        return ["data"]
    
    def _run(self, data: str, operation: str = "count") -> str:
        """Example data processing implementation."""
        try:
            import json
            
            # Try to parse as JSON, otherwise treat as text
            try:
                data_obj = json.loads(data)
                is_json = True
            except json.JSONDecodeError:
                data_obj = data.split('\n')
                is_json = False
            
            if operation == "count":
                if is_json:
                    return f"JSON object has {len(data_obj)} top-level keys"
                else:
                    return f"Text has {len(data_obj)} lines"
            elif operation == "sort":
                if is_json and isinstance(data_obj, list):
                    sorted_data = sorted(data_obj)
                    return f"Sorted data: {json.dumps(sorted_data)}"
                else:
                    return "Sort operation only works with JSON arrays"
            else:
                return f"Operation '{operation}' not implemented"
                
        except Exception as e:
            return f"Error processing data: {str(e)}" 