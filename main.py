tarefas = []
tarefas_concluidas = []

def comandos():
    print('1 - Adicionar tarefa')
    print('2 - listar tarefa')
    print('3 - Remover tarefa')
    print('4 - marcar tarefa como concluída')
    print('5 - Sair')

def adicionar_tarefa(lista):
    tarefa = input('Qual tarefa deseja adicionar: ')
    print('Adicionando tarefa')
    lista.append(tarefa)
    print('Tarefa adicionada com sucesso')
    terminal_orgnizador()

def listar_tarefa(lista1, lista2):
    if not lista1:
        print('Nenhuma tarefa cadastrada.')
    else:
        print('Suas Tarefas')
        for i, tarefa in enumerate(lista1, start=1):
            print(f'{i} - {tarefa}')
        if lista2:
            terminal_orgnizador()
            print('Suas Tarefas concluídas')
            for i, tarefa in enumerate(lista2, start=1):
                print(f'{i} - {tarefa} ✅')

            terminal_orgnizador()

def remover_tarefa(lista):
    if not lista:
        print('Nenhuma tarefa cadastrada.')
    else:
        print('Suas Tarefas')
        for i, tarefa in enumerate(lista, start=1):
            print(f'{i} - {tarefa}')
        print('Digite o índice da tarefa que deseja remover, lembrando que o índice começa com 0')
        remover = int(input('Qual índice: '))
        remove = lista.pop(remover)
        print(f'Tarefa {remove}, removida com sucesso')
        terminal_orgnizador()

def tarefa_concluida(lista):
    if not lista:
        print('Nenhuma tarefa cadastrada.')
    else:
        print('Suas Tarefas')
        for i, tarefa in enumerate(lista, start=1):
            print(f'{i} - {tarefa}')
        print('Digite o índice da tarefa que deseja marcar como concluído, lembrando que o índice começa com 0')
        tarefa_escolhida = int(input('Qual índice: '))
        tarefas_concluidas.append(lista[tarefa_escolhida])
        lista.pop(tarefa_escolhida)
        print('Tarefa concluída com sucesso')
        terminal_orgnizador()

def terminal_orgnizador():
    print()
    print()
    print()

def mini_trello():

    while True:
        terminal_orgnizador()
        comandos()

        comando = input('Digite um comando: ')

        if comando == '1':
            adicionar_tarefa(tarefas)
        elif comando == '2':
            listar_tarefa(tarefas, tarefas_concluidas)
        elif comando == '3':
            remover_tarefa(tarefas)
        elif comando == '4':
            tarefa_concluida(tarefas)
        elif comando == '5':
            print('Encerrando o Programa')
            break
        else:
            print('Comando desconhecido')


mini_trello()