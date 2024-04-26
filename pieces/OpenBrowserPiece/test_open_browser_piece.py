import importlib

from domino.testing import piece_dry_run


def test_open_browser_piece():
    """
    open browser piece
    """

    piece_output = piece_dry_run(piece_name="OpenBrowserPiece", input_data={})

    piece_module = importlib.import_module("OpenBrowserPiece.piece")
    piece_class = getattr(piece_module, "OpenBrowserPiece")

    assert piece_output["script"] == piece_class.piece_function.__doc__
