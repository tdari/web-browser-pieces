from domino.testing import piece_dry_run

from .piece import template


def test_open_browser_piece():
    input_data = {"ip_addr": "127.0.0.1", "port": "4444"}

    piece_output = piece_dry_run(piece_name="OpenBrowserPiece", input_data=input_data)

    assert piece_output["script"] == template.substitute(
        {"ip_addr": input_data["ip_addr"], "port": input_data["port"]}
    )
