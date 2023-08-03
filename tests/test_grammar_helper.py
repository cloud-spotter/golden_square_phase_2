import pytest 
from lib.grammar_helper import *

'''
Given a lower case text string
It returns the string with the first word capitalised, and end punctuation
'''
def test_capitalises_lower_case_string():
    result = grammar_helper("this is an example to work on") 
    assert result == "This is an example to work on."

'''
Given a string already capitalised and with appropriate end punctuation
It returns the same string
'''
def test_returns_appropriate_string_as_is():
    result = grammar_helper("This string is fine as it is.") 
    assert result == "This string is fine as it is."

'''
Given a lower case string with unsuitable end punctuation
It returns a capitalised string with suitable end punctuation
'''
def test_lower_case_string_with_unsuitable_end_punctuation():
    result = grammar_helper("This string needs suitable end punctuation;")
    assert result == "This string needs suitable end punctuation." 

'''
Given a mixed case string with suitable end punctuation
It returns a capitalised string with suitable end punctuation
'''
def test_mixed_case_string_with_suitable_end_punctuation():
    result = grammar_helper("HeLLo, WORLD!") 
    assert result == "Hello, world!"

'''
Given an empty string
It raises an exception
'''
def test_empty_string(): 
    with pytest.raises(Exception) as e:
        result = grammar_helper("")
    error_message = str(e.value)
    assert error_message == "Cannot punctuate an empty string"