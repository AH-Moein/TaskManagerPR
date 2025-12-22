from datetime import datetime, timedelta


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

    def postpone_task(self):

        _post = []

        _today = datetime.today().date()

        for task in self.tasks:

            _deadline = datetime.strptime(task.Deadline, "%Y-%m-%d").date()

            if _deadline < _today and task.Status != "Done":

                _post.append(task)

        return _post

    def person_task(self, person_id):
        _assigned = []

        target_id = None
        target_name = str(person_id).lower()

        if str(person_id).isdigit():
            target_id = int(person_id)

        for task in self.tasks:
            if target_id is not None and task.assignee_id == target_id:
                _assigned.append(task)
                continue

            for member in self.members:
                if member.id == task.assignee_id and member.name.lower() == target_name:
                    _assigned.append(task)
                    break

        return _assigned

    def project_summary(self, project_id):
        summary = []
        found = False

        for project in self.projects:
            if project.id == project_id:
                found = True
                summary.append("Project: " + project.ProjectName)
                summary.append("Description: " + project.Description)

                for task in self.tasks:
                    if project.id == task.project_id:
                        summary.append(
                            "Task: " + task.TaskName + ", Status: " + task.Status
                        )

        if not found:
            summary.append(f"No project found with id {project_id}")

        return summary

    def dueon_task(self):

        _due_on = []

        today = datetime.today().date()

        _max_due_on = today + timedelta(days=7)

        for task in self.tasks:

            _deadline = datetime.strptime(task.Deadline, "%Y-%m-%d").date()

            if today <= _deadline <= _max_due_on:

                _due_on.append(task)

        return _due_on

    def export_all_projects_summary(self, filename="projects_summary.txt"):

        with open(filename, "w", encoding="utf-8") as f:

            for project in self.projects:

                f.write("Project: " + project.ProjectName + "\n")

                f.write("Description: " + project.Description + "\n")

                for task in self.tasks:

                    if task.project_id == project.id:

                        f.write(
                            "Task: " + task.TaskName + ", Status: " + task.Status + "\n"
                        )

                f.write("\n")

        print("All project summaries exported to", filename)

        with open(filename, "r", encoding="utf-8") as f:
            print("\n===Project Summary===")
            print(f.read())

    def export_postpone_tasks_summary(self, filename="tasks_summary.txt"):

        _postpone = self.postpone_task()

        with open(filename, "w", encoding="utf-8") as f:

            f.write("Postponed Tasks Summary\n")

            f.write("=======================\n")

            if _postpone:

                for task in _postpone:

                    f.write(
                        f"Project: {task.project_id}, Task: {task.TaskName}, Deadline: {task.Deadline}, Status: {task.Status}\n"
                    )
            else:

                f.write("No postponed tasks.\n")

        with open(filename, "r", encoding="utf-8") as f:
            print("\n===Postponed Tasks Summary===")
            print(f.read())

    def export_members_tasks(self, filename="members_tasks.txt"):
        f = open(filename, "w", encoding="utf-8")
        f.write("Members Active Tasks\n")
        f.write("=======================\n")

        for member in self.members:
            my_tasks = []
            for task in self.tasks:
                if task.assignee_id == member.id:
                    my_tasks.append(task)

            if len(my_tasks) > 0:
                count_todo = 0
                count_inprogress = 0
                count_done = 0

                for t in my_tasks:
                    if t.Status == "ToDo":
                        count_todo = count_todo + 1
                    elif t.Status == "In Progress":
                        count_inprogress = count_inprogress + 1
                    elif t.Status == "Done":
                        count_done = count_done + 1

                header = "Name: " + member.name + " (Total: " + str(len(my_tasks)) + ")"
                details = (
                    " [ToDo: "
                    + str(count_todo)
                    + ", In Progress: "
                    + str(count_inprogress)
                    + ", Done: "
                    + str(count_done)
                    + "]\n"
                )

                f.write(header + details)

                for x in my_tasks:
                    line = (
                        "  Task: "
                        + x.TaskName
                        + ", Deadline: "
                        + x.Deadline
                        + ", Status: "
                        + x.Status
                        + "\n"
                    )
                    f.write(line)

                f.write("\n")

        f.close()

        print("Report exported to", filename)
        print("\n=== Preview ===")

        f = open(filename, "r", encoding="utf-8")
        content = f.read()
        print(content)
        f.close()
