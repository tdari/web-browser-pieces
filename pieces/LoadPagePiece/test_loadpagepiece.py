import importlib

from domino.testing import piece_dry_run


def test_load_page_piece():
    script = """
    def previous_script():
        foo = bar

    """

    input_data = {
        "url": "https://www.google.com",
        "script": script,
    }

    piece_output = piece_dry_run(piece_name="LoadPagePiece", input_data=input_data)

    piece_module = importlib.import_module("LoadPagePiece.piece")

    assert piece_output["script"] == piece_module.template.substitute(
        {"script": input_data["script"], "url": input_data["url"]}
    )
