from services.task_service import TaskService

service = TaskService()

def get_valid_task_id():
    task_id = input("Informe o ID da tarefa: ")
    task_id = task_id.strip()
    if task_id.isnumeric() and int(task_id) > 0:
        return int(task_id)

while True:
    
    print("Selecione uma opção: ")
    print("1 - Criar tarefa")
    print("2 - Listar tarefas")
    print("3 - Concluir tarefa")
    print("4 - Deletar tarefa")
    print("0 - Sair")

    opcao = input("Opção: ")

    if opcao == "1":
        title = input("Informe o título:")
        delivery_date = input("Informe a data de entrega:")
        task = service.create_task(title=title, delivery_date=delivery_date)
        print(f"Tarefa criada: {task}!")

    elif opcao == "2":
        print("Tarefas existentes: ")
        tasks = service.list_tasks()
        for task in tasks:
            print(task)

    elif opcao == "3":
        task_id = get_valid_task_id()
        if not task_id:
            print("ID Inválido")
        else:
            task = service.complete_task(task_id)
            if task:
                print(f"Tarefa {task_id} concluída!")
            else:
                print("Tarefa não encontrada!")

    elif opcao == "4":
        task_id = get_valid_task_id()
        if not task_id:
            print("ID Inválido")
        else:
            task = service.delete_task(task_id)
            if task:
                print(f"Tarefa {task_id} deletada!")
            else:
                print("Tarefa não encontrada!")

    elif opcao == "0":
        break