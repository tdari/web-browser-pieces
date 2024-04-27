from domino.base_piece import BasePiece

from .models import InputModel, OutputModel


class OpenBrowserPiece(BasePiece):
    def piece_function(self, input_data: InputModel):
        """
from selenium import webdriver

self.logger.info("Execution started")

options = webdriver.ChromeOptions()

# try:
driver = webdriver.Remote(
    command_executor="http://localhost:4444/wd/hub"
)

self.logger.info("Maximizing window")

driver.maximize_window()
        
        """

        return OutputModel(script=self.piece_function.__doc__)
