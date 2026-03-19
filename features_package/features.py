import json

priorities = ('ALTA', 'MEDIA', 'BAIXA')
order_of_priority = {
    "ALTA": 1,
    "MEDIA": 2,
    "BAIXA": 3
}


def save_data(tasks, completed_tasks_list):
    data = {
        'tasks': tasks,
        'completed_tasks_list': completed_tasks_list,
    }
    with open("features_package/tasks.json", "w") as arquivo:
        json.dump(data, arquivo, indent=4)



def load_data():
    try:
        with open("features_package/tasks.json", "r") as arquivo:
            data = json.load(arquivo)
        return data["tasks"], data["completed_tasks_list"]
    except FileNotFoundError:
        return [], []

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
    print('4 - Marcar tarefa como concluída')
    print('5 - Remover tarefa marcada como concluída ')
    print('6 - Sair')
    print('\n')

def add_task(tasks, completed_tasks_list):
    try:
        task = input('Qual tarefa deseja adicionar: ').strip()

        if not task:
            print("Entrada vazia.")
            return

        print('Tipos de prioridade: Alta, Media, Baixa')
        task_priority = input('Prioridade da tarefa: ').upper()

        if task:
            if task_priority in priorities:
                tasks.append({
                    "nome": task,
                    "prioridade": task_priority,
                })

                save_data(tasks, completed_tasks_list)

                print('Tarefa adicionada com sucesso!')
            else:
                print('Prioridade desconhecida!')

        else:
            print('Resposta invalida.')

    except ValueError:
        print('Resposta invalida.')



def list_tasks(tasks, completed_tasks_list):
    if not tasks:

        print('Nenhuma tarefa cadastrada na lista de tarefas.')
        if completed_tasks_list:
            bar_spacing()
    else:
        to_do_list_by_priority(tasks)

    if not completed_tasks_list:
        bar_spacing()
        print('Nenhuma tarefa concluída')
    else:
        print('Suas Tarefas concluídas')
        to_do_list_by_priority(completed_tasks_list, status="✅")

        print('\n')


def remove_task(tasks, completed_tasks_list):
    if not tasks:
        print('Nenhuma tarefa cadastrada.')
        return

    print("Tarefas (ordem de criação):")
    to_do_list_in_order(tasks)

    try:
        remove = int(input('Qual é o número da tarefa que deseja remover: '))
        real_index = remove - 1

        if 0 <= real_index < len(tasks):
            removed = tasks.pop(real_index)
            print(f'Tarefa "{removed["nome"]}"| Prioridade: {removed["prioridade"]} removida com sucesso. ❌')

            save_data(tasks, completed_tasks_list)

        else:
            print('Índice inválido.')
    except ValueError:
        print('Digite apenas números.')


def task_completed(tasks, completed_tasks_list):
    if not tasks:
        print('Nenhuma tarefa cadastrada.')
        return

    print("Tarefas (ordem de criação):")
    to_do_list_in_order(tasks)

    try:
        task_that_will_be_marked_as_completed = int(input('Qual é o número da tarefa que deseja marca como concluída: '))
        real_index = task_that_will_be_marked_as_completed - 1

        if 0 <= real_index < len(tasks):
            completed_tasks_list.append(tasks[real_index])
            tasks.pop(real_index)
            print('Tarefa concluida com sucesso.')

            save_data(tasks, completed_tasks_list)
        else:
            print('Índice inválido.')

    except ValueError:
        print('Digite apenas números.')


def remove_completed_task(tasks, completed_tasks_list):
    if not completed_tasks_list:
        print('Nenhuma tarefa cadastrada.')
        return

    print("Tarefas (ordem de criação):")
    to_do_list_in_order(completed_tasks_list)

    try:
        remove = int(input('Qual é o número da tarefa que deseja remover: '))
        real_index = remove - 1

        if 0 <= real_index < len(completed_tasks_list):
            removed = completed_tasks_list.pop(real_index)
            print(f'Tarefa "{removed["nome"]}"| Prioridade: {removed["prioridade"]} removida com sucesso. ❌')

            save_data(tasks, completed_tasks_list)

        else:
            print('Índice inválido.')
    except ValueError:
        print('Digite apenas números.')