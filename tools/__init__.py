"""
Tools package for the tech support agent.
Import and register tools here for easy access.
"""

from .base import BaseTool
from .math_tool import MathTool
from .web_search_tool import WebSearchTool
from .file_tool import FileTool

# List of all available tools
AVAILABLE_TOOLS = [
    MathTool,
    WebSearchTool,
    FileTool,
]

def get_all_tools():
    """Return all available tool instances."""
    return [tool() for tool in AVAILABLE_TOOLS]

def get_tool_by_name(name):
    """Get a specific tool by name."""
    tool_map = {tool.__name__: tool for tool in AVAILABLE_TOOLS}
    return tool_map.get(name)

__all__ = [
    'BaseTool',
    'MathTool', 
    'WebSearchTool',
    'FileTool',
    'AVAILABLE_TOOLS',
    'get_all_tools',
    'get_tool_by_name'
] 