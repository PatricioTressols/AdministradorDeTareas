# Importamos la biblioteca 'os' para limpiar la pantalla de la consola en algunas partes del programa
import os

# Función para limpiar la pantalla de la consola, depende del sistema operativo
def clear_screen():
    if os.name == 'nt':  # Si el sistema es Windows
        os.system('cls')
    else:  # Para otros sistemas como Linux o Mac
        os.system('clear')

# Esta es la lista donde se almacenarán las tareas
tasks = []

# Función para mostrar el menú principal
def show_menu():
    print("\n----- Administrador de Tareas -----")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")

# Función para agregar una nueva tarea
def add_task():
    task = input("\nIngrese la descripción de la tarea: ")
    tasks.append({"description": task, "completed": False})
    print(f"Tarea '{task}' agregada con éxito.")

# Función para listar todas las tareas
def list_tasks():
    if len(tasks) == 0:
        print("\nNo hay tareas en la lista.")
    else:
        print("\n----- Lista de Tareas -----")
        for i, task in enumerate(tasks, 1):
            status = "Completada" if task["completed"] else "Pendiente"
            print(f"{i}. {task['description']} - {status}")

# Función para marcar una tarea como completada
def complete_task():
    list_tasks()  # Primero mostramos la lista de tareas
    try:
        task_number = int(input("\nIngrese el número de la tarea a completar: "))
        if 0 < task_number <= len(tasks):
            tasks[task_number - 1]["completed"] = True
            print(f"Tarea '{tasks[task_number - 1]['description']}' marcada como completada.")
        else:
            print("Número de tarea inválido.")
    except ValueError:
        print("Por favor, ingrese un número válido.")

# Función para eliminar una tarea de la lista
def delete_task():
    list_tasks()  # Mostramos la lista de tareas
    try:
        task_number = int(input("\nIngrese el número de la tarea a eliminar: "))
        if 0 < task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"Tarea '{removed_task['description']}' eliminada.")
        else:
            print("Número de tarea inválido.")
    except ValueError:
        print("Por favor, ingrese un número válido.")

# Función principal que ejecuta el programa
def main():
    while True:
        clear_screen()  # Limpiamos la pantalla antes de mostrar el menú
        show_menu()  # Mostramos el menú principal
        choice = input("\nSeleccione una opción: ")

        if choice == '1':
            add_task()  # Agregar tarea
        elif choice == '2':
            list_tasks()  # Listar tareas
        elif choice == '3':
            complete_task()  # Marcar tarea como completada
        elif choice == '4':
            delete_task()  # Eliminar tarea
        elif choice == '5':
            print("Saliendo del programa...")
            break  # Salir del bucle
        else:
            print("Opción no válida, por favor intente de nuevo.")

        input("\nPresione Enter para continuar...")  # Pausa antes de volver al menú

# Verificamos si este archivo se está ejecutando directamente
if __name__ == "__main__":
    main()
