# Tech Support Agent

A LangGraph-based agent for technical support tasks with Weaviate vector database integration for finding similar past tickets.

## Features

- **Similar Ticket Search**: Uses Weaviate vector database to find similar past support tickets
- **LangGraph Agent**: Powered by LangGraph for intelligent conversation flow
- **OpenAI Integration**: Uses GPT-4o for natural language processing
- **Dual Modes**: Simple test mode and full agent mode

## Setup

### 1. Virtual Environment

**Note**: The `venv/` directory is not included in the repository. Each developer needs to create their own virtual environment and install dependencies from `requirements.txt`.

Create and activate a virtual environment:

```bash
# Create virtual environment
python -m venv venv

# Activate the virtual environment
source venv/bin/activate  # On macOS/Linux
# or
venv\Scripts\activate     # On Windows
```

### 2. Install Dependencies

```bash
# Install all required packages from requirements.txt
pip install -r requirements.txt
```

### 3. Environment Variables

Create a `.env` file in the project root with your API keys:

```bash
# OpenAI API Key (required)
OPENAI_API_KEY=your_openai_api_key_here

# Weaviate Configuration (if using external Weaviate instance)
# WEAVIATE_URL=your_weaviate_url_here
# WEAVIATE_API_KEY=your_weaviate_api_key_here
```

### 4. Get API Keys

- **OpenAI API Key**: Get your API key from [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)
- **Weaviate**: Currently uses embedded Weaviate (no external setup required)

## Usage

### Run the Agent

```bash
# Make sure virtual environment is activated
source venv/bin/activate

# Run the main agent
python main.py
```

The agent will prompt you to choose between two modes:

1. **Simple Test Mode**: Directly tests the Weaviate search functionality
2. **Full Agent Mode**: Complete LangGraph agent with conversation capabilities

### Example Usage

```
Choose mode:
1. Simple test (direct search)
2. Full agent mode
Enter choice (1 or 2): 2

=== Tech Support Agent ===
New ticket: My printer is not working
🔎 Closest match:
[Agent will search for similar tickets and provide response]
```

## Project Structure

```
tech-support/
├── main.py              # Main agent implementation with dual modes
├── requirements.txt      # Python dependencies
├── README.md           # This file
├── .gitignore          # Git ignore rules
├── tools/              # Tools package
│   ├── __init__.py     # Tools initialization and exports
│   └── weaviate_tool.py # Weaviate search functionality
└── venv/               # Virtual environment (create locally)
```

## Dependencies

- `weaviate-client>=4.16.0` - Weaviate vector database client
- `langchain>=0.1.0` - LangChain framework
- `langchain-openai>=0.0.5` - OpenAI integration
- `langchain-community>=0.0.20` - Community integrations
- `langgraph>=0.0.20` - LangGraph for agent orchestration
- `python-dotenv>=1.0.0` - Environment variable management
- `openai>=1.98.0` - OpenAI Python client
- `protobuf>=6.31.1` - Protocol buffers
- `urllib3>=2.5.0` - HTTP client
- `requests>=2.32.4` - HTTP library

## How It Works

1. **Ticket Input**: User submits a new support ticket
2. **Vector Search**: The agent searches for similar past tickets using Weaviate
3. **Response Generation**: GPT-4o analyzes the search results and provides helpful information
4. **Conversation Flow**: LangGraph manages the conversation state and tool usage

## Troubleshooting

### Virtual Environment Issues
Make sure the virtual environment is activated:
```bash
source venv/bin/activate
```

### Import Errors
If you encounter import errors, reinstall dependencies:
```bash
pip install -r requirements.txt
```

### API Key Issues
Make sure your `.env` file contains a valid OpenAI API key:
```bash
OPENAI_API_KEY=sk-your-actual-api-key-here
```

### Weaviate Warnings
Protobuf warnings are normal and don't affect functionality. They're automatically suppressed.

## Development

The project uses a modular structure with:
- **Main Agent**: `main.py` handles user interaction and mode selection
- **Tools Package**: `tools/` contains all agent tools and utilities
- **Weaviate Integration**: Embedded vector database for similarity search

## License

This project is for educational and development purposes. 
