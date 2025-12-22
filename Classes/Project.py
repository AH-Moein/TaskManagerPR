class Project:
    def __init__(self, ProjectName, Description, PManager, StartDate, EndDate, id=0):
        self.id = id  # Project id (handle in DB) just for esasy work in Report and UI
        self.ProjectName = ProjectName
        self.Description = Description
        self.PManager = PManager
        self.StartDate = StartDate
        self.EndDate = EndDate
