# {{Task Tracker}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

<!-- Assumption is that the user doesn't wish to keep a list of the 
completed tasks, just remove them completely once marked complete -->

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class TaskTracker:
    # User-facing properties:
    #   name: task_list

    def __init__(self):
        # Parameters: none
        # Side effects: Sets the name of the self object (instance variable)
        pass # No code here yet

    def add(self, task: str):
        # Parameters:
        #   task: string representing a single task
        # Returns:
        #   Nothing
        # Side-effects: Saves the task to the self object
        pass # No code here yet

    def task_list(self):
        # Returns: a list containing all tasks not yet completed
        # Side-effects: None
        pass # No code here yet

    def mark_complete(self, task: str):
        # Returns nothing
        # Side-effects: Throws an exception if task does not exist
        pass # No code here yet
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
When a new TaskTracker object is created
#__init__ creates a new list of tasks
"""
task_tracker = TaskTracker()
task_tracker.task_list() # -> []

"""
Given a task
#add adds this to the task_list 
"""
task_tracker = TaskTracker()
task_tracker.add("Complete weekend challenge")
task_tracker.task_list() # -> ["Complete weekend challenge"]

"""
Given a task already in the task_list
#add raises an exception
"""
task_tracker = TaskTracker()
task_tracker.add("Complete weekend challenge")
task_tracker.add("Complete weekend challenge") # raises an error with the message "This task is already in the task list."

# """
# Given an empty task
# #add raises an error with the message "Task is empty! Enter a task."
# """
# task_tracker = TaskTracker()
# task_tracker.add("") # -> "Task is empty! Enter a task."
#REMOVED 

"""
When called,
#task_list displays the list of tasks not yet completed
"""
task_tracker = TaskTracker()
task_tracker.add("Complete weekend challenge")
task_tracker.add("Water the plants")
task_tracker.add("Post birthday card")
task_tracker.task_list() # -> ["Complete weekend challenge", "Water the plants", "Post birthday card"]

"""
When a task is marked as complete
It does not display in the task_list when list is accessed
"""
task_tracker = TaskTracker()
task_tracker.mark_complete("Water the plants")
task_tracker.task_list() # -> ["Complete weekend challenge", "Post birthday card"]

"""
When a user tries to mark a task not in the task list as complete
It raises an error
"""
task_tracker = TaskTracker()
task_tracker.mark_complete("Walk the dog")
task_tracker.task_list() # -> "Task not in task list"

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
