class ReportManager:
    def __init__(self, db_manager):
        self.db = db_manager
        self.members = []
        self.projects = []
        self.tasks = []

        self.load_data()

    def load_data(self):
        self.members = self.db.get_all_members()
        self.projects = self.db.get_all_projects()
        self.tasks = self.db.get_all_tasks()
