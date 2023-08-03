# {{Grammar Helper}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def grammar_helper(text_string):
    """Checks a string for capitalised text and correct final punctuation 

    Parameters: (list all parameters and their types)
        a string: a string containing words (e.g. "this is an example to work on")

    Returns: (state the return value and its type)
        a capitalised string with appropriate end punctuation (e.g. "This is an example to work on!")

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

'''
Given a lower case text string
It returns the string with the first word capitalised, and end punctuation
'''
grammar_helper("this is an example to work on") => "This is an example to work on."

"""
Given a string already capitalised and with appropriate end punctuation
It returns the same string
"""
grammar_helper("This string is fine as it is.") => "This string is fine as it is."

"""
Given a lower case string with unsuitable end punctuation
It returns a capitalised string with suitable end punctuation
"""
grammar_helper("This string needs suitable end punctuation;") => "This string needs suitable end punctuation." 

"""
Given a mixed case string with suitable end punctuation
It returns a capitalised string with suitable end punctuation
"""
grammar_helper("HeLLo, WORLD!") => "Hello, world!"

"""
Given an empty string
It raises an exception
"""
grammar_helper("") => ""

"""
Given a None value
It throws an error
"""
grammar_helper() => (None) throws an error
```

<!-- Could go into quite a lot of detail here, e.g. if text_string is a question, 
needs question mark (this makes it more complex though). Assume simple case with "." as default end punctuation but will accept "!" or "?" if already there. -->


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
