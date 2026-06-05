import json

def save_data(tasks):
    data = {
        'tasks': tasks,

    }
    with open("data_package/tasks.json", "w") as arquivo:
        json.dump(data, arquivo, indent=4)


def load_data():
    try:
        with open("data_package/tasks.json", "r") as arquivo:
            data = json.load(arquivo)
        return data["tasks"]

    except (FileNotFoundError, json.JSONDecodeError):
        save_data([])
        return []
