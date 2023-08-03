import pytest
from lib.GrammarStats import *

'''
Given an empty text
#check raises an error and displays an error message
'''
def test_check_empty_text_raises_error():
    grammar_stats = GrammarStats()
    with pytest.raises(Exception) as e:
        grammar_stats.check("")
    error_message = str(e.value)
    assert error_message == "Text must be a string and cannot be empty."

'''
Given a non-string
#check raises an error and displays an error message
'''
def test_check_non_string_raises_error():
    grammar_stats = GrammarStats()
    with pytest.raises(Exception) as e:
        grammar_stats.check(3)
    error_message = str(e.value)
    assert error_message == "Text must be a string and cannot be empty."

'''
Given a string starting with a capital letter 
and ending with a full stop
#check returns True
'''
def test_check_capital_letter_and_full_stop():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("Spider mites have been eating my cucumber plant.")
    assert result == True

'''
Given a string starting with a capital letter 
and ending with any allowed end punctuation
#check returns True
'''
def test_check_capital_letter_and_appropriate_end_punctuation():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("Spider mites have been eating my cucumber plant!")
    assert result == True

'''
Given a string starting without a capital letter 
and ending with a full stop
#check returns False
'''
def test_check_no_capital_letter_but_full_stop():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("spider mites have been eating my cucumber plant.")
    assert result == False

'''
Given a string starting with a capital letter 
but without suitable end punctuation
#check returns False
'''
def test_check_capital_letter_but_unsuitable_end_punctuation():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("Spider mites have been eating my cucumber plant:")
    assert result == False

'''
When called with one correct check
#percentage_good returns 100 
'''
def test_one_correct_check_returns_100_percent_of_tests_passing_check():
    grammar_stats = GrammarStats()
    grammar_stats.check("Spider mites have been eating my cucumber plant!")
    result = grammar_stats.percentage_good()
    assert result == 100

'''
When called with two correct checks and one incorrect check
#percentage_good rounds the result and
returns an integer percentage of tests passing #check
'''
def test_2_out_of_3_checks_returns_rounded_percentage():
    grammar_stats = GrammarStats()
    grammar_stats.check("Spider mites have been eating my cucumber plant!") # -> Pass
    grammar_stats.check("I've dowsed them in neem oil now.")                # -> Pass
    grammar_stats.check("i'm not holding out for cucumbers this year")      # -> Fail
    result = grammar_stats.percentage_good()
    assert result == 67

'''
When called with multiple checks
#percentage_good returns an integer percentage of tests passing #check
'''
def test_multiple_checks_returns_percentage_of_tests_passing_check():
    grammar_stats = GrammarStats()
    grammar_stats.check("Correct!")
    grammar_stats.check("Correct.")
    grammar_stats.check("Correct?")
    grammar_stats.check("Also correct!")
    grammar_stats.check("Correct too.")
    grammar_stats.check("incorrect.")
    result = grammar_stats.percentage_good()
    assert result == 83