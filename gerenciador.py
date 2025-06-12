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
    add_tasks(tasks, task_name, task_description)
  elif choice == "2":
    show_tasks(tasks)
  elif choice == "6":
    break
  
print("Programa finalizado.")