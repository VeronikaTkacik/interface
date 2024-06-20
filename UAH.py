import tkinter as tk
from tkinter import ttk
import requests

# Введіть свій API ключ тут
API_KEY = '91548e41c1d0a0326fb29017'
BASE_URL = 'https://v6.exchangerate-api.com/v6'

def get_exchange_rate(api_key, base_currency, target_currency):
    url = f"{BASE_URL}/{api_key}/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()
    if data['result'] == 'success':
        return data['conversion_rates'][target_currency]
    else:
        raise Exception('API request failed with message: ' + data['error-type'])

def convert():
    try:
        amount = float(entry_amount.get())
        from_currency = combo_from_currency.get()
        to_currency = combo_to_currency.get()
        rate = get_exchange_rate(API_KEY, from_currency, to_currency)
        result = amount * rate
        label_result.config(text=f"Виходить: {round(result, 2)} {to_currency}")
    except Exception as e:
        label_result.config(text=f"Помилка: {str(e)}")

# Створення головного вікна
root = tk.Tk()
root.title("Конвертер Валют")

# Задаємо стиль для віджетів
style = ttk.Style()
style.configure('TLabel', font=('Arial', 12))
style.configure('TButton', font=('Arial', 12))
style.configure('TCombobox', font=('Arial', 12))
style.configure('TEntry', font=('Arial', 12))

# Створення і розміщення віджетів
label_amount = ttk.Label(root, text="Введіть суму:")
label_amount.grid(column=0, row=0, padx=10, pady=10)

entry_amount = ttk.Entry(root)
entry_amount.grid(column=1, row=0, padx=10, pady=10)

label_from_currency = ttk.Label(root, text="З валюти:")
label_from_currency.grid(column=0, row=1, padx=10, pady=10)

# Список валют, включаючи гривню (UAH)
currencies = ['USD', 'EUR', 'GBP', 'UAH', 'JPY', 'CAD']

combo_from_currency = ttk.Combobox(root, values=currencies, state="readonly")
combo_from_currency.grid(column=1, row=1, padx=10, pady=10)
combo_from_currency.set("USD")  # Встановлення значення за замовчуванням

label_to_currency = ttk.Label(root, text="До валюти:")
label_to_currency.grid(column=0, row=2, padx=10, pady=10)

combo_to_currency = ttk.Combobox(root, values=currencies, state="readonly")
combo_to_currency.grid(column=1, row=2, padx=10, pady=10)
combo_to_currency.set("UAH")  # Встановлення значення за замовчуванням

button_convert = ttk.Button(root, text="Конвертувати", command=convert)
button_convert.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

label_result = ttk.Label(root, text="Виходить:")
label_result.grid(column=0, row=4, columnspan=2, padx=10, pady=10)

# Запуск головного циклу
root.mainloop()

