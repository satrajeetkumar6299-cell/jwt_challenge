from datetime import datetime


class Task:
    def __init__(self, task_id, title, description, user_id):
        self.id = task_id
        self.title = title
        self.description = description
        self.user_id = user_id
        self.created_at = datetime.utcnow()

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "user_id": self.user_id,
            "created_at": self.created_at.isoformat()
        }
