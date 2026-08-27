from src.main import personalized_welcome, welcome_message


def test_welcome_message():
    assert welcome_message("Ammy") == "Ammy, welcome to the Data Engineering course."


def test_personalized_welcome_trims_spaces():
    assert (
        personalized_welcome(" Evelyn ")
        == "Evelyn, welcome to the Data Engineering course."
    )


def test_personalized_welcome_empty_name():
    assert personalized_welcome("   ") == "Welcome to the Data Engineering course."
