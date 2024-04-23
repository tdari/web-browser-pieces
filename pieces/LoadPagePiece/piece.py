from domino.base_piece import BasePiece
from .models import InputModel, OutputModel


class LoadPagePiece(BasePiece):

    def piece_function(self, input_data: InputModel):
        return OutputModel()
