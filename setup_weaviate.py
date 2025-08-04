#!/usr/bin/env python3
"""
Setup script for Weaviate connection configuration.
"""

import os
from dotenv import load_dotenv
from tools.weaviate_tool import WeaviateTool

def setup_weaviate_config():
    """Interactive setup for Weaviate configuration."""
    print("🔧 Weaviate Connection Setup\n")
    
    # Load existing .env file
    load_dotenv()
    
    # Get current values
    current_url = os.getenv("WEAVIATE_URL", "")
    current_api_key = os.getenv("WEAVIATE_API_KEY", "")
    current_class = os.getenv("WEAVIATE_CLASS_NAME", "SlackMessages")
    current_text_key = os.getenv("WEAVIATE_TEXT_KEY", "text")
    
    print("Current configuration:")
    print(f"  URL: {current_url or 'Not set'}")
    print(f"  API Key: {'Set' if current_api_key else 'Not set'}")
    print(f"  Class Name: {current_class}")
    print(f"  Text Key: {current_text_key}")
    print()
    
    # Get new values
    print("Enter your Weaviate configuration:")
    
    url = input(f"Weaviate URL [{current_url}]: ").strip()
    if not url and current_url:
        url = current_url
    
    api_key = input("API Key (optional, press Enter to skip): ").strip()
    if not api_key and current_api_key:
        api_key = current_api_key
    
    class_name = input(f"Collection/Class name [{current_class}]: ").strip()
    if not class_name:
        class_name = current_class
    
    text_key = input(f"Text field name [{current_text_key}]: ").strip()
    if not text_key:
        text_key = current_text_key
    
    # Update .env file
    env_content = []
    if os.path.exists(".env"):
        with open(".env", "r") as f:
            env_content = f.readlines()
    
    # Remove existing Weaviate config
    env_content = [line for line in env_content if not line.startswith("WEAVIATE_")]
    
    # Add new config
    if url:
        env_content.append(f"WEAVIATE_URL={url}\n")
    if api_key:
        env_content.append(f"WEAVIATE_API_KEY={api_key}\n")
    env_content.append(f"WEAVIATE_CLASS_NAME={class_name}\n")
    env_content.append(f"WEAVIATE_TEXT_KEY={text_key}\n")
    
    # Write .env file
    with open(".env", "w") as f:
        f.writelines(env_content)
    
    print(f"\n✅ Configuration saved to .env file")
    
    # Test connection
    print("\n🧪 Testing connection...")
    test_weaviate_connection()

def test_weaviate_connection():
    """Test the Weaviate connection."""
    try:
        tool = WeaviateTool()
        
        if tool.is_available():
            print("✅ Weaviate connection successful!")
            print(f"   {tool.get_collection_info()}")
            
            # Test a simple search
            print("\n🔍 Testing search functionality...")
            result = tool._run("test query", k=1)
            if "Error" not in result:
                print("✅ Search functionality working!")
            else:
                print(f"⚠️  Search test: {result}")
        else:
            print("❌ Weaviate connection failed")
            print("   Please check your configuration in .env file")
            
    except Exception as e:
        print(f"❌ Error testing connection: {e}")

def show_help():
    """Show help information."""
    print("""
🔧 Weaviate Setup Help

To connect to your existing Weaviate collection, you need:

1. **Weaviate URL**: Your Weaviate instance URL
   Example: https://your-weaviate-instance.weaviate.network

2. **API Key** (optional): If your Weaviate instance requires authentication
   Get this from your Weaviate dashboard

3. **Collection Name**: The name of your existing collection/class
   Example: "SlackMessages", "TechSupport", etc.

4. **Text Field**: The field name that contains the text content
   Example: "text", "content", "message", etc.

Common Weaviate URLs:
- Cloud: https://your-cluster.weaviate.network
- Local: http://localhost:8080
- Docker: http://localhost:8080

To run setup: python setup_weaviate.py
    """)

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--help":
        show_help()
    else:
        setup_weaviate_config() 