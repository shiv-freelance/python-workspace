
# filename: should starts with test_*.py (or) *_test.py
# testcase: test_*(), *_test()

# assert

# pip install pytest
# python -m pip install pytest

# def test_check():
#     assert False # validations




from programs import reverse_string, is_palindrome


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



def test_ispalindrom_success():
    input_str = "madam"

    actual = is_palindrome(input_str) # True
    expected = True # True

    assert actual == expected


def test_ispalindrom_failure():
    input_str = "Janaki"

    actual = is_palindrome(input_str) # False
    expected = False # False

    assert actual == expected


import pytest

def test_is_palindrome_empty_string():
    assert is_palindrome("") == True

def test_is_palindrome_single_character():
    assert is_palindrome("a") == True

def test_is_palindrome_multiple_characters():
    assert is_palindrome("racecar") == True

def test_is_palindrome_not_palindrome():
    assert is_palindrome("hello") == False

def test_is_palindrome_mixed_case():
    assert is_palindrome("RaCeCaR") == True

def test_is_palindrome_with_spaces():
    assert is_palindrome("race car") == False

def test_is_palindrome_with_punctuation():
    assert is_palindrome("A man, a plan, a canal: Panama") != True

def test_is_palindrome_with_numbers():
    assert is_palindrome("12321") == True

def test_is_palindrome_with_unicode():
    assert is_palindrome("saippuakivikauppias") == True  # Finnish for "soapstone vendor"