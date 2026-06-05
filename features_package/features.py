import time
from data_package.data_features import save_data


def get_current_time():
    return time.strftime('%d/%m/%Y %H:%M:%S')

priorities = ('ALTA', 'MEDIA', 'BAIXA')
order_of_priority = {
    "ALTA": 1,
    "MEDIA": 2,
    "BAIXA": 3
}

order_of_status = {
    "pendente": 1,
    "concluída": 2
}

def to_do_list_by_priority(task_lists):
    ordered_tasks = sorted(
        task_lists,
        key=lambda task: (
            order_of_status[task["status"]],
            order_of_priority[task["prioridade"]]
        )
    )

    for i, task in enumerate(ordered_tasks, start=1):
        emoji = "⏳" if task["status"] == "pendente" else "✅"

        print(f"[{i}] Tarefa: {task['nome']}")
        print(f"    Prioridade: {task['prioridade']}")
        print(f"    Status: {task['status']} {emoji}")
        print(f"    Criado em: {task['horario']}")
        print("-" * 25)


def to_do_list_in_order(task_lists, **kwargs):

    for i, task in enumerate(task_lists, start=1):
        emoji = "⏳" if task["status"] == "pendente" else "✅"

        print(f"[{i}] Tarefa: {task['nome']}")
        print(f"    Prioridade: {task['prioridade']}")
        print(f"    Status: {task['status']} {emoji}")
        print(f"    Criado em: {task['horario']}")
        print("-" * 25)

def terminal_commands():
    print('1 - Adicionar tarefa')
    print('2 - listar tarefa')
    print('3 - Remover tarefa')
    print('4 - Marcar tarefa como concluída')
    print('5 - Sair')
    print('\n')

def add_task(tasks):
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
                    "status": "pendente",
                    "horario": get_current_time()

                })

                save_data(tasks)

                print('Tarefa adicionada com sucesso!')
            else:
                print('Prioridade desconhecida!')

        else:
            print('Resposta invalida.')

    except ValueError:
        print('Resposta invalida.')



def list_tasks(tasks):
    if not tasks:

        print('Nenhuma tarefa cadastrada na lista de tarefas.')


    else:
        print('Lista de tarefas:')
        to_do_list_by_priority(tasks)
        input('Aperte Enter para continuar...')


def remove_task(tasks):
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

            save_data(tasks)

        else:
            print('Índice inválido.')
    except ValueError:
        print('Digite apenas números.')


def task_completed(tasks):
    if not tasks:
        print('Nenhuma tarefa cadastrada.')
        return

    print("Tarefas (ordem de criação):")
    to_do_list_in_order(tasks)

    try:
        task_that_will_be_marked_as_completed = int(input('Qual é o número da tarefa que deseja marca como concluída: '))
        real_index = task_that_will_be_marked_as_completed - 1

        if 0 <= real_index < len(tasks):
            tasks[real_index]["status"] = "concluída"
            print('Tarefa concluida com sucesso.')

            save_data(tasks)
        else:
            print('Índice inválido.')

    except ValueError:
        print('Digite apenas números.')