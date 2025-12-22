class Task:
    def __init__(
        self,
        TaskName,
        Description,
        Assignee,
        Deadline,
        Status="ToDo",  # Defualt ToDO for change later
        project_id=0,
        assignee_id=0,
        id=0,
    ):  # formatted with vs code Extensions

        self.id = id  # Task id (handle in DB) just for esasy work in Report and UI (identify Task id)
        self.TaskName = TaskName
        self.Description = Description
        self.Assignee = Assignee
        self.Deadline = Deadline
        self.Status = Status
        self.project_id = project_id
        self.assignee_id = assignee_id
