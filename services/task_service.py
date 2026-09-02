from models.task import Task


class TaskService:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def create_task(self, user_id, title, description):
        task = Task(
            task_id=self.next_id,
            title=title,
            description=description,
            user_id=user_id
        )

        self.tasks.append(task)
        self.next_id += 1
        return task

    def get_user_tasks(self, user_id):
        return [
            task for task in self.tasks
            if task.user_id == user_id
        ]

    def update_task(self, task_id, user_id, data):
        task = next(
            (task for task in self.tasks if task.id == task_id),
            None
        )

        if not task:
            return None, 404

        if task.user_id != user_id:
            return None, 403

        if "title" in data:
            task.title = data["title"]

        if "description" in data:
            task.description = data["description"]

        return task, 200

    def delete_task(self, task_id, user_id):
        task = next(
            (task for task in self.tasks if task.id == task_id),
            None
        )

        if not task:
            return 404

        if task.user_id != user_id:
            return 403

        self.tasks.remove(task)
        return 204
