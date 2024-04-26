from pydantic import BaseModel, Field


class InputModel(BaseModel):
    pass


class OutputModel(BaseModel):
    """
    Load Page Piece Output Model
    """

    script: str = Field(
        description="Parsed script of this piece.",
    )
