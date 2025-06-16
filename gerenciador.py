import func

tasks = []

while True:
  print("\n Menu de Gerenciador de Tarefas:")
  print("1. Adicionar tarefa")
  print("2. Ver tarefas")
  print("3. Atualizar tarefa")
  print("4. Completar tarefa")
  print("5. Deletar tarefas completadas")
  print("6. Sair")

  choice = input("Escolha uma opção: ")
  if choice == "1":
    task_name = input("Digite o nome da tarefa: ")
    task_description = input("Digite a descrição da tarefa: ")
    func.add_tasks(tasks, task_name, task_description)
  elif choice == "2":
    func.show_tasks(tasks)
  elif choice == "3":
    task_id = int(input("Digite o ID da tarefa que deseja atualizar: "))
    new_name = input("Digite o novo nome da tarefa: ")
    new_description = input("Digite a nova descrição da tarefa: ")
    func.update_task(tasks, task_id, new_name, new_description)
  elif choice == "4":
    task_id = int(input("Digite o ID da tarefa que deseja completar: "))
    func.complete_task(tasks, task_id)
  elif choice == "5":
    func.delete_tasks(tasks)
  elif choice == "6":
    break
  
print("Programa finalizado.")