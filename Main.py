from Database.DatabaseManager import DatabaseManager
from Database.Database import create_tables
from Classes.Report import ReportManager
from Classes.Project import Project
from Classes.Member import Member
from Classes.Task import Task
import datetime


def input_int(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Invalid number. Try again.")


def input_date(msg):
    while True:
        val = input(f"{msg} (YYYY-MM-DD): ")
        try:
            datetime.datetime.strptime(val, "%Y-%m-%d")
            return val
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD")


def main():
    create_tables()
    db = DatabaseManager("TaskManagement.db")
    repo = ReportManager(db)

    while True:
        print("\n--- Main Menu ---")
        print("1. Member Management")
        print("2. Project Management")
        print("3. Task Management")
        print("4. Reports")
        print("5. Exit")

        choice = input("Select: ")

        if choice == "1":
            print("\n(1) Member Management")
            print("1. Add New Member")
            print("2. Show All Members")
            sub = input("Select: ")

            if sub == "1":
                n = input("Name: ")
                r = input("Role: ")
                e = input("Email: ")
                db.addMemberdb(Member(n, r, e))
            elif sub == "2":
                for m in db.get_all_members():
                    print(f"[ID: {m.id}] {m.name} - {m.role} - {m.email}")

        elif choice == "2":
            print("\n(2) Project Management")
            print("1. Create New Project")
            print("2. Show All Projects")
            sub = input("Select: ")

            if sub == "1":
                n = input("Name: ")
                d = input("Description: ")
                mid = input_int("Manager ID: ")
                s = input_date("Start Date")
                e = input_date("End Date")
                db.create_project(Project(n, d, mid, s, e), mid)
            elif sub == "2":
                for p in db.get_all_projects():
                    print(f"[ID: {p.id}] {p.ProjectName} - {p.Description}")

        elif choice == "3":
            print("\n(3) Task Management")
            print("1. Create New Task")
            print("2. Change Task Status")
            print("3. Reassign Task")
            print("4. Show Project Tasks")
            print("5. Show Person Tasks")
            print("6. Show Tasks by Status")
            sub = input("Select: ")

            if sub == "1":
                pid = input_int("Project ID: ")
                t = input("Title: ")
                d = input("Description: ")
                aid = input_int("Assignee ID: ")
                dl = input_date("Deadline")
                db.CreateTask(Task(t, d, aid, dl, "ToDo"), pid, aid)

            elif sub == "2":
                tid = input_int("Task ID: ")
                s = input("New Status (ToDo/In Progress/Done): ")
                db.update_task_status(tid, s)

            elif sub == "3":
                tid = input_int("Task ID: ")
                aid = input_int("New Assignee ID: ")
                db.update_task_assignee(tid, aid)

            elif sub == "4":
                pid = input_int("Project ID: ")
                tasks = db.get_tasks_by_project(pid)
                if not tasks:
                    print("No tasks found.")
                for t in tasks:
                    print(
                        f"Task: {t.TaskName} | Status: {t.Status} | Deadline: {t.Deadline}"
                    )
            elif sub == "5":
                aid = input_int("Assignee ID: ")
                tasks = db.get_tasks_by_assignee(aid)
                if not tasks:
                    print("No tasks found for this member.")
                for t in tasks:
                    print(
                        f"Task: {t.TaskName} | Status: {t.Status} | Project ID: {t.project_id}"
                    )

            elif sub == "6":
                stat = input("Status (ToDo/In Progress/Done): ")
                tasks = db.get_tasks_by_status(stat)
                if not tasks:
                    print(f"No tasks found with status '{stat}'.")
                for t in tasks:
                    print(
                        f"Task: {t.TaskName} | Deadline: {t.Deadline} | Assignee ID: {t.assignee_id}"
                    )

        elif choice == "4":
            print("\n(4) Reports")
            repo = ReportManager(db)
            print("1. Show Postponed Tasks")
            print("2. Show Tasks Due in 7 Days")
            print("3. Show Project Summary")
            print("4. Export All Projects Summary to File")
            print("5. Export Postponed Tasks Summary to File")
            print("6. Export Members Active Tasks to File")
            print("7. Show Person Tasks")
            sub = input("Select: ")

            if sub == "1":
                postponed = repo.postpone_task()
                if not postponed:
                    print("No postponed tasks.")
                else:
                    for t in postponed:
                        print(
                            f"Task: {t.TaskName} | Deadline: {t.Deadline} | Status: {t.Status}"
                        )

            elif sub == "2":
                dueon = repo.dueon_task()
                if not dueon:
                    print("No tasks due in next 7 days.")
                else:
                    for t in dueon:
                        print(
                            f"Task: {t.TaskName} | Deadline: {t.Deadline} | Status: {t.Status}"
                        )

            elif sub == "3":
                pid = input_int("Project ID: ")
                summary = repo.project_summary(pid)
                for line in summary:
                    print(line)

            elif sub == "4":
                repo.export_all_projects_summary()

            elif sub == "5":
                repo.export_postpone_tasks_summary()

            elif sub == "6":
                repo.export_members_tasks()

            elif sub == "7":
                pid = input("Person ID or Name: ")
                tasks = repo.person_task(pid)
                if not tasks:
                    print("No tasks found for this person.")
                else:
                    for t in tasks:
                        print(
                            f"Task: {t.TaskName} | Deadline: {t.Deadline} | Status: {t.Status}"
                        )

        elif choice == "5":
            break
        else:
            print("Invalid option")


if __name__ == "__main__":
    main()
