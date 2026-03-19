import features_package.features as features



def mini_trello():

    tasks, completed_tasks_list = features.load_data()

    while True:
        features.terminal_commands()

        command = input('Digite um comando: ')

        if command == '1':
            features.add_task(tasks, completed_tasks_list)
        elif command == '2':
            features.list_tasks(tasks, completed_tasks_list)
        elif command == '3':
            features.remove_task(tasks, completed_tasks_list)
        elif command == '4':
            features.task_completed(tasks, completed_tasks_list)
        elif command == '5':
            features.remove_completed_task(tasks, completed_tasks_list)
        elif command == '6':
            print('Encerrando o Programa')
            break
        else:
            print('Comando desconhecido')

        print('\n')

mini_trello()