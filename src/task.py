class Task:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.completed = False

def create_task(name, description):
    return Task(name, description)
