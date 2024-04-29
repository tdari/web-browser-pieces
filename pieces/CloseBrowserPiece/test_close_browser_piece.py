import importlib

from domino.testing import piece_dry_run


def test_close_browser_piece():
    script = """
def hello():
    print("hello world!")
    
"""

    input_data = {
        "script": script,
    }

    piece_output = piece_dry_run(piece_name="CloseBrowserPiece", input_data=input_data)

    piece_module = importlib.import_module("CloseBrowserPiece.piece")

    assert piece_output["script"] == piece_module.template.substitute(
        {"script": input_data["script"]}
    )
