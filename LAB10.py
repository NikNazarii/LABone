import os
import shutil
import re

# 1. Написати програму, яка використовує текстові файли для зберігання
# даних (приклад 10.1).

# f = "text1.txt"
#
# try:
#     with open(f, 'r') as file:
#         content = file.read()
#         print("Вміст файлу:")
#         print(content)
# except FileNotFoundError:
#     print(f"Файл {f} не знайдено.")


# 2. Написати програму, яка виконує операції з файлами (копіювання,
# перейменування, видалення) (приклад 10.2).


# src = 'trade.txt'
# backup = 'trade.bak'
# renamed = 'trade_backup.txt'
#
#
# if os.path.exists(src):
#     shutil.copy(src, backup)
#     print(f"Файл {src} скопійовано до {backup}.")
# else:
#     print(f"Файл {src} не знайдено для копіювання.")
#
#
# if os.path.exists(backup):
#     os.rename(backup, renamed)
#     print(f"Файл {backup} перейменовано на {renamed}.")
# else:
#     print(f"Файл {backup} не знайдено для перейменування.")
#
#
# if os.path.exists(renamed):
#     os.remove(renamed)
#     print(f"Файл {renamed} видалено.")
# else:
#     print(f"Файл {renamed} не знайдено для видалення.")

# 1. Текстовий файл містить фрагмент тексту на англійській мові. Програма
# повинна: 1) визначити кількість питальних, розповідних і окличних речень; 2)
# записати у список всі слова, які починаються з великої літери; 3) записати в
# інший список всі розділові знаки, які зустрічаються в тексті; 4) зберегти
# результати роботи в окремі текстові файли.

# f = 'text.txt'
#
# question = 0
# statement = 0
# exclamation= 0
# capitalized = []
# punctuation = []
#
# try:
#     with open(f, 'r') as file:
#         text = file.read()
#
#         # Підрахунок речень
#         question = len(re.findall(r'\?\s', text))
#         exclamation = len(re.findall(r'!\s', text))
#         statement = len(re.findall(r'\.\s', text))
#
#         capitalized = re.findall(r'\b[A-Z][a-z]*\b', text)
#
#         punctuation = re.findall(r'[.?!,;:]', text)
#
#     with open('sentence_count.txt', 'w') as f:
#         f.write(f"Питальних речень: {question}\n")
#         f.write(f"Окличних речень: {exclamation}\n")
#         f.write(f"Narrative sentences: {statement}\n")
#
#     with open('capitalized_words.txt', 'w') as f:
#         f.write('\n'.join(capitalized))
#
#     with open('punctuation_marks.txt', 'w') as f:
#         f.write(' '.join(punctuation))
#
#     print("Аналіз завершено Результати збережено у файлах")
# except FileNotFoundError:
#     print(f"Файл {f} не знайдено.")


# 2. Текстовий файл містить назви каталогів, записані кожен з нового рядка.
# Програма повинна створити каталоги з такими назвами у каталогу WORK.


# f = 'text.txt'
# work = 'WORK'
#
# if not os.path.exists(work):
#     os.mkdir(work)
#
# try:
#     with open(f, 'r') as file:
#         for line in file:
#             catalog = line.strip()
#             if catalog:
#                 catalog_path = os.path.join(work, catalog)
#                 if not os.path.exists(catalog_path):
#                     os.mkdir(catalog_path)
#                     print(f"Каталог {catalog} створено.")
#                 else:
#                     print(f"Каталог {catalog} вже існує.")
# except FileNotFoundError:
#     print(f"Файл {f} не знайдено.")

