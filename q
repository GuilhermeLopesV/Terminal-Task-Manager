[1mdiff --git a/data_package/data_features.py b/data_package/data_features.py[m
[1mindex 62a91c1..564806e 100644[m
[1m--- a/data_package/data_features.py[m
[1m+++ b/data_package/data_features.py[m
[36m@@ -1,19 +1,20 @@[m
 import json[m
 [m
[31m-def save_data(tasks, completed_tasks_list):[m
[32m+[m[32mdef save_data(tasks):[m
     data = {[m
         'tasks': tasks,[m
[31m-        'completed_tasks_list': completed_tasks_list,[m
[32m+[m
     }[m
     with open("data_package/tasks.json", "w") as arquivo:[m
         json.dump(data, arquivo, indent=4)[m
 [m
 [m
[31m-[m
 def load_data():[m
     try:[m
         with open("data_package/tasks.json", "r") as arquivo:[m
             data = json.load(arquivo)[m
[31m-        return data["tasks"], data["completed_tasks_list"][m
[31m-    except FileNotFoundError:[m
[31m-        return [], [][m
[32m+[m[32m        return data["tasks"][m
[32m+[m
[32m+[m[32m    except (FileNotFoundError, json.JSONDecodeError):[m
[32m+[m[32m        save_data([])[m
[32m+[m[32m        return [][m
[1mdiff --git a/data_package/tasks.json b/data_package/tasks.json[m
[1mindex 626199b..faf5cd4 100644[m
[1m--- a/data_package/tasks.json[m
[1m+++ b/data_package/tasks.json[m
[36m@@ -1,21 +1,16 @@[m
 {[m
     "tasks": [[m
         {[m
[31m-            "nome": "Futebol",[m
[31m-            "prioridade": "MEDIA",[m
[31m-            "horario": "30/04/2026 00:48:09"[m
[31m-        }[m
[31m-    ],[m
[31m-    "completed_tasks_list": [[m
[31m-        {[m
[31m-            "nome": "Estudar",[m
[32m+[m[32m            "nome": "Bom dia",[m
             "prioridade": "ALTA",[m
[31m-            "horario": "30/04/2026 00:55:19"[m
[32m+[m[32m            "status": "pendente",[m
[32m+[m[32m            "horario": "04/06/2026 20:01:34"[m
         },[m
         {[m
[31m-            "nome": "Lavar a lou\u00e7a",[m
[31m-            "prioridade": "ALTA",[m
[31m-            "horario": "30/04/2026 20:04:21"[m
[32m+[m[32m            "nome": "mkkk",[m
[32m+[m[32m            "prioridade": "BAIXA",[m
[32m+[m[32m            "status": "conclu\u00edda",[m
[32m+[m[32m            "horario": "04/06/2026 20:06:27"[m
         }[m
     ][m
 }[m
\ No newline at end of file[m
[1mdiff --git a/features_package/__pycache__/features.cpython-311.pyc b/features_package/__pycache__/features.cpython-311.pyc[m
[1mindex cd69c83..26acc65 100644[m
Binary files a/features_package/__pycache__/features.cpython-311.pyc and b/features_package/__pycache__/features.cpython-311.pyc differ
[1mdiff --git a/features_package/features.py b/features_package/features.py[m
[1mindex 72bcc53..2cd4ec0 100644[m
[1m--- a/features_package/features.py[m
[1m+++ b/features_package/features.py[m
[36m@@ -1,6 +1,6 @@[m
 import time[m
 from data_package.data_features import save_data[m
[31m-from features_package.utils import bar_spacing[m
[32m+[m
 [m
 def get_current_time():[m
     return time.strftime('%d/%m/%Y %H:%M:%S')[m
[36m@@ -12,41 +12,50 @@[m [morder_of_priority = {[m
     "BAIXA": 3[m
 }[m
 [m
[31m-def to_do_list_by_priority(task_lists, **kwargs):[m
[31m-    status = kwargs.get("status", "")[m
[32m+[m[32morder_of_status = {[m
[32m+[m[32m    "pendente": 1,[m
[32m+[m[32m    "concluída": 2[m
[32m+[m[32m}[m
 [m
[32m+[m[32mdef to_do_list_by_priority(task_lists):[m
     ordered_tasks = sorted([m
         task_lists,[m
[31m-        key=lambda task: order_of_priority[task["prioridade"]][m
[32m+[m[32m        key=lambda task: ([m
[32m+[m[32m            order_of_status[task["status"]],[m
[32m+[m[32m            order_of_priority[task["prioridade"]][m
[32m+[m[32m        )[m
     )[m
 [m
     for i, task in enumerate(ordered_tasks, start=1):[m
[31m-        print(f"[{i}] {task['nome']}")[m
[31m-        print(f"    Prioridade: {task['prioridade']} {status}")[m
[32m+[m[32m        emoji = "⏳" if task["status"] == "pendente" else "✅"[m
[32m+[m
[32m+[m[32m        print(f"[{i}] Tarefa: {task['nome']}")[m
[32m+[m[32m        print(f"    Prioridade: {task['prioridade']}")[m
[32m+[m[32m        print(f"    Status: {task['status']} {emoji}")[m
         print(f"    Criado em: {task['horario']}")[m
         print("-" * 25)[m
 [m
 [m
 def to_do_list_in_order(task_lists, **kwargs):[m
[31m-    status = kwargs.get("status", "")[m
 [m
     for i, task in enumerate(task_lists, start=1):[m
[31m-        print(f"[{i}] {task['nome']}")[m
[31m-        print(f"    Prioridade: {task['prioridade']} {status}")[m
[32m+[m[32m        emoji = "⏳" if task["status"] == "pendente" else "✅"[m
[32m+[m
[32m+[m[32m        print(f"[{i}] Tarefa: {task['nome']}")[m
[32m+[m[32m        print(f"    Prioridade: {task['prioridade']}")[m
[32m+[m[32m        print(f"    Status: {task['status']} {emoji}")[m
         print(f"    Criado em: {task['horario']}")[m
         print("-" * 25)[m
 [m
[31m-[m
 def terminal_commands():[m
     print('1 - Adicionar tarefa')[m
     print('2 - listar tarefa')[m
     print('3 - Remover tarefa')[m
     print('4 - Marcar tarefa como concluída')[m
[31m-    print('5 - Remover tarefa marcada como concluída ')[m
[31m-    print('6 - Sair')[m
[32m+[m[32m    print('5 - Sair')[m
     print('\n')[m
 [m
[31m-def add_task(tasks, completed_tasks_list):[m
[32m+[m[32mdef add_task(tasks):[m
     try:[m
         task = input('Qual tarefa deseja adicionar: ').strip()[m
 [m
[36m@@ -62,11 +71,12 @@[m [mdef add_task(tasks, completed_tasks_list):[m
                 tasks.append({[m
                     "nome": task,[m
                     "prioridade": task_priority,[m
[32m+[m[32m                    "status": "pendente",[m
                     "horario": get_current_time()[m
 [m
                 })[m
 [m
[31m-                save_data(tasks, completed_tasks_list)[m
[32m+[m[32m                save_data(tasks)[m
 [m
                 print('Tarefa adicionada com sucesso!')[m
             else:[m
[36m@@ -80,26 +90,19 @@[m [mdef add_task(tasks, completed_tasks_list):[m
 [m
 [m
 [m
[31m-def list_tasks(tasks, completed_tasks_list):[m
[32m+[m[32mdef list_tasks(tasks):[m
     if not tasks:[m
 [m
         print('Nenhuma tarefa cadastrada na lista de tarefas.')[m
[31m-        if completed_tasks_list:[m
[31m-             bar_spacing()[m
[31m-    else:[m
[31m-        to_do_list_by_priority(tasks)[m
 [m
[31m-    if not completed_tasks_list:[m
[31m-        bar_spacing()[m
[31m-        print('Nenhuma tarefa concluída')[m
[31m-    else:[m
[31m-        print('Suas Tarefas concluídas')[m
[31m-        to_do_list_by_priority(completed_tasks_list, status="✅")[m
 [m
[32m+[m[32m    else:[m
[32m+[m[32m        print('Lista de tarefas:')[m
[32m+[m[32m        to_do_list_by_priority(tasks)[m
         input('Aperte Enter para continuar...')[m
 [m
 [m
[31m-def remove_task(tasks, completed_tasks_list):[m
[32m+[m[32mdef remove_task(tasks):[m
     if not tasks:[m
         print('Nenhuma tarefa cadastrada.')[m
         return[m
[36m@@ -115,7 +118,7 @@[m [mdef remove_task(tasks, completed_tasks_list):[m
             removed = tasks.pop(real_index)[m
             print(f'Tarefa "{removed["nome"]}"| Prioridade: {removed["prioridade"]} removida com sucesso. ❌')[m
 [m
[31m-            save_data(tasks, completed_tasks_list)[m
[32m+[m[32m            save_data(tasks)[m
 [m
         else:[m
             print('Índice inválido.')[m
[36m@@ -123,7 +126,7 @@[m [mdef remove_task(tasks, completed_tasks_list):[m
         print('Digite apenas números.')[m
 [m
 [m
[31m-def task_completed(tasks, completed_tasks_list):[m
[32m+[m[32mdef task_completed(tasks):[m
     if not tasks:[m
         print('Nenhuma tarefa cadastrada.')[m
         return[m
[36m@@ -136,37 +139,12 @@[m [mdef task_completed(tasks, completed_tasks_list):[m
         real_index = task_that_will_be_marked_as_completed - 1[m
 [m
         if 0 <= real_index < len(tasks):[m
[31m-            completed_tasks_list.append(tasks[real_index])[m
[31m-            tasks.pop(real_index)[m
[32m+[m[32m            tasks[real_index]["status"] = "concluída"[m
             print('Tarefa concluida com sucesso.')[m
 [m
[31m-            save_data(tasks, completed_tasks_list)[m
[32m+[m[32m            save_data(tasks)[m
         else:[m
             print('Índice inválido.')[m
 [m
[31m-    except ValueError:[m
[31m-        print('Digite apenas números.')[m
[31m-[m
[31m-[m
[31m-def remove_completed_task(tasks, completed_tasks_list):[m
[31m-    if not completed_tasks_list:[m
[31m-        print('Nenhuma tarefa cadastrada.')[m
[31m-        return[m
[31m-[m
[31m-    print("Tarefas (ordem de criação):")[m
[31m-    to_do_list_in_order(completed_tasks_list)[m
[31m-[m
[31m-    try:[m
[31m-        remove = int(input('Qual é o número da tarefa que deseja remover: '))[m
[31m-        real_index = remove - 1[m
[31m-[m
[31m-        if 0 <= real_index < len(completed_tasks_list):[m
[31m-            removed = completed_tasks_list.pop(real_index)[m
[31m-            print(f'Tarefa "{removed["nome"]}"| Prioridade: {removed["prioridade"]} removida com sucesso. ❌')[m
[31m-[m
[31m-            save_data(tasks, completed_tasks_list)[m
[31m-[m
[31m-        else:[m
[31m-            print('Índice inválido.')[m
     except ValueError:[m
         print('Digite apenas números.')[m
\ No newline at end of file[m
[1mdiff --git a/main.py b/main.py[m
[1mindex d035d34..3b9b9f3 100644[m
[1m--- a/main.py[m
[1m+++ b/main.py[m
[36m@@ -4,16 +4,15 @@[m [mfrom features_package.features import ([m
     remove_task,[m
     task_completed,[m
     terminal_commands,[m
[31m-    remove_completed_task,[m
 )[m
 [m
 [m
 from data_package.data_features import load_data[m
 [m
 [m
[31m-def mini_trello():[m
[32m+[m[32mdef terminal_task_manager():[m
 [m
[31m-    tasks, completed_tasks_list = load_data()[m
[32m+[m[32m    tasks = load_data()[m
 [m
     while True:[m
         terminal_commands()[m
[36m@@ -21,16 +20,14 @@[m [mdef mini_trello():[m
         command = input('Digite um comando: ')[m
 [m
         if command == '1':[m
[31m-            add_task(tasks, completed_tasks_list)[m
[32m+[m[32m            add_task(tasks)[m
         elif command == '2':[m
[31m-            list_tasks(tasks, completed_tasks_list)[m
[32m+[m[32m            list_tasks(tasks)[m
         elif command == '3':[m
[31m-            remove_task(tasks, completed_tasks_list)[m
[32m+[m[32m            remove_task(tasks)[m
         elif command == '4':[m
[31m-            task_completed(tasks, completed_tasks_list)[m
[32m+[m[32m            task_completed(tasks)[m
         elif command == '5':[m
[31m-           remove_completed_task(tasks, completed_tasks_list)[m
[31m-        elif command == '6':[m
             print('Encerrando o Programa')[m
             break[m
         else:[m
[36m@@ -38,4 +35,5 @@[m [mdef mini_trello():[m
 [m
         print('\n')[m
 [m
[31m-mini_trello()[m
\ No newline at end of file[m
[32m+[m
[32m+[m[32mterminal_task_manager()[m
\ No newline at end of file[m
