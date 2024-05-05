from pydantic import BaseModel, Field


class InputModel(BaseModel):
    """
    Take Screenshot Piece Input Model
    """

    script: str = Field(
        description="Preceding script.",
    )


class OutputModel(BaseModel):
    """
    Take Screenshot Piece Output Model
    """

    script: str = Field(
        description="Parsed script of this piece.",
    )

    image_path: str = Field(
        description="Path to the screenshot image.",
    )
