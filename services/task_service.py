from models.task import Task
import json

class TaskService:

    def __init__(self):
        self.tasks = {}
        self.next_id = 1
        try:
            self.load_tasks()
        except FileNotFoundError:
            print("Nenhum arquivo de tarefas encontrado. Iniciando vazio.")
    
    def create_task(self, title, delivery_date):
        new_task = Task(id=self.next_id, title=title, delivery_date=delivery_date)
        self.tasks[self.next_id] = new_task
        self.next_id += 1
        self.save_tasks()

        return new_task
    
    def list_tasks(self):

        return self.tasks.values()
    
    def complete_task(self, task_id):
        task = self.tasks.get(task_id)
        if task:
            task.status = True
            self.save_tasks()

        return task
    
    def delete_task(self, task_id):
        task = self.tasks.get(task_id)
        if task:
            self.tasks.pop(task_id)
            self.save_tasks()

        return task
    
    def save_tasks(self):
        tasks = self.list_tasks()
        tasks_list = []
        for task in tasks:
            tasks_list.append(task.to_dict())
        with open("task.json", "w") as f:
            json.dump(tasks_list, f)

    def load_tasks(self):
        with open("task.json", "r") as f:
            tasks_list = json.load(f)

        for task in tasks_list:
            task_loaded = Task.from_dict(task)
            self.tasks[task_loaded.id] = task_loaded
            if task_loaded.id >= self.next_id:
                self.next_id = task_loaded.id + 1