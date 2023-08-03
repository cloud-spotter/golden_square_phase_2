import pytest
from lib.diary_entry import *

'''
Given an empty title
Raises an exception and displays an error message
'''
def test_error_raised_on_empty_title():
    with pytest.raises(Exception) as e:
        DiaryEntry("", "")
    error_message = str(e.value)
    assert error_message == "Diary entries must have a title and contents" 

'''
Given empty contents
Raises an exception and displays an error message
'''
def test_error_raised_on_empty_contents():
    with pytest.raises(Exception) as e:
        DiaryEntry("", "")
    error_message = str(e.value)
    assert error_message == "Diary entries must have a title and contents" 

'''
Given a title and some contents
#format returns a formatted entry
e.g. "A Title: Here is some content"
'''
def test_format_title_and_contents():
    diary_entry = DiaryEntry("A Title", "Here is some content")
    result = diary_entry.format()
    assert result == "A Title: Here is some content"

'''
Given a diary entry (title and contents)
#count_words returns the number of words contained in the entry
'''
def test_count_diary_entry_words():
    diary_entry = DiaryEntry("Golden Square", "Definitely still working on Debugging skills")
    result = diary_entry.count_words()
    assert result == f"Total words in this diary entry: 8"

'''
Given a wpm of 100
And diary contents with 30 words
#reading_time returns 0 minutes
'''
def test_reading_time_in_mins_with_100_wpm_and_30_words():
    content_for_test = """
    Definitely still working on Debugging skills. 
    Unsure of why the exception raised in the constructor method 
    needs to come before the instance variables are defined.
    #TODO Check with coach tomorrow."""
    diary_entry = DiaryEntry("Golden Square", content_for_test)
    result = diary_entry.reading_time(100)
    assert result == 0

'''
Given a number of words the user can read per minute
#reading_time returns an estimate of the reading time in minutes for the given contents
'''
def test_reading_time_in_mins_for_content():
    diary_entry = DiaryEntry("Golden Square", """Definitely still working on Debugging skills. 
    Unsure of why the exception raised in the constructor method 
    needs to come before the instance variables are defined.
    #TODO Check with coach tomorrow.""")
    result = diary_entry.reading_time(200)
    assert result == 0

'''
Given a wpm of 0
Raises an error (otherwise it will take infinity to read)
'''
def test_reading_time_of_zero_wpm():
    diary_entry = DiaryEntry("A Title", "Here is some content")
    with pytest.raises(Exception) as e:
        diary_entry.reading_time(0)
    assert str(e.value) == "Cannot calculate reading time for wpm of 0"

'''
Given contents of 10 words
And wpm of 2
And minutes of 3
#reading_chunk returns the first 6 words
'''
def test_content_of_10_words_with_2_wpm_and_1_minutes_reading_time():
    diary_entry = DiaryEntry("10 word test", "one two three four five six seven eight nine ten")
    result = diary_entry.reading_chunk(2, 1)
    assert result == "one two"

'''
Given contents of 6 words
And wpm of 2
And minutes of 1
#reading_chunk returns "one two", first time
Next time, returns "three four"
Next time, returns "five six"
'''
def test_content_of_6_words_with_2_wpm_and_1_minutes_called_multiple_times():
    diary_entry = DiaryEntry("6 word test", "one two three four five six")
    assert diary_entry.reading_chunk(2, 1) == "one two"
    assert diary_entry.reading_chunk(2, 1) == "three four"
    assert diary_entry.reading_chunk(2, 1) == "five six"

'''
Given contents of 6
If #reading_chunk is called repeatedly, with an exact ending
The last chunk == last words in contents
The next chunk after that is at the start again
'''
def test_reading_chunk_wraps_around_on_multiple_calls_with_exact_ending():
    diary_entry = DiaryEntry("6 word test", "one two three four five six")
    assert diary_entry.reading_chunk(2, 2) == "one two three four"
    assert diary_entry.reading_chunk(2, 1) == "five six"
    assert diary_entry.reading_chunk(2, 2) == "one two three four"