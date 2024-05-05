import importlib

from domino.testing import piece_dry_run


def test_take_screenshot_piece():
    script = """
    def previous_script():
        foo = bar

    """

    input_data = {
        "script": script,
    }

    piece_output = piece_dry_run(
        piece_name="TakeScreenshotPiece",
        input_data=input_data,
    )

    piece_module = importlib.import_module("TakeScreenshotPiece.piece")
    image_path = "/home/shared_storage/screenshot.png"

    assert piece_output["script"] == piece_module.template.substitute(
        {"script": input_data["script"], "image_path": image_path}
    )

    assert piece_output["image_path"].endswith(".png")
