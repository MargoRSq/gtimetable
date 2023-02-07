from typing import TypedDict


class ArgsDict(TypedDict):
    filename: str
    start: str
    until: str
    clear: bool
    credentials: str
    output: str
    evenness: int
