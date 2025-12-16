import sys
import os

sys.path.append(os.getcwd())

from Database.DatabaseManager import DatabaseManager
from Classes.Member import Member
from Classes.Project import Project


def main():
    db = DatabaseManager("TaskManagement.db")

    while True:
        print("\n--- Task Management ---")
        print("1.Add Member")
        print("2.Show Members")
        print("3.Add Project")
        print("4.Exit")

        choice = input("Select : ")

        if choice == "1":
            name = input("Name : ")
            role = input("Role : ")
            email = input("Email :")

            new_member = Member(name, role, email)
            try:
                db.add_member(new_member)
            except Exception as e:
                print(f"Error{e}")

        elif choice == "2":
            projs = db.get_all_members()
            print(f"\nلیست اعضا ({len(projs)} نفر):")
            for m in projs:
                print(f"- {m.name} ({m.role}) - {m.email}")

        elif choice == "3":
            p_name = input("نام پروژه: ")
            desc = input("توضیحات: ")
            s_date = input("تاریخ شروع (YYYY-MM-DD): ")
            e_date = input("تاریخ پایان (YYYY-MM-DD): ")

            print("\nیک نفر را به عنوان مدیر پروژه انتخاب کنید (شناسه را وارد کنید):")
            manager_id = input("شناسه (ID) مدیر پروژه: ")

            new_project = Project(p_name, desc, manager_id, s_date, e_date)
            db.create_project(new_project, manager_id)

        elif choice == "4":
            print("exit")
            break
        else:
            print("Wrong Choice")


if __name__ == "__main__":
    main()
