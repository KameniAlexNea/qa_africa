from typing import List, Union
from pydantic import BaseModel, Field

class AnswerChoice(BaseModel):
    letter: str = Field(
        description="The letter identifier for the answer choice (e.g., 'A', 'B', 'C'...)",
    )
    text: str = Field(
        description="The actual text content of the answer choice",
    )


class Question(BaseModel):
    question_number: Union[int, str] = Field(
        description="Sequential number identifying the question in the set",
    )
    question_text: str = Field(
        description="The actual text of the question being asked",
    )
    answer_choices: List[AnswerChoice] = Field(
        description="List of possible answer choices for the question",
    )
    correct_answers: List[str] = Field(
        description="List of letters corresponding to the correct answer choices. examples : ['A', 'C']",
    )
    explanation: str = Field(
        description="Factual detailed explanation of why the marked answers are correct",
    )


class QuestionBank(BaseModel):
    questions: List[Question] = Field(
        description="Collection of all questions in the question bank"
    )

