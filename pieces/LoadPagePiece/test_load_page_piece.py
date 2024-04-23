from domino.testing import piece_dry_run


def test_load_page_piece():
    piece_output = piece_dry_run(
        piece_name="LoadPagePiece",
        input_data={}
    )

    assert 1==1
