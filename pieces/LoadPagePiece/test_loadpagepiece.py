import importlib

from domino.testing import piece_dry_run


def test_load_page_piece():
    """
    def previous_script():
        foo = bar

    """

    input_data = {
        "url": "https://www.google.com",
        "script": test_load_page_piece.__doc__,
    }

    piece_output = piece_dry_run(piece_name="LoadPagePiece", input_data=input_data)

    test_script = f"""
        {input_data["script"]}
        self.logger.info(f"Loading URL: {input_data["url"]}")
        driver.get({input_data["url"]})

        """

    assert piece_output["script"] == test_script
