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

    # Section 1
    # Add member function for add a member into DB
    def addMemberdb(self, member):
        query = "INSERT INTO members (name, role, email) VALUES (?, ?, ?)"
        self._execute_query(query, (member.name, member.role, member.email))
        print(f"Member '{member.name}' added successfully.")

    # Return all member fron DB
    def get_all_members(self):
        query = "SELECT * FROM members"
        cursor = self._execute_query(query)
        rows = cursor.fetchall()
        members_list = []
        for row in rows:
            new_member = Member(row[1], row[2], row[3])
            members_list.append(new_member)
        return members_list

    # Section2
    # Create Project and add to DB
    def create_project(self, project, manager_id):
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

    # return all projects from DB
    def get_all_projects(self):
        query = "SELECT * FROM projects"
        cursor = self._execute_query(query)
        rows = cursor.fetchall()
        project_list = []
        for row in rows:
            new_project = Project(row[1], row[2], row[3], row[4], row[5])
            project_list.append(new_project)
        return project_list
