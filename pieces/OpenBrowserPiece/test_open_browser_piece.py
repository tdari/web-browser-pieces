from .piece import template

from domino.testing import piece_dry_run


def test_open_browser_piece():
    input_data = {
        "ip_addr": "127.0.0.1",
    }

    piece_output = piece_dry_run(piece_name="OpenBrowserPiece", input_data=input_data)

    assert piece_output["script"] == template.substitute({"ip_addr": input_data["ip_addr"]})
