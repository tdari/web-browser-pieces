from pydantic import BaseModel, Field


class InputModel(BaseModel):
    """
    Load Page Piece Input Model
    """
    script: str = Field(
        description="Preceding script.",
    )

    url: str = Field(
        description="Page url to be loaded.",
    )


class OutputModel(BaseModel):
    """
    Load Page Piece Output Model
    """

    script: str = Field(
        description="Parsed script of this piece.",
    )
