# Project 1

## About

This project is maintained by **Goutham Krishna**.
[GitHub Profile](https://github.com/gouthamkriz)

## Step-by-Step Guide

### 1. Install Required Packages

Make sure you have the following packages installed:

```bash
pip install langchain-core langchain-openai langchain langgraph python-dotenv
```

### 2. Import the Modules

You can add these imports at the top of your Python script:

```python
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv
```

Or, you can test the imports directly in your terminal (Python REPL):

```bash
python
>>> from langchain_core.messages import HumanMessage
>>> from langchain_openai import ChatOpenAI
>>> from langchain.tools import tool
>>> from langgraph.prebuilt import create_react_agent
>>> from dotenv import load_dotenv
```

### 3. Load Environment Variables

Before using APIs, load your environment variables:

```python
load_dotenv()
```

### 4. Use the Imported Modules

- **HumanMessage**: For creating human message objects.
- **ChatOpenAI**: For interacting with OpenAI chat models.
- **tool**: For defining custom tools.
- **create_react_agent**: For creating a React agent with LangGraph.
- **load_dotenv**: For loading environment variables from a `.env` file.

Refer to the official documentation for detailed usage examples.