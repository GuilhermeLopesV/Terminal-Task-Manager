tarefas = []
tarefas_concluidas_lista = []
prioridades = ('ALTA', 'MEDIA', 'BAIXA')
ordem_prioridade = {
    "ALTA": 1,
    "MEDIA": 2,
    "BAIXA": 3
}

def comandos():
    print('1 - Adicionar tarefa')
    print('2 - listar tarefa')
    print('3 - Remover tarefa')
    print('4 - marcar tarefa como concluída')
    print('5 - Sair')
    print('\n')

def adicionar_tarefa(lista):
    try:
        tarefa = input('Qual tarefa deseja adicionar: ')

        print('Tipos de prioridade: Alta, Media, Baixa')
        prioridade_da_tarefa = input('Prioridade da tarefa: ').upper()

        if tarefa:
            if prioridade_da_tarefa in prioridades:
                lista.append({
                    "nome": tarefa,
                    "prioridade": prioridade_da_tarefa,
                })
                print('Tarefa adicionada com sucesso!')
            else:
                print('Prioridade desconhecida!')

        else:
            print('Resposta invalida.')

    except ValueError:
        print('Resposta invalida.')




def listar_tarefa(lista1, lista2):
    if not lista1:
        print('Nenhuma tarefa cadastrada.')
    else:
        tarefas_ordenadas = sorted(
            lista1,
            key=lambda ta: ordem_prioridade[ta["prioridade"]]
        )

        for tarefa in tarefas_ordenadas:
            print(f'{tarefa["nome"]} | Prioridade: {tarefa["prioridade"]}')

        if lista2:
            terminal_orgnizador()
            print('Suas Tarefas concluídas')
            for i, tarefa in enumerate(lista2, start=1):
                print(f'{i} - {tarefa["nome"]} ✅')

            print('\n')

def remover_tarefa(lista):
    if not lista:
        print('Nenhuma tarefa cadastrada.')
        return

    for i, tarefa in enumerate(lista, start=1):
        print(f'{i} - {tarefa}')

    try:
        remover = int(input('Qual é o número da tarefa que deseja remover: '))
        indice_real = remover - 1

        if 0 <= indice_real < len(lista):
            removida = lista.pop(indice_real)
            print(f'Tarefa "{removida}" removida com sucesso.')
        else:
            print('Índice inválido.')
    except ValueError:
        print('Digite apenas números.')


def tarefa_concluida(lista):
    if not lista:
        print('Nenhuma tarefa cadastrada.')
        return

    for i, tarefa in enumerate(lista, start=1):
        print(f'{i} - {tarefa}')

    try:
        tarefa_c = int(input('Qual é o número da tarefa que deseja marca como concluída: '))
        indice_real = tarefa_c - 1

        if 0 <= indice_real < len(lista):
            tarefas_concluidas_lista.append(lista[indice_real])
            lista.pop(indice_real)
            print('Tarefa concluida com sucesso.')
        else:
            print('Índice inválido.')

    except ValueError:
        print('Digite apenas números.')

def terminal_orgnizador():
    print('\n' * 2)
