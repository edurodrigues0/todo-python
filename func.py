import os
import platform

def clear_terminal():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def add_tasks(tasks, task_name, task_description):
  task = {
    "id": len(tasks) + 1,
    "name": task_name,
    "description": task_description,
    "is_completed": False,
  }

  # Add new task
  tasks.append(task)
  clear_terminal()

  print("Tarefa adicionada com sucesso!")
  return

def show_tasks(tasks):
  clear_terminal()
  print("Lista de tarefas:")
  for task in tasks:
    print(f"ID: {task['id']}")
    print(f"Nome: {task['name']}")
    print(f"Descrição: {task['description']}")
    print(f"Status: {'Concluída' if task['is_completed'] else 'Pendente'}")
    print("-" * 20)
  return

def update_task(tasks, task_id, new_name, new_description):
  for task in tasks:
    if task["id"] == task_id:
      task["name"] = new_name
      task["description"] = new_description
      clear_terminal()
      print("Tarefa atualizada com sucesso!")
      return

def complete_task(tasks, task_id):
  for task in tasks:
    if task["id"] == task_id:
      task["is_completed"] = True
      name = task["name"]
      clear_terminal()
      print(f"Tarefa {name} marcada como concluida")

def delete_tasks(tasks):
  for task in tasks:
    if task["is_completed"]:
      tasks.remove(task)

  clear_terminal()
  print("Tarefas completadas deletadas com sucesso!")
