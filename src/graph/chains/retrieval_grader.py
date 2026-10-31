from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(temperature=0, model="gpt-4o-mini")


class GradeDocuments(BaseModel):
    """Binary score for relavence check on retrieved documents."""

    binary_score: str = Field(
        description= "Documents are relavent to the Question, 'yes' or 'no'"
    )

structured_llm_grader = llm.with_structured_output(GradeDocuments)

system = """
    You are a gradder assessing relavence of a retrived document to a user question.
    If the document contains keyword(s) or semantic meaning related to the question, grade it as releavent
    Give a binar score 'yes' or 'no' score to indicate whether the document is relavent to the
    question
"""

grade_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        ("human", "Retrived documents: {documents} User Question: {question}")
    ]
)

retrieval_grader = grade_prompt | structured_llm_grader