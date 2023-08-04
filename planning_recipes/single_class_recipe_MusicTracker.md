# {{Music Tracker}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.

Assumption: user only wants to keep track of listening to songs/music by title 
i.e. not further types of metadata such as composer/lyricist. 
Storage: list

Assumption: user only wants to keep track of unique tracks they've listened to. No duplicates.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class MusicTracker:
    # User-facing properties:
    #   listening_diary: list

   def __init__(self):
        # Parameters: none
        # Returns: Nothing
        # Side effects: Sets the name of the self object (instance variable)
        pass # No code here yet

    def add(self, track: str):
        # Returns: Nothing
        # Side-effects: Saves the task to the self object (listening_diary)
        pass # No code here yet

    def listening_list(self):
        # Returns: a list containing all tracks listened to
        # Side-effects: None
        pass # No code here yet
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
1. When a new MusicTracker object is created
#__init__ creates a new empty list to store tracks listened to
"""
music_tracker = MusicTracker()
music_tracker.listening_list() # -> []

"""
2. Given a track 
#add adds this to the listening list 
"""
music_tracker = MusicTracker()
music_tracker.add("Supermassive Black Hole")
music_tracker.listening_list() # -> ["Supermassive Black Hole"]

"""
3. Given a track already in the listening list
#add raises an exception instead of adding it to the list
"""
music_tracker = MusicTracker()
music_tracker.add("Supermassive Black Hole")
music_tracker.add("Supermassive Black Hole") # raises an error with the message "This track is already in your listening list."

"""
4. Given a non-string
#add raises an exception and displays an error messsage
"""
music_tracker = MusicTracker()
music_tracker.add(7) # raises an error with the message "Please enter a string."

"""
5. When called,
#listening_list displays the list of tracks listened to
"""
music_tracker = MusicTracker()
music_tracker.add("Supermassive Black Hole")
music_tracker.add("Blackbird")
music_tracker.add("Take the A Train")
music_tracker.listening_list() # -> ["Supermassive Black Hole", "Blackbird, "Take the A Train"]

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_class_recipe_template.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_class_recipe_template.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_class_recipe_template.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_class_recipe_template.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_class_recipe_template.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
