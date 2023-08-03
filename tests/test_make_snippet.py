import pytest
from lib.make_snippet import *

'''
return first five words of given string
'''

def test_snippet_returns_first_five_words_of_string():
    result = make_snippet("return first five words is")
    assert result == "return first five words is"

'''
if string is longer than 5 words
return first 5 words followed by ... instead of rest of string
'''

def test_snippet_returns_more_than_five_words_of_string():
    result = make_snippet("return first five words is next step")
    assert result == "return first five words is..."
'''
if string is empty
return just the string
'''
def test_snippet_returns_empty_string():
    result = make_snippet("")
    assert result == ""
'''
if argument is an integer
return error
'''
def test_snippet_returns_error_for_non_string():
    # make_snippet(5)
    with pytest.raises(Exception) as e:
        result = make_snippet(5)
    error_message = str(e.value)
    assert error_message == "Please enter a string"