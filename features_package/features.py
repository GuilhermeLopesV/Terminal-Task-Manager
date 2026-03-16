tasks = []
completed_tasks_list = []
priorities = ('ALTA', 'MEDIA', 'BAIXA')
order_of_priority = {
    "ALTA": 1,
    "MEDIA": 2,
    "BAIXA": 3
}


def to_do_list_by_priority(task_lists, **kwargs):
    status = kwargs.get("status", "")  # pega o status se existir

    ordered_tasks = sorted(
        task_lists,
        key=lambda task: order_of_priority[task["prioridade"]]
    )

    for i, task in enumerate(ordered_tasks, start=1):
        print(f'{i} - {task["nome"]} | Prioridade: {task["prioridade"]} {status}')


def to_do_list_in_order(task_lists):
    for i, task in enumerate(task_lists, start=1):
        print(f'{i} - {task["nome"]} | Prioridade: {task["prioridade"]}')

def bar_spacing():
    print('----///----')


def terminal_commands():
    print('1 - Adicionar tarefa')
    print('2 - listar tarefa')
    print('3 - Remover tarefa')
    print('4 - marcar tarefa como concluída')
    print('5 - Sair')
    print('\n')

def add_task(to_do_list):
    try:
        task = input('Qual tarefa deseja adicionar: ').strip()

        if not task:
            print("Entrada vazia.")
            return

        print('Tipos de prioridade: Alta, Media, Baixa')
        task_priority = input('Prioridade da tarefa: ').upper()

        if task:
            if task_priority in priorities:
                to_do_list.append({
                    "nome": task,
                    "prioridade": task_priority,
                })
                print('Tarefa adicionada com sucesso!')
            else:
                print('Prioridade desconhecida!')

        else:
            print('Resposta invalida.')

    except ValueError:
        print('Resposta invalida.')



def list_tasks(to_do_list, tasks_completed):
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
        to_do_list_by_priority(completed_tasks_list, status="✅")

        print('\n')


def remove_task(task_lists):
    if not task_lists:
        print('Nenhuma tarefa cadastrada.')
        return

    print("Tarefas (ordem de criação):")
    to_do_list_in_order(task_lists)

    try:
        remove = int(input('Qual é o número da tarefa que deseja remover: '))
        real_index = remove - 1

        if 0 <= real_index < len(task_lists):
            removed = task_lists.pop(real_index)
            print(f'Tarefa "{removed["nome"]}"| Prioridade: {removed["prioridade"]} removida com sucesso. ❌')

        else:
            print('Índice inválido.')
    except ValueError:
        print('Digite apenas números.')


def task_completed(task_lists):
    if not task_lists:
        print('Nenhuma tarefa cadastrada.')
        return

    print("Tarefas (ordem de criação):")
    to_do_list_in_order(task_lists)

    try:
        task_that_will_be_marked_as_completed = int(input('Qual é o número da tarefa que deseja marca como concluída: '))
        real_index = task_that_will_be_marked_as_completed - 1

        if 0 <= real_index < len(task_lists):
            completed_tasks_list.append(task_lists[real_index])
            task_lists.pop(real_index)
            print('Tarefa concluida com sucesso.')
        else:
            print('Índice inválido.')

    except ValueError:
        print('Digite apenas números.')
