from agent.models.states.state import State

def lower_case(state: State) -> State:
    """
    Converts the value of the 'my_name' key in the given state dictionary to lowercase.
    Args:
        state (State): A dictionary containing a key 'my_name' with a string value.
    Returns:
        State: A new dictionary with the 'my_name' key's value converted to lowercase.
    """
    lowered_name = state['my_name'].lower()
    return {"my_name": lowered_name}