import math
import random

# 1. Написати програму для обробки одного рядка.
# def Oneline():
#     line = input("Введіть рядок: ")
#     Oneline = line.title()
#     print(f"Оброблений рядок: {Oneline}")
#
# Oneline()



# 2. Написати програму для обробку кількох рядків.
# def Sline():
#     number = int(input("Скільки рядків ви хочете ввести? "))
#     lines = []
#     for i in range(number):
#         line = input(f"Введіть рядок {i + 1}: ")
#         lines.append(line.title().strip())
#
#
#     print("Оброблені рядки:")
#     for line in lines:
#         print(line)
#
# Sline()


# 3. Користувач задає два рядка слів, розділених пробілами.
# Програма повинна видалити з рядків повтори слів.


# def Remline():
#      number = int(input("Скільки рядків ви хочете ввести? "))
#      lines = []
#
#      for i in range(number):
#          line = input(f"Введіть рядок {i + 1}: ")
#          words = set(line.split())
#          lines.append("".join(words))
#
#      print("Оброблені рядки:")
#      for line in lines:
#         print(line)
#
# Remline()

# 4. Користувач вводить чотири рядка символів (англійських літер і цифр).
# Програма повинна вивести рядок, сума цифр, які зустрічаються у ньому,
# найбільша.


# def MaxSumline():
#     lines = []
#     for i in range(4):
#         line = input(f"Введіть рядок {i + 1}: ")
#         lines.append(line)
#
#     maxSum = 0
#     maxline = ""
#
#     for line in lines:
#         digit_sum = sum(int(char) for char in line if char.isdigit())
#         if digit_sum > maxSum:
#             maxSum = digit_sum
#             maxline = line
#
#     print(f"Рядок з найбільшою сумою цифр: {maxline} (сума цифр: {maxSum})")
#
#
# MaxSumline()
