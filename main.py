from langgraph.prebuilt import create_agent_executor
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from tools import get_all_tools
import os

# Load environment variables
load_dotenv()

# Create the agent with tools
llm = ChatOpenAI(model="gpt-4o")
tools = get_all_tools()

agent = create_agent_executor(
    llm=llm,
    tools=tools,
    prompt="You are a helpful tech support assistant with access to various tools. You can perform calculations, search the web, and work with files. Use the available tools to help users with their requests."
)

# Test with a simple question
print("=== Agent Test ===")
result = agent.invoke(
    {"messages": [{"role": "user", "content": "What is 15 + 27?"}]}
)
print(result["messages"][-1].content)
