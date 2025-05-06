from agent.models.states.state import State
from langchain_openai import ChatOpenAI

def generate_response(state: State) -> State:
    """
    Generates a response based on the provided state using a language model.
    Args:
        state (State): A dictionary containing the following keys:
            - 'input_prompt' (str): The input query or prompt to be processed.
            - 'my_name' (str): The name of the user to be included in the prompt.
    Returns:
        State: A dictionary containing the key:
            - 'output' (str): The generated response content from the language model.
    """

    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0
    )

    input_prompt = state['input_prompt']
    my_name = state['my_name']

    prompt = f"My name is {my_name}. This is my query: {input_prompt}"
    response = llm .invoke(prompt)

    return {"output": response.content}
