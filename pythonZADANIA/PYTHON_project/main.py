# PROJEKT KOŃCOWY
#
# Zadanie: Notatnik zadań
# Twoim zadaniem jest stworzenie prostego notatnika zadań w Pythonie, który będzie umożliwiał użytkownikowi dodawanie nowych zadań, oznaczanie ich jako wykonane i zapisywanie ich do pliku.
# Wymagane funkcje notatnika zadań:
# Dodawanie nowego zadania: Użytkownik powinien móc wprowadzić opis nowego zadania, a program powinien zapisać je w liście zadań.
# Wyświetlanie listy zadań: Użytkownik powinien mieć możliwość wyświetlenia listy wszystkich zadań w terminalu.
# Oznaczanie zadania jako wykonane: Użytkownik powinien móc oznaczyć zadanie jako wykonane, co wpłynie na jego status w liście zadań (zmienna typu bool - true/false).
# Zapisywanie do pliku: Po zakończeniu pracy z notatnikiem, lista zadań powinna zostać zapisana do pliku tekstowego, aby można było ją ponownie odczytać przy kolejnym uruchomieniu programu. (Np. jako plik tekstowy w każdym wierusz jest zadanie, godzina, stan zadania)
# Biblioteki, które można wykorzystać:
# datetime: Do dodawania daty i czasu wykonania zadania, albo "do kiedy" (wg. uznania)
# (opcjonalnie) os: Do obsługi bezpiecznej operacji na plikach, odczytywanie danych tylko jeśli plik istnieje.
# Wskazówki:
# Rozpocznij od stworzenia prostego menu dla użytkownika, które umożliwi dodawanie, wyświetlanie i oznaczanie zadań (te operacje będą funkcjami).
# Wykorzystaj pętlę while, aby umożliwić użytkownikowi wykonanie wielu operacji przed zamknięciem notatnika.
# Zadbaj o strukturę danych np. przechowuj listę zadań w formie słownika, gdzie kluczami będą numery indeksów, a wartościami będą opisy zadań.
# Po zakończeniu pracy z notatnikiem, zapisz listę zadań do pliku tekstowego za pomocą biblioteki os.

import datetime
import os


PATH = "pythonZADANIA/PYTHON_project/zadania.txt"


def save(tasks):
    with open(PATH, "w") as file:
        for idx, task in tasks.items():
            file.write(
                f'{idx};{task["name"]};{task["done"]};{task["description"]};{task["date"]}\n')


def add(tasks):
    name = input("Task name: ")
    description = input("Task description: ")
    date = input("Due date [YYYY-MM-DD]: ")
    tasks[len(tasks)] = {
        "name": name,
        "done": False,
        "description": description,
        "date": datetime.date.fromisoformat(date),
    }

    print("Task was added!")

    return tasks


def mark_as_done(tasks):
    idx = int(input("Task number: "))
    tasks[idx]["done"] = True

    print("Task was marked as done")

    return tasks


def list_tasks(tasks):
    for idx, task in tasks.items():
        mark = "√" if task["done"] else "X"
        print(f'{idx} \t[{mark}]\t{task["name"]}')
        print(f'due: {task["date"]}')
        print(task["description"])

    ui = input("\n[m] - mark task as done\n[b] - go back\n\n")
    if ui == "m":
        tasks = mark_as_done(tasks)

    return tasks


def read_backup():
    if os.path.exists(PATH):
        tasks = {}
        with open(PATH) as file:
            content = file.readlines()
        for line in content:
            line = line.strip().split(";")
            tasks[line[0]] = {
                "name": line[1],
                "done": line[2] == "True",
                "description": line[3],
                "date": datetime.date.fromisoformat(line[4]),
            }
    else:
        tasks = {
            0: {
                "name": "example",
                "done": False,
                "description": "test",
                "date": datetime.date.today(),
            }
        }
    return tasks


tasks = read_backup()
while True:
    ui = input("\n[l] - list all tasks\n[a] - add task\n[q] - quit\n\n")
    if ui == "l":
        tasks = list_tasks(tasks)
    if ui == "a":
        tasks = add(tasks)
    if ui == "q":
        save(tasks)
        break