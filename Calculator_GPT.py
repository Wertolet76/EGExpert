from tkinter import *
from tkinter import ttk

def func(e, x):
    if x == '=':
        try:
            # Получаем введенное выражение и удаляем пробелы и символы новой строки
            expression = txt.get(1.0, END).strip()
            # Выполняем вычисление
            result = eval(expression)
            # Очищаем текстовое поле и показываем результат
            txt.delete(1.0, END)
            txt.insert(1.0, str(result))
        except Exception:
            txt.delete(1.0, END)
            txt.insert(1.0, "Ошибка")  # Сообщение об ошибке
    elif x == 'C':
        txt.delete(1.0, END)  # Очищаем текстовое поле
    else:
        # Добавляем новый символ в конец текста
        txt.insert(END, x)

root = Tk()
root.title('Калькулятор')
root.geometry('300x400')
root.resizable(False, False)

# Фреймы для упорядочивания виджетов
frame1 = Frame(master=root)
frame2 = Frame(master=root)
frame1.pack(pady=10)
frame2.pack()

# Поле для отображения ввода и результата
txt = Text(master=frame1, width=24, height=2, bg='white', font=("Arial", 16))
txt.pack(pady=5)

# Шаблон для кнопок
pattern = [
    (0, 0, '1'), (0, 1, '2'), (0, 2, '3'), (0, 3, '+'),
    (1, 0, '4'), (1, 1, '5'), (1, 2, '6'), (1, 3, '-'),
    (2, 0, '7'), (2, 1, '8'), (2, 2, '9'), (2, 3, '*'),
    (3, 0, '.'), (3, 1, '0'), (3, 2, '='), (3, 3, '/')
]

# Создаем кнопки для калькулятора
for r, c, value in pattern:
    button = ttk.Button(master=frame2, text=value, width=7, command=lambda x=value: func(None, x))
    button.grid(row=r, column=c, padx=5, pady=5)

# Кнопка очистки (C) вне числового ряда
clear_button = ttk.Button(master=frame1, text='C', width=24, command=lambda: txt.delete("1.0", END))
clear_button.pack(pady=5)

root.mainloop()