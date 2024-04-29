from pydantic import BaseModel, Field


class InputModel(BaseModel):
    """
    Close Browser Piece Input Model
    """

    script: str = Field(
        description="Preceding script.",
    )


class OutputModel(BaseModel):
    """
    Close Browser Piece Output Model
    """

    script: str = Field(
        description="Parsed script of this piece.",
    )
