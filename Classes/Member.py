class Member:
    def __init__(self, name, role, email, id=0):
        self.id = id  # Class member - id sets in database (auto increment)
        self.name = name
        self.role = role
        self.email = email
