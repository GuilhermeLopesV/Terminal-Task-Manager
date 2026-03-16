from features_package.features import *

def mini_trello():

    while True:
        comandos()

        comando = input('Digite um comando: ')

        if comando == '1':
            adicionar_tarefa(tasks)
        elif comando == '2':
            listar_tarefa(tasks, tarefas_concluidas_lista)
        elif comando == '3':
            remover_tarefa(tasks)
        elif comando == '4':
            tarefa_concluida(tasks)
        elif comando == '5':
            print('Encerrando o Programa')
            break
        else:
            print('Comando desconhecido')

        print('\n')

mini_trello()