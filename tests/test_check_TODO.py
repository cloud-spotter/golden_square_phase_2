import pytest
from lib.check_TODO import *

"""
Given a string with #TODO inside, upper case
It returns True
"""
def test_check_TODO_uppercase():
    result = check_TODO("Here is my #TODO list for Monday")
    assert result == True

"""
Given a string with #todo inside, lower case 
It returns True
"""
def test_check_TODO_lowercase():
    result = check_TODO("Here is my #todo list for Monday")
    assert result == True

"""
Given a string with #TODO hidden inside a word in that string
It returns True
"""
def test_check_TODO_hidden_in_word():
    result = check_TODO("Here is my #todolist for Monday")
    assert result == True

"""
Given an empty string
It raises an exception
"""
def test_check_TODO_empty_string():
    with pytest.raises(Exception) as e:
        check_TODO("") 
    error_message = str(e.value)
    assert error_message == "Text is empty!"