from string import Template

from domino.base_piece import BasePiece

from .models import InputModel, OutputModel

template = Template(
"""
from selenium import webdriver

self.logger.info("Execution started")

options = webdriver.ChromeOptions()

driver = webdriver.Remote(
    command_executor='http://$ip_addr:4444/wd/hub',
    options=options
)

self.logger.info("Maximizing window")

driver.maximize_window()
"""
)


class OpenBrowserPiece(BasePiece):
    def piece_function(self, input_data: InputModel):
        script = template.substitute({"ip_addr": input_data.ip_addr})
        return OutputModel(script=script)
