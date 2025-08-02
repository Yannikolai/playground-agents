"""
File tool for reading and writing files.
"""

import os
import json
from typing import Dict, Any, Optional
from .base import BaseTool


class FileTool(BaseTool):
    """
    Tool for reading and writing files.
    
    Supports text files, JSON files, and basic file operations.
    """
    
    def get_description(self) -> str:
        return "Read and write files. Supports text files, JSON files, and basic file operations like listing directories."
    
    def get_properties(self) -> Dict[str, Any]:
        return {
            "operation": {
                "type": "string",
                "description": "The operation to perform: 'read', 'write', 'list', 'exists'",
                "enum": ["read", "write", "list", "exists"]
            },
            "file_path": {
                "type": "string",
                "description": "The path to the file or directory"
            },
            "content": {
                "type": "string",
                "description": "Content to write to the file (for write operations)"
            },
            "file_type": {
                "type": "string",
                "description": "Type of file: 'text' or 'json' (default: 'text')",
                "default": "text"
            }
        }
    
    def get_required_properties(self) -> list:
        return ["operation", "file_path"]
    
    def _run(self, operation: str, file_path: str, content: Optional[str] = None, file_type: str = "text") -> str:
        """Perform file operations."""
        try:
            if operation == "read":
                return self._read_file(file_path, file_type)
            elif operation == "write":
                if content is None:
                    return "Error: Content is required for write operations"
                return self._write_file(file_path, content, file_type)
            elif operation == "list":
                return self._list_directory(file_path)
            elif operation == "exists":
                return self._check_exists(file_path)
            else:
                return f"Error: Unknown operation '{operation}'"
                
        except Exception as e:
            return f"Error performing file operation: {str(e)}"
    
    def _read_file(self, file_path: str, file_type: str) -> str:
        """Read a file."""
        if not os.path.exists(file_path):
            return f"Error: File '{file_path}' does not exist"
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if file_type == "json":
                # Try to parse as JSON for better formatting
                try:
                    data = json.loads(content)
                    return f"JSON content:\n{json.dumps(data, indent=2)}"
                except json.JSONDecodeError:
                    return f"File content (not valid JSON):\n{content}"
            else:
                return f"File content:\n{content}"
                
        except Exception as e:
            return f"Error reading file: {str(e)}"
    
    def _write_file(self, file_path: str, content: str, file_type: str) -> str:
        """Write content to a file."""
        try:
            # Create directory if it doesn't exist
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            
            if file_type == "json":
                # Try to parse content as JSON
                try:
                    data = json.loads(content)
                    with open(file_path, 'w', encoding='utf-8') as f:
                        json.dump(data, f, indent=2)
                except json.JSONDecodeError:
                    return f"Error: Content is not valid JSON"
            else:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
            
            return f"Successfully wrote to '{file_path}'"
            
        except Exception as e:
            return f"Error writing file: {str(e)}"
    
    def _list_directory(self, directory_path: str) -> str:
        """List contents of a directory."""
        if not os.path.exists(directory_path):
            return f"Error: Directory '{directory_path}' does not exist"
        
        if not os.path.isdir(directory_path):
            return f"Error: '{directory_path}' is not a directory"
        
        try:
            items = os.listdir(directory_path)
            if not items:
                return f"Directory '{directory_path}' is empty"
            
            result = f"Contents of '{directory_path}':\n"
            for item in sorted(items):
                item_path = os.path.join(directory_path, item)
                if os.path.isdir(item_path):
                    result += f"📁 {item}/\n"
                else:
                    result += f"📄 {item}\n"
            
            return result
            
        except Exception as e:
            return f"Error listing directory: {str(e)}"
    
    def _check_exists(self, path: str) -> str:
        """Check if a file or directory exists."""
        exists = os.path.exists(path)
        if exists:
            if os.path.isdir(path):
                return f"Directory '{path}' exists"
            else:
                return f"File '{path}' exists"
        else:
            return f"'{path}' does not exist" 