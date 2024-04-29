from domino.testing import piece_dry_run


def test_run_script_piece():
    script = """
def hello():
    print("hello world!")

"""

    input_data = {
        "script": script,
    }

    piece_output = piece_dry_run(piece_name="RunScriptPiece", input_data=input_data)

    assert piece_output["message"] == "Script executed"
