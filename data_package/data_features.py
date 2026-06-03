import json

def save_data(tasks, completed_tasks_list):
    data = {
        'tasks': tasks,
        'completed_tasks_list': completed_tasks_list,
    }
    with open("data_package/tasks.json", "w") as arquivo:
        json.dump(data, arquivo, indent=4)



def load_data():
    try:
        with open("data_package/tasks.json", "r") as arquivo:
            data = json.load(arquivo)
        return data["tasks"], data["completed_tasks_list"]
    except FileNotFoundError:
        return [], []
