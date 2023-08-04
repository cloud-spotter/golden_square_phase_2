class TaskTracker:
    '''A class to represent a to-do list tracker'''
    def __init__(self) -> None:
        self.tasks = []

    def add(self, task: str):
        # Returns: Nothing
        # Side-effects: Saves the task to the self object
        if task in self.tasks:
            raise Exception("This task is already in the task list.")
        else:
            self.tasks.append(task)

    def task_list(self):
        return self.tasks

    def mark_complete(self, task: str):
        # Returns nothing
        # Side-effects: Throws an exception if task does not exist
        if task in self.tasks:
            self.task.pop(task)
        else:
            raise Exception("Task not in task list")
