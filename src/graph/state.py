from typing import TypedDict, List

class GraphState(TypedDict):
    """
    Represents the state of the graph

    Attributes:
        question: question
        generation: LLM generation
        websearch: whether to add search
        documents: list of documents
    """

    question: str
    generation: str
    websearch: bool
    documents: List[str]

    