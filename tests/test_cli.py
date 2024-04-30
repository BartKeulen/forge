from forge.cli import main


def test_cli(capsys):
    # Given
    args = ["John"]

    # When
    main(args)

    # Then
    captured = capsys.readouterr()
    assert captured.out == "Hello, John!\n"
