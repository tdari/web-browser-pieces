from string import Template

from domino.base_piece import BasePiece

from .models import InputModel, OutputModel

template = Template(
"""
$script
driver.quit()
"""
)

class CloseBrowserPiece(BasePiece):

    def piece_function(self, input_data: InputModel):
        script = template.substitute({"script": input_data.script})
        return OutputModel(script=script)
