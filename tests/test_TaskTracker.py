import pytest
from lib.TaskTracker import *

"""
When a new TaskTracker object is created
#__init__ creates a new list of tasks
"""
def test_new_tracker_object_creates_empty_task_list():
    task_tracker = TaskTracker()
    result = task_tracker.task_list() 
    assert result == []

"""
Given a task
#add adds this to the task_list 
"""
def test_add_task_to_task_list():
    task_tracker = TaskTracker()
    task_tracker.add("Complete weekend challenge")
    result = task_tracker.task_list() 
    assert result == ["Complete weekend challenge"]

"""
Given a task already in the task_list
#add raises an exception
"""
def test_add_does_not_add_duplicated_tasks():
    task_tracker = TaskTracker()
    task_tracker.add("Complete weekend challenge")
    with pytest.raises(Exception) as e:
        result = task_tracker.add("Complete weekend challenge") 
    error_message = str(e.value)
    assert error_message == "This task is already in the task list."

# raises an error with the message "This task is already in the task list."

"""
When called,
#task_list displays the list of tasks not yet completed
"""
def test_display_task_list():
    task_tracker = TaskTracker()
    task_tracker.add("Complete weekend challenge")
    task_tracker.add("Water the plants")
    task_tracker.add("Post birthday card")
    result = task_tracker.task_list() 
    assert result == ["Complete weekend challenge", "Water the plants", "Post birthday card"]

"""
When a task is marked as complete
It does not display in the task_list when the list is accessed
"""
def test_completed_tasks_do_not_display_in_task_list():
    task_tracker = TaskTracker()
    task_tracker.add("Complete weekend challenge")
    task_tracker.add("Post birthday card")
    task_tracker.mark_complete("Water the plants")
    result = task_tracker.task_list() 
    assert result == ["Complete weekend challenge", "Post birthday card"]

"""
When a task is marked as complete
It does not display in the task_list when list is accessed
"""
def test_completed_tasks_do_not_display_in_task_list():
    task_tracker = TaskTracker()
    with pytest.raises(Exception) as e:
        task_tracker.mark_complete("Walk the dog")
        result = task_tracker.task_list() 
    error_message = str(e.value)
    assert error_message == "Task not in task list"