from string import Template

from domino.base_piece import BasePiece

from .models import InputModel, OutputModel

template = Template(
"""
$script
self.logger.info("Loading URL: $url")
driver.get("$url")
"""
)


class LoadPagePiece(BasePiece):

    def piece_function(self, input_data: InputModel):
        script = template.substitute(
            {"script": input_data.script, "url": input_data.url}
        )
        return OutputModel(script=script)
