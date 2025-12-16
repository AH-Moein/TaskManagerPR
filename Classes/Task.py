class Task:
    def __init__(self, TaskName, Description, Assignee, Deadline, Status="ToDo"):
        self.TaskName = TaskName
        self.Description = Description
        self.Assignee = Assignee
        self.Deadline = Deadline
        self.Status = Status
