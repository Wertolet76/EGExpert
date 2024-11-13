from tkinter import *
from tkinter import ttk

def func(e, x):
    if x == '=':
        tmp = '=' + str(eval(txt.get(1.0, END)))
        txt.insert('end-1c', tmp)
    elif x == 'C':
        txt.delete(1.0, END)
    # Вставляем новый символ в конец текста
    else:
        txt.insert('end-1c', x)

root = Tk()
root.title('Калькулятор')
root.geometry('300x300+1000+100')
root.resizable(False, False)

# Создаем фреймы
frame1 = Frame(master=root)
frame2 = Frame(master=root)
frame3 = Frame(master=root)
frame1.pack()
frame2.pack()
frame3.pack()

# Текстовое поле для отображения ввода и результата
txt = Text(master=frame1, width=30, height=3, bg='white')
txt.pack(pady=5)

# Определяем шаблон для кнопок калькулятора
pattern = [
    (0, 0, '1'), (0, 1, '2'), (0, 2, '3'), (0, 3, '+'),
    (1, 0, '4'), (1, 1, '5'), (1, 2, '6'), (1, 3, '-'),
    (2, 0, '7'), (2, 1, '8'), (2, 2, '9'), (2, 3, '*'),
    (3, 0, '.'), (3, 1, '0'), (3, 2, '='), (3, 3, '/')
]

# Создаем кнопки на основе шаблона
buttons = []
for i, (r, c, value) in enumerate(pattern):
    button = ttk.Button(master=frame2, text=value, width=10)
    button.grid(row=r, column=c)
    button.bind('<Button-1>', lambda e, x=value: func(e, x))
    buttons.append(button)

# Кнопка очистки
clear_button = ttk.Button(master=frame3, text='C', command=lambda: txt.delete("1.0", END))
clear_button.pack(fill=X)

root.mainloop()