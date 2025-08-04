import warnings
from langgraph.prebuilt import chat_agent_executor
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from tools import get_all_tools, search_similar_tickets
import os

# Suppress protobuf warnings
warnings.filterwarnings("ignore", message="Protobuf gencode version.*")

# Load environment variables
load_dotenv()

def run_simple_test():
    """Simple test mode that directly tests the search functionality"""
    print("=== Simple Weaviate Test Mode ===")
    user_input = input("Enter your support request: ")
    result = search_similar_tickets(user_input)
    print(f"\nResult: {result}")

def run_full_agent():
    """Full agent mode with LangGraph"""
    llm = ChatOpenAI(model="gpt-4o")
    tools = get_all_tools()

    agent = chat_agent_executor(
        llm=llm,
        tools=tools,
        system_message="You are a helpful tech support assistant. When a user submits a new ticket, check if a similar issue has been reported before using the available tools."
    )

    print("=== Tech Support Agent ===")
    while True:
        user_input = input("\nNew ticket: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        result = agent.invoke({"messages": [{"role": "user", "content": f"Check for similar past tickets to: {user_input}"}]})
        print("\n🔎 Closest match:")
        print(result["messages"][-1].content)

if __name__ == "__main__":
    print("Choose mode:")
    print("1. Simple test (direct search)")
    print("2. Full agent mode")
    
    choice = input("Enter choice (1 or 2): ").strip()
    
    if choice == "1":
        run_simple_test()
    elif choice == "2":
        run_full_agent()
    else:
        print("Invalid choice. Running full agent mode.")
        run_full_agent()
