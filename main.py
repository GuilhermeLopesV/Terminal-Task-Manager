from features_package.features import (
    add_task,
    list_tasks,
    remove_task,
    task_completed,
    terminal_commands,
)


from data_package.data_features import load_data


def terminal_task_manager():

    tasks = load_data()

    while True:
        terminal_commands()

        command = input('Digite um comando: ')

        if command == '1':
            add_task(tasks)
        elif command == '2':
            list_tasks(tasks)
        elif command == '3':
            remove_task(tasks)
        elif command == '4':
            task_completed(tasks)
        elif command == '5':
            print('Encerrando o Programa')
            break
        else:
            print('Comando desconhecido')

        print('\n')


terminal_task_manager()