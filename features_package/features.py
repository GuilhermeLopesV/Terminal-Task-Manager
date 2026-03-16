tasks = []
tarefas_concluidas_lista = []
prioridades = ('ALTA', 'MEDIA', 'BAIXA')
ordem_prioridade = {
    "ALTA": 1,
    "MEDIA": 2,
    "BAIXA": 3
}


def to_do_list_by_priority(task_lists, **kwargs):
    status = kwargs.get("status", "")  # pega o status se existir

    tarefas_ordenadas = sorted(
        task_lists,
        key=lambda task: ordem_prioridade[task["prioridade"]]
    )

    for i, tarefa in enumerate(tarefas_ordenadas, start=1):
        print(f'{i} - {tarefa["nome"]} | Prioridade: {tarefa["prioridade"]} {status}')


def to_do_list_in_order(task_lists):
    for i, tarefa in enumerate(task_lists, start=1):
        print(f'{i} - {tarefa["nome"]} | Prioridade: {tarefa["prioridade"]}')

def bar_spacing():
    print('----///----')


def comandos():
    print('1 - Adicionar tarefa')
    print('2 - listar tarefa')
    print('3 - Remover tarefa')
    print('4 - marcar tarefa como concluída')
    print('5 - Sair')
    print('\n')

def adicionar_tarefa(to_do_list):
    try:
        tarefa = input('Qual tarefa deseja adicionar: ').strip()

        if not tarefa:
            print("Entrada vazia.")
            return

        print('Tipos de prioridade: Alta, Media, Baixa')
        prioridade_da_tarefa = input('Prioridade da tarefa: ').upper()

        if tarefa:
            if prioridade_da_tarefa in prioridades:
                to_do_list.append({
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



def listar_tarefa(to_do_list, tasks_completed):
    if not to_do_list:

        print('Nenhuma tarefa cadastrada na lista de tarefas.')
        if tasks_completed:
            bar_spacing()
    else:
        to_do_list_by_priority(to_do_list)

    if not tasks_completed:
        bar_spacing()
        print('Nenhuma tarefa concluída')
    else:
        print('Suas Tarefas concluídas')
        to_do_list_by_priority(tarefas_concluidas_lista, status="✅")

        print('\n')


def remover_tarefa(task_lists):
    if not task_lists:
        print('Nenhuma tarefa cadastrada.')
        return

    print("Tarefas (ordem de criação):")
    to_do_list_in_order(task_lists)

    try:
        remover = int(input('Qual é o número da tarefa que deseja remover: '))
        indice_real = remover - 1

        if 0 <= indice_real < len(task_lists):
            removida = task_lists.pop(indice_real)
            print(f'Tarefa "{removida["nome"]}"| Prioridade: {removida["prioridade"]} removida com sucesso. ❌')

        else:
            print('Índice inválido.')
    except ValueError:
        print('Digite apenas números.')


def tarefa_concluida(task_lists):
    if not task_lists:
        print('Nenhuma tarefa cadastrada.')
        return

    print("Tarefas (ordem de criação):")
    to_do_list_in_order(task_lists)

    try:
        tarefa_c = int(input('Qual é o número da tarefa que deseja marca como concluída: '))
        indice_real = tarefa_c - 1

        if 0 <= indice_real < len(task_lists):
            tarefas_concluidas_lista.append(task_lists[indice_real])
            task_lists.pop(indice_real)
            print('Tarefa concluida com sucesso.')
        else:
            print('Índice inválido.')

    except ValueError:
        print('Digite apenas números.')
