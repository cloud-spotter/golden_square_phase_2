import pytest
from lib.reading_time_estimate import *

def test_return_result_of_calculation():
    result = reading_time_estimate(400)
    assert result == "This text will take 2 minutes to read"

def test_not_exact_division():
    result = reading_time_estimate(501)
    assert result == "This text will take 3 minutes to read"

def test_text_size_zero():
    result = reading_time_estimate(0)
    assert result == "No text to be read here"

def test_text_size_less_than_200_words():
    result = reading_time_estimate(50)
    assert result == "This text will take less than 2 minutes to read"