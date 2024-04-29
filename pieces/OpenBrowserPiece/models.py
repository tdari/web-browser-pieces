from pydantic import BaseModel, Field


class InputModel(BaseModel):
    """
    Open Browser Piece Input Model
    """
    ip_addr: str = Field(
        description="Ip address of remote web driver host."
    )

    port: str = Field(
        description="Port number of remote web driver host."
    )


class OutputModel(BaseModel):
    """
    Open Browser Piece Output Model
    """

    script: str = Field(
        description="Parsed script of this piece.",
    )
