''' 1. Написати програму для зображення графіка функції відповідно варіанта,
зберегти його у файл відповідно варіанта (приклад 16.1).'''

# import numpy as np
# import matplotlib.pyplot as plt
#
#
# x_start = float(input("Введіть початкове значення x: "))
# x_end = float(input("Введіть кінцеве значення x: "))
# n = int(input("Введіть кількість точок: "))
#
# y_s = int(input("Введіть початкове значення y: "))
# y_m = int(input("Введіть середнє значення y: "))
# y_e = int(input("Введіть кінцеве значення y: "))
#
#
# x = np.linspace(x_start, x_end, n)
#
# y = y_s * x**y_m - y_e
#
# plt.plot(x, y, 'r-', label=f'y={y_s}x^{y_m}-{y_e}')
#
# plt.xlabel('x')
# plt.ylabel('y')
# plt.grid(True)
# plt.title('Графік функції')
# plt.legend()
#
# plt.savefig('image12.png', dpi=400)
#
# plt.show()


''' 2. Написати програму для зображення гістограми (приклад 16.2).'''

# import numpy as np
# import matplotlib.pyplot as plt
#
# n = int(input("Введіть кількість категорій: "))
#
# x = []
# y = []
# print("Введіть значення для кожної категорії:")
#
# for i in range(n):
#     x_val = input(f"Назва категорії {i + 1}: ")
#     y_val = float(input(f"Значення для категорії '{x_val}': "))
#     x.append(x_val)
#     y.append(y_val)
#
# x = np.array(x)
# y = np.array(y)
#
# plt.bar(x, y, color='darkgreen')
#
# plt.xlabel('Категорії')
# plt.ylabel('Значення')
# plt.title('Приклад гістограми')
# plt.grid(axis='y', linestyle='--', alpha=0.7)
#
# plt.savefig('histogram_example.png', dpi=400)
#
# plt.show()


'''Варіант 16'''
''' 1. Зобразити графік функції 𝑦 = 1/𝜋 ∙ sin(0,3𝑥), 𝑥 ∈ [−8; 8], тип лінії –
пунктирна, колір лінії – чорний. Зберегти графік у файл function.jpg.'''


# import numpy as np
# import matplotlib.pyplot as plt
#
# x = np.linspace(-8, 8, 400)
# y = (1 / np.pi) * np.sin(0.3 * x)
#
# plt.plot(x, y, 'k--', label=r'$y = \frac{1}{\pi} \cdot \sin(0.3x)$', color='green')
#
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Графік функції $y = \\frac{1}{\\pi} \cdot \sin(0.3x)$')
# plt.legend()
# plt.grid(True)
#
# plt.savefig('function.jpg', dpi=400)
#
# plt.show()


'''2. Написати програму, яка виведе на екран гістограму кількостей
гіперпосилань на 6-8 сайтах (за вибором). Кількість гіперпосилань повинна
підраховуватися програмою. '''

# import requests
# from bs4 import BeautifulSoup
# import matplotlib.pyplot as plt
#
# urls = [
#     'https://www.wikipedia.org',
#     'https://www.python.org',
#     'https://www.github.com',
#     'https://rozetka.com.ua',
#     'https://prom.ua',
#     'https://www.olx.ua'
# ]
#
# link_counts = []
# for url in urls:
#     try:
#         response = requests.get(url)
#         response.raise_for_status()
#
#         soup = BeautifulSoup(response.text, 'html.parser')
#
#         links = soup.find_all('a')
#         link_counts.append(len(links))
#         print(f"{url}: {len(links)} гіперпосилань")
#
#     except requests.RequestException as e:
#         print(f"Не вдалося завантажити {url}: {e}")
#         link_counts.append(0)
#
#
# plt.figure(figsize=(10, 6))
# plt.bar(urls, link_counts, color='skyblue')
# plt.xlabel('Сайти')
# plt.ylabel('Кількість гіперпосилань')
# plt.title('Кількість гіперпосилань на веб-сайтах')
# plt.xticks(rotation=45, ha="right")
# plt.tight_layout()
#
# plt.savefig('hyperlinks_histogram.png', dpi=300)
#
# plt.show()
