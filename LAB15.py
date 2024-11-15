
'''Варіант 16
1. Текстовий файл містить прізвища співробітників і заробітну плату за
кожен з місяців (для кожного робітника дані записуються в рядок). Розробити
програму, яка побудує гістограму, на якій буде відображена середня заробітна
плата кожного робітника. Початкові параметри вікна: ширина – 500, висота –
380, колір тла – коричневий. Використати менеджер геометрії pack().'''

# import tkinter as tk
# from tkinter import filedialog, messagebox
# import matplotlib.pyplot as plt
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#
# def create_file():
#     def save_data():
#         try:
#             with open('employee_salaries.txt', 'w', encoding='utf-8') as file:
#                 file.write(text_box.get("1.0", tk.END).strip())
#             messagebox.showinfo("Успіх", "Файл збережено як 'employee_salaries.txt'")
#             input_window.destroy()
#         except Exception as e:
#             messagebox.showerror("Помилка", f"Помилка збереження файлу: {e}")
#
#     input_window = tk.Toplevel(window)
#     input_window.title("Введіть статистику")
#     input_window.geometry("400x300")
#     tk.Label(input_window, text="Введіть прізвища та зарплати за місяці:\nПриклад: Іванов 10000").pack(pady=5)
#     text_box = tk.Text(input_window, width=40, height=10)
#     text_box.pack(pady=10)
#     tk.Button(input_window, text="Зберегти", command=save_data).pack()
#
# def calculate_average_salary():
#     file_path = filedialog.askopenfilename(title="Виберіть файл із зарплатами", filetypes=(("Text Files", "*.txt"),))
#     if not file_path:
#         return
#     try:
#         with open(file_path, 'r', encoding='utf-8') as file:
#             data = [line.strip().split() for line in file if line.strip()]
#
#         names = [line[0] for line in data]
#         avg_salaries = [sum(map(float, line[1:])) / len(line[1:]) for line in data]
#         plot_histogram(names, avg_salaries)
#     except Exception as e:
#         messagebox.showerror("Помилка", f"Помилка обробки файлу: {e}")
#
# def plot_histogram(names, avg_salaries):
#     fig, ax = plt.subplots(figsize=(6, 4))
#     ax.bar(names, avg_salaries, color='green')
#     ax.set_xlabel('Співробітники')
#     ax.set_ylabel('Середня зарплата')
#     ax.set_title('Середня зарплата кожного співробітника')
#     FigureCanvasTkAgg(fig, master=window).get_tk_widget().pack()
#
# window = tk.Tk()
# window.title("Гістограма зарплати")
# window.geometry("500x380")
# window.configure(bg="blue")
#
# tk.Button(window, text="Створити файл", command=create_file).pack(pady=10)
# tk.Button(window, text="Завантажити файл", command=calculate_average_salary).pack(pady=10)
#
# window.mainloop()


'''2. Розробити екранний додаток, який зчитуватиме текст з веб-сторінки,
введеної користувачем, і виводитиме його у поле Text. Вікно програми повинно
містити віджети: Label, Entry, Text, Button. '''

# import tkinter as tk
# from tkinter import messagebox
# import requests
# from bs4 import BeautifulSoup
#
#
# def fetch_text():
#     url = url_entry.get()
#     if not url:
#         messagebox.showwarning("Увага", "Будь ласка, введіть URL.")
#         return
#
#     try:
#         response = requests.get(url)
#         response.raise_for_status()
#         soup = BeautifulSoup(response.text, 'html.parser')
#         page_text = soup.get_text()
#
#         text_box.delete("1.0", tk.END)
#         text_box.insert(tk.END, page_text)
#     except requests.exceptions.RequestException as e:
#         messagebox.showerror("Помилка", f"Не вдалося завантажити сторінку: {e}")
#
#
# window = tk.Tk()
# window.title("Зчитування тексту з веб-сторінки")
# window.geometry("600x400")
#
#
# tk.Label(window, text="Введіть URL веб-сторінки:").pack(pady=5)
# url_entry = tk.Entry(window, width=50)
# url_entry.pack(pady=5)
#
# fetch_button = tk.Button(window, text="Отримати текст", command=fetch_text)
# fetch_button.pack(pady=5)
#
# text_box = tk.Text(window, wrap='word', height=15, width=70)
# text_box.pack(pady=10)
#
# window.mainloop()
