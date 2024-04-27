from domino.base_piece import BasePiece

from .models import InputModel, OutputModel


class LoadPagePiece(BasePiece):

    def piece_function(self, input_data: InputModel):
        # a better way?
        script = f"""
{input_data.script}
self.logger.info(f"Loading URL: {input_data.url}")
driver.get({input_data.url})

        """
        return OutputModel(script=script)
