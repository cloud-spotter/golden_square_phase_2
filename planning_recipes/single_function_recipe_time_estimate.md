# {{Reading Time Estimate}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._



```python
# EXAMPLE
def reading_time_estimate(text_size):
    """Extracts uppercase words from a string

    Parameters: (list all parameters and their types)
        text_size: an integer that is the number of words in a text (e.g. 300)

    Returns: (state the return value and its type)
        a string with converted integer (minutes) as an estimate reading time for the text (e.g. 12)

    Side effects: (state any side effects)
        If the data type returned is not an integer, this could impact any other functions using
        the output.

        User-friendliness: function needs to return a readable output that makes sense to a human.
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given an integer text size
Function returns an integer (the calculated time to read in)
"""
reading_time_estimate(400) => ["This text will take 2 minutes to read"]

"""
Given an integer not divisible by 200
The calculation returns a float and rounds this to an integer
The function returns the string with converted integer
"""
reading_time_estimate(678) => ["This text will take 3 minutes to read"]

"""
Given an integer of 0
It returns a string message saying "No text to be read here"
"""
reading_time_estimate(0) => ["No text to be read here"]

"""
Given a text size 0 < text_size < 200 words
It returns a string message  
"""
reading_time_estimate(50) => ["This text will take less than 2 minutes to read"]


_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]

```

Ensure all test function names are unique, otherwise pytest will ignore them!


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
