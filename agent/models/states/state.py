from typing_extensions import TypedDict

class State(TypedDict):
    input_prompt: str
    my_name: str
    output: str

class InputState(TypedDict):
    input_prompt: str
    my_name: str
