class Task:
    
    def __init__(self, id, title, delivery_date, status=False):
        self.id = id
        self.title = title
        self.status = status
        self.delivery_date = delivery_date

    def __str__(self):
        text_status = "Concluída" if self.status else "Pendete"
        message = f"[{self.id}] - {self.title} - {text_status} - Entrega: {self.delivery_date}"
        
        return message
    
    def to_dict(self):
        task_dict = {
            "id" : self.id,
            "title" : self.title,
            "status" : self.status,
            "delivery_date" : self.delivery_date
        }

        return task_dict
    
    @staticmethod
    def from_dict(task_dict):
        id = task_dict["id"]
        title = task_dict["title"]
        delivery_date = task_dict["delivery_date"]
        status = task_dict["status"]

        return Task(id=id, title=title, delivery_date=delivery_date, status=status)
    
