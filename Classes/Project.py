class Project:
    def __init__(self, ProjectName, Description, PManager, StartDate, EndDate, id=0):
        self.ProjectName = ProjectName
        self.Description = Description
        self.PManager = PManager
        self.StartDate = StartDate
        self.EndDate = EndDate
        self.id = id
