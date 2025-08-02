# Tech Support Agent

A LangGraph-based agent for technical support tasks.

## Setup

### 1. Virtual Environment

The virtual environment has been set up with all required dependencies:

```bash
# Activate the virtual environment
source venv/bin/activate

# Verify setup
python test_setup.py
```

### 2. Environment Variables

Create a `.env` file in the project root with your API keys:

```bash
# OpenAI API Key
OPENAI_API_KEY=your_openai_api_key_here

# Optional: Notion API Token (for future use)
# NOTION_TOKEN=your_notion_token_here
```

### 3. Get API Keys

- **OpenAI API Key**: Get your API key from [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)
- **Notion Token** (optional): For future Notion integration features

## Usage

### Test the Setup

```bash
# Verify all packages are installed correctly
python test_setup.py
```

### Run the Agent

```bash
# Run the main agent
python main.py
```

## Project Structure

```
tech-support/
├── main.py              # Main agent implementation
├── test_setup.py        # Setup verification script
├── requirements.txt      # Python dependencies
├── README.md           # This file
└── venv/               # Virtual environment (created)
```

## Dependencies

- `langchain==0.1.0` - LangChain framework
- `langchain-openai==0.0.5` - OpenAI integration
- `langgraph==0.0.20` - LangGraph for agent orchestration
- `python-dotenv==1.0.0` - Environment variable management
- `openai>=1.10.0,<2.0.0` - OpenAI Python client

## Troubleshooting

### SSL Warning
If you see SSL warnings, this is normal on macOS and doesn't affect functionality.

### Import Errors
If you encounter import errors, make sure the virtual environment is activated:
```bash
source venv/bin/activate
```

### API Key Issues
Make sure your `.env` file contains a valid OpenAI API key:
```bash
OPENAI_API_KEY=sk-your-actual-api-key-here
``` 