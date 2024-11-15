import csv
import json
import random
import os

# 1. Написати програму, яка зберігає дані у файл формату CSV (приклад 11.1).

# f = "workers.csv"
#
# data = [
#     ["Name", "Position", "Age"],
#     ["John Doe", "Developer", 28],
#     ["Anton Boken","Student", 18],
#     ["Jane Smith", "Designer", 34],
#     ["Mike Johnson", "Manager", 45],
#     ["Nazar Carter", "Financial Analyst", 25],
#     ["Nik Kinekan", "Marketing Manager", 34]
#
# ]
#
# with open(f, 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerows(data)
#
# print(f"Дані збережено у файл {f}")



# 2. Написати програму, яка зберігає дані у файл формату JSON (приклад 11.2).


# f = "workersss.json"
#
# info = {
#     "workers": [
#         {"name": "John Doe", "position": "Developer", "age": 28},
#         {"name": "Jane Smith", "position": "Designer", "age": 34},
#         {"name": "Mike Johnson", "position": "Manager", "age": 45},
#         {"name": "Nik Kinekan", "position": "Marketing Manager", "age": 34},
#         {"name": "Nazar Carter", "position": "Financial Analyst", "age": 25}
#     ]
# }
#
#
# with open(f, 'w') as jsonfile:
#     json.dump(info, jsonfile, indent=4)
#
# print(f"Дані збережено у файл {f}")


# Варіант 16
# 1. Координати точки на площині (х;у) являють собою випадкові числа у
# діапазоні [-20; 20]. Програма повинна підрахувати, скільки таких точок припаде
# на кожну з чвертей координатної площини, якщо всього таких точок 100.

# range_min, range_max = -20, 20
# num_points = 100
#
#
# first = 0
# second = 0
# third = 0
# fourth = 0
#
# # Генерація 100 випадкових точок та підрахунок для кожної чверті
# for _ in range(num_points):
#     x = random.randint(range_min, range_max)
#     y = random.randint(range_min, range_max)
#
#     if x > 0 and y > 0:
#         first += 1
#     elif x < 0 and y > 0:
#         second+= 1
#     elif x < 0 and y < 0:
#         third += 1
#     elif x > 0 and y < 0:
#         fourth += 1
#
#
# print(f"Кількість точок у першій чверті: {first}")
# print(f"Кількість точок у другій чверті: {second}")
# print(f"Кількість точок у третій чверті: {third}")
# print(f"Кількість точок у четвертій чверті: {fourth}")



# 2. Файл у форматі JSON містить дані про кількість днів, протягом яких
# співробіники фірми перебували на лікарняному. Програма повинна: 1)
# відсортувати ці дані у порядку спадання; 2) вивести прізвища співробітників,
# які не мали жодного лікарняного; 3) вивести прізвища співробітників, які
# перебували ан лікарняному понад 20 днів.


# f = "SickDays.json"
#
# print("Поточний каталог:", os.getcwd())
#
# try:
#     with open(f, "r") as file:
#         data = json.load(file)
# except FileNotFoundError:
#     print(f"Файл {f} не знайдено.")
#     data = {"workers": []}  # Додаємо пустий словник на випадок, якщо файл не буде знайдений
#
# # Сортування співробітників за кількістю лікарняних днів
# sorted_workers = sorted(data["workers"], key=lambda x: x["sick_days"], reverse=True)
#
# print("Список співробітників за кількістю днів на лікарняному (у порядку спадання):")
# for employee in sorted_workers:
#     print(f"{employee['name']}: {employee['sick_days']} днів")
#
# print("Співробітники без лікарняного:")
# no_sick_leave = [emp["name"] for emp in sorted_workers if emp["sick_days"] == 0]
# print(", ".join(no_sick_leave) if no_sick_leave else "Немає таких співробітників.")
#
# print("Співробітники з лікарняним понад 20 днів:")
# over_20_days = [emp["name"] for emp in sorted_workers if emp["sick_days"] > 20]
# print(", ".join(over_20_days) if over_20_days else "Немає таких співробітників.")

