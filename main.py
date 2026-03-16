from features_package.features import *

# Problema nas tarefas concluídas, problama quando eu encerro o programa de forma forçada e impossibilidade de remover
# tarefas marcadas como concluídas.

def mini_trello():

    tasks, completed_tasks_list = load_data()

    while True:
        terminal_commands()

        command = input('Digite um comando: ')

        if command == '1':
            add_task(tasks, completed_tasks_list)
        elif command == '2':
            list_tasks(tasks, completed_tasks_list)
        elif command == '3':
            remove_task(tasks)
        elif command == '4':
            task_completed(tasks, completed_tasks_list)
        elif command == '5':
            print('Encerrando o Programa')
            break
        else:
            print('Comando desconhecido')

        print('\n')

mini_trello()