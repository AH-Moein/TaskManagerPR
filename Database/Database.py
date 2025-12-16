import sqlite3


def create_tables():

    with sqlite3.connect("TaskManagement.db") as connection:
        conn = connection.cursor()

    conn.execute(
        """
    CREATE TABLE IF NOT EXISTS members (
        member_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        role TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL
    )
    """
    )

    conn.execute(
        """
    CREATE TABLE IF NOT EXISTS projects (
        project_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT,
        manager_id INTEGER,
        start_date TEXT,
        end_date TEXT,
        FOREIGN KEY (manager_id) REFERENCES members (member_id)
    )
    """
    )

    conn.execute(
        """
    CREATE TABLE IF NOT EXISTS tasks (
        task_id INTEGER PRIMARY KEY AUTOINCREMENT,
        project_id INTEGER NOT NULL,
        title TEXT NOT NULL,
        description TEXT,
        assignee_id INTEGER,
        deadline TEXT,
        status TEXT CHECK(status IN ('ToDo', 'In Progress', 'Done')) DEFAULT 'ToDo',
        FOREIGN KEY (project_id) REFERENCES projects (project_id),
        FOREIGN KEY (assignee_id) REFERENCES members (member_id)
    )
    """
    )
    print("Table Created Succesful")


if __name__ == "__main__":
    create_tables()
