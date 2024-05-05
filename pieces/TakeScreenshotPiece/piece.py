import uuid
from string import Template

from domino.base_piece import BasePiece

from .models import InputModel, OutputModel

image_path = f"/screenshots/{str(uuid.uuid4())}.png"

template = Template(
"""
$script
self.logger.info("Taking screenshot")
driver.save_screenshot("$image_path")

"""
)


class TakeScreenshotPiece(BasePiece):

    def piece_function(self, input_data: InputModel):
        script = template.substitute(
            {
                "script": input_data.script,
                "image_path": image_path,
            }
        )
        return OutputModel(script=script, image_path=image_path)
