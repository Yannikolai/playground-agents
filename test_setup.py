#!/usr/bin/env python3
"""
Test script to verify the virtual environment setup
"""

def test_imports():
    """Test that all required packages can be imported"""
    try:
        import langchain
        print("✓ langchain imported successfully")
        
        import langchain_openai
        print("✓ langchain_openai imported successfully")
        
        import langgraph
        print("✓ langgraph imported successfully")
        
        import openai
        print("✓ openai imported successfully")
        
        import dotenv
        print("✓ python-dotenv imported successfully")
        
        # Test specific imports
        from langgraph.prebuilt import create_agent_executor
        print("✓ create_agent_executor imported successfully")
        
        from langchain_openai import ChatOpenAI
        print("✓ ChatOpenAI imported successfully")
        
        print("\n🎉 All imports successful! Your virtual environment is set up correctly.")
        print("\nNext steps:")
        print("1. Add your OpenAI API key to a .env file:")
        print("   OPENAI_API_KEY=your_api_key_here")
        print("2. Run: python main.py")
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    
    return True

if __name__ == "__main__":
    test_imports() 