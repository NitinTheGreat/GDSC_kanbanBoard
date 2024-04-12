class Task:
    def __init__(self, task_id, title, description, assignee, reporter, status, priority):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.assignee = assignee
        self.reporter = reporter
        self.status = status
        self.priority = priority

    def to_dict(self):
        """Convert Task object to a dictionary."""
        return {
            'task_id': self.task_id,
            'title': self.title,
            'description': self.description,
            'assignee': self.assignee,
            'reporter': self.reporter,
            'status': self.status,
            'priority': self.priority
        }



class Board:
    def __init__(self, board_id, name):
        self.board_id = board_id
        self.name = name
        self.tasks = []
