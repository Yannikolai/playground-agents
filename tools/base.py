"""
Base tool class for the tech support agent.
All tools should inherit from this class.
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, Optional
from langchain.tools import BaseTool as LangChainBaseTool


class BaseTool(LangChainBaseTool, ABC):
    """
    Base class for all tools in the tech support agent.
    
    This class provides a common interface and structure for all tools.
    Inherit from this class to create new tools.
    """
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = self.__class__.__name__
        self.description = self.get_description()
    
    @abstractmethod
    def get_description(self) -> str:
        """Return the tool description for the agent."""
        pass
    
    @abstractmethod
    def _run(self, *args, **kwargs) -> str:
        """Execute the tool logic."""
        pass
    
    def get_tool_schema(self) -> Dict[str, Any]:
        """Get the tool schema for LangChain integration."""
        return {
            "name": self.name,
            "description": self.description,
            "parameters": self.get_parameters_schema()
        }
    
    def get_parameters_schema(self) -> Dict[str, Any]:
        """Get the parameters schema for the tool."""
        return {
            "type": "object",
            "properties": self.get_properties(),
            "required": self.get_required_properties()
        }
    
    def get_properties(self) -> Dict[str, Any]:
        """Get the properties schema for the tool parameters."""
        return {}
    
    def get_required_properties(self) -> list:
        """Get the list of required properties."""
        return []
    
    def validate_input(self, **kwargs) -> bool:
        """Validate input parameters."""
        return True
    
    def __str__(self) -> str:
        return f"{self.name}: {self.description}"
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name='{self.name}')" 