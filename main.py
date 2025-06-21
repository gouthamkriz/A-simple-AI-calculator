from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

load_dotenv()

@tool
def calculater(a: float, b: float) -> str:
    """A simple calculator tool that adds two numbers together."""
    print("The tool has been called")
    return f"The sum of {a} and {b} is {a + b}"

@tool
def greeting(name) -> str:
    """Usefull to greet users with his name."""
    print("The tool has been called")
    return f"Hello {name}, how can I assist you today?"

def main():
    model = ChatOpenAI(temperature=0)

    tools = [calculater]
    agent_executor = create_react_agent(model, tools)

    print("Welcome! Iam your AI assistant. How can I help you today? Type 'exit' to quit.")
    print("You can ask me to perform calculations or chat with me")

    while True:
        user_input = input("\nYou: ").strip()

        if user_input == "exit":
            print("Goodbye!")
            break
        print("\nAssistant: ", end="")
        for chunk in agent_executor.stream(
            {"messages": [HumanMessage(content=user_input)]}
        ):
            if "agent" in chunk and "messages" in chunk["agent"]:
                for message in chunk["agent"]["messages"]:
                    print(message.content, end="")
        print()

if __name__ == "__main__":
    main()