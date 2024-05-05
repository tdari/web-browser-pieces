from string import Template

from domino.base_piece import BasePiece

from .models import InputModel, OutputModel

template = Template(
"""
$script
self.logger.info("Taking screenshot")
driver.save_screenshot("$image_path")

"""
)


class TakeScreenshotPiece(BasePiece):

    def piece_function(self, input_data: InputModel):
        script = template.substitute({"script": input_data.script, "image_path": input_data.image})
        return OutputModel(script=script)
