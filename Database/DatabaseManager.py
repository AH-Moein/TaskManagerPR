import sqlite3
from Classes.Member import Member
from Classes.Project import Project
from Classes.Task import Task


class DatabaseManager:
    def __init__(self, db_name="TaskManagement.db"):
        self.db_name = db_name

    def _execute_query(self, query, params=()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            return cursor

    # --- Section 1: Members ---
    def addMemberdb(self, member):
        try:
            query = "INSERT INTO members (name, role, email) VALUES (?, ?, ?)"
            self._execute_query(query, (member.name, member.role, member.email))
            print(f"Member '{member.name}' added successfully.")
        except Exception as e:
            print(f"Error: {e}")

    def get_all_members(self):
        query = "SELECT * FROM members"
        cursor = self._execute_query(query)
        rows = cursor.fetchall()
        members_list = []
        for row in rows:
            new_member = Member(row[1], row[2], row[3])
            new_member.id = row[0]
            members_list.append(new_member)
        return members_list

    # --- Section 2: Projects ---
    def create_project(self, project, manager_id):
        try:
            query = """
            INSERT INTO projects (name, description, manager_id, start_date, end_date)
            VALUES (?, ?, ?, ?, ?)
            """
            self._execute_query(
                query,
                (
                    project.ProjectName,
                    project.Description,
                    manager_id,
                    project.StartDate,
                    project.EndDate,
                ),
            )
            print(f"Project '{project.ProjectName}' created successfully.")
        except Exception as e:
            print(f"Error: {e}")

    def get_all_projects(self):
        query = "SELECT * FROM projects"
        cursor = self._execute_query(query)
        rows = cursor.fetchall()
        project_list = []
        for row in rows:
            new_project = Project(row[1], row[2], row[3], row[4], row[5])
            new_project.id = row[0]
            project_list.append(new_project)
        return project_list

    # --- Section 3: Tasks ---
    def CreateTask(self, task, project_id, assignee_id):
        try:
            query = """
            INSERT INTO tasks (project_id, title, description, assignee_id, deadline, status)
            VALUES (?, ?, ?, ?, ?, ?)
            """
            self._execute_query(
                query,
                (
                    project_id,
                    task.TaskName,
                    task.Description,
                    assignee_id,
                    task.Deadline,
                    task.Status,
                ),
            )
            print(f"Task '{task.TaskName}' added successfully.")
        except Exception as e:
            print(f"Error: {e}")

    def update_task_status(self, task_id, new_status):
        valid = ["ToDo", "In Progress", "Done"]
        if new_status not in valid:
            print("Error: Invalid status.")
            return

        query = "UPDATE tasks SET status = ? WHERE task_id = ?"
        self._execute_query(query, (new_status, task_id))
        print("Status updated.")

    def update_task_assignee(self, task_id, new_assignee_id):
        query = "UPDATE tasks SET assignee_id = ? WHERE task_id = ?"
        self._execute_query(query, (new_assignee_id, task_id))
        print("Reassigned successfully.")

    def get_tasks_by_project(self, project_id):
        query = "SELECT * FROM tasks WHERE project_id = ?"
        cursor = self._execute_query(query, (project_id,))
        rows = cursor.fetchall()
        tasks_list = []
        for row in rows:
            new_task = Task(row[2], row[3], row[4], row[5], row[6])
            new_task.id = row[0]
            tasks_list.append(new_task)
        return tasks_list

    def get_all_tasks(self):
        query = "SELECT * FROM tasks"
        cursor = self._execute_query(query)
        rows = cursor.fetchall()
        tasks_list = []
        for row in rows:
            new_task = Task(row[2], row[3], row[4], row[5], row[6])
            new_task.id = row[0]
            tasks_list.append(new_task)
        return tasks_list
