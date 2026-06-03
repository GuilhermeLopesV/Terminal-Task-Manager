from features_package.features import (
    add_task,
    list_tasks,
    remove_task,
    task_completed,
    terminal_commands,
    remove_completed_task,
)


from data_package.data_features import load_data


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
            remove_task(tasks, completed_tasks_list)
        elif command == '4':
            task_completed(tasks, completed_tasks_list)
        elif command == '5':
           remove_completed_task(tasks, completed_tasks_list)
        elif command == '6':
            print('Encerrando o Programa')
            break
        else:
            print('Comando desconhecido')

        print('\n')

mini_trello()