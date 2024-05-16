

from programs import reverse_string


def test_reverse_string_success():
    input_string = "Rama"
    actual = reverse_string(input_string) # the real output you got after program execution.
    expected = "amaR" # this is expected.

    # print(result)

    assert actual == expected # amaR == amaR


def test_reverse_string_failure():
    input_string = "Rama"
    actual = reverse_string(input_string) # the real output you got after program execution.
    expected = "amar" # this is expected.

    # print(result)

    assert actual != expected # amaR != amar