class Task:
    def __init__(self, Title, Description, Assignee, Deadline, Status="ToDo"):
        self.Title = Title
        self.Description = Description
        self.Assignee = Assignee
        self.Deadline = Deadline
        self.Status = Status
