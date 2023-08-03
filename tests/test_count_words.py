from lib.count_words import *

'''
Check function returns count of words in string
'''

def test_count_words_in_string():
    result = count_words("twenty green spiders on this plant")
    assert result == 6