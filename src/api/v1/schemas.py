from pydantic import BaseModel, Field

class TextInput(BaseModel):
    text: str = Field(
        ...,
        examples=["hello", "silent"],
        description="The text you want to analyse"
    )