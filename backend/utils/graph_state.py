# python imports
from typing import TypedDict, List

# schema of chat
class Chat(TypedDict):
    role: str
    msg: str

# schema of state
class GraphState(TypedDict):
    chat: List[Chat]