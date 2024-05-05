from domino.base_piece import BasePiece

from .models import InputModel, OutputModel


class RunScriptPiece(BasePiece):

    def piece_function(self, input_data: InputModel):
        exec(input_data.script)
        message = "Script executed"
        return OutputModel(message=message)
