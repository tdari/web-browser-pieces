from pydantic import BaseModel, Field


class InputModel(BaseModel):
    """
    Run Script Piece Input Model
    """

    script: str = Field(
        description="Script to execute.",
    )


class OutputModel(BaseModel):
    """
    Run Script Piece Output Model
    """

    message: str = Field(
        description="Parsed script of this piece.",
    )
