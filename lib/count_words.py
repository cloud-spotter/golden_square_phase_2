# Behaviour: 
# - takes string as an arg 
# - returns number of words in that string

def count_words(string):
    count = len(string.split())
    return count

# print(count_words("twenty green spiders on this plant"))