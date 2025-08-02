"""
Math tool for performing calculations.
"""

import re
from typing import Dict, Any
from .base import BaseTool


class MathTool(BaseTool):
    """
    Tool for performing mathematical calculations.
    
    Supports basic arithmetic operations: +, -, *, /, **
    Also supports mathematical functions like sqrt, sin, cos, etc.
    """
    
    def get_description(self) -> str:
        return "Perform mathematical calculations. Supports basic arithmetic (+, -, *, /, **) and common math functions."
    
    def get_properties(self) -> Dict[str, Any]:
        return {
            "expression": {
                "type": "string",
                "description": "The mathematical expression to evaluate (e.g., '2 + 3 * 4', 'sqrt(16)', 'sin(45)')"
            }
        }
    
    def get_required_properties(self) -> list:
        return ["expression"]
    
    def _run(self, expression: str) -> str:
        """Evaluate a mathematical expression."""
        try:
            # Clean the expression
            expression = expression.strip()
            
            # Basic validation
            if not self._is_safe_expression(expression):
                return "Error: Expression contains unsafe operations"
            
            # Replace common math functions
            expression = self._replace_math_functions(expression)
            
            # Evaluate the expression
            result = eval(expression)
            
            return f"Result: {result}"
            
        except Exception as e:
            return f"Error evaluating expression: {str(e)}"
    
    def _is_safe_expression(self, expression: str) -> bool:
        """Check if the expression is safe to evaluate."""
        # Only allow numbers, operators, parentheses, and basic math functions
        safe_pattern = r'^[0-9+\-*/().\s,]+$'
        math_functions = ['sqrt', 'sin', 'cos', 'tan', 'log', 'exp', 'abs']
        
        # Check for math functions
        for func in math_functions:
            if func in expression.lower():
                return True
        
        # Check basic pattern
        return bool(re.match(safe_pattern, expression))
    
    def _replace_math_functions(self, expression: str) -> str:
        """Replace math functions with Python equivalents."""
        import math
        
        # Common math function replacements
        replacements = {
            'sqrt': 'math.sqrt',
            'sin': 'math.sin',
            'cos': 'math.cos',
            'tan': 'math.tan',
            'log': 'math.log',
            'exp': 'math.exp',
            'abs': 'abs',
            'pi': 'math.pi',
            'e': 'math.e'
        }
        
        # Apply replacements
        for old, new in replacements.items():
            expression = expression.replace(old, new)
        
        return expression 