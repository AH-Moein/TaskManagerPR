class Task:
    def __init__(
        self,
        TaskName,
        Description,
        Assignee,
        Deadline,
        Status="ToDo",
        project_id=0,
        assignee_id=0,
        id=0,
    ):
        self.TaskName = TaskName
        self.Description = Description
        self.Assignee = Assignee
        self.Deadline = Deadline
        self.Status = Status
        self.project_id = project_id
        self.assignee_id = assignee_id
        self.id = id
