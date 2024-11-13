from tkinter import *
from tkinter import ttk
from translate import Translator

# Инициализация основного окна
root = Tk()
root.title('Переводчик')
root.geometry('750x450')
root.resizable(width=False, height=False)

# Переменная для выбора направления перевода
translation_direction = IntVar(value=0)  # Установлено начальное значение по умолчанию

# Функция перевода текста
def translate_text():
    try:
        # Определение направления перевода
        if translation_direction.get() == 0:
            translator = Translator(from_lang='English', to_lang='Russian')
        elif translation_direction.get() == 1:
            translator = Translator(from_lang='Russian', to_lang='English')

        # Получение текста из входного поля и выполнение перевода
        input_text = input_box.get(1.0, END).strip()
        if not input_text:
            output_box.delete(1.0, END)
            output_box.insert(1.0, "Введите текст для перевода.")
            return

        translated_text = translator.translate(input_text)

        # Вывод переведенного текста в выходное поле
        output_box.delete(1.0, END)
        output_box.insert(1.0, translated_text)
    except Exception as e:
        output_box.delete(1.0, END)
        output_box.insert(1.0, f"Ошибка перевода: {e}")

# Создание виджетов интерфейса
input_label = Label(root, text="Введите текст для перевода:", font='Arial 12')
input_box = Text(root, height=8, width=80, font='Arial 13')

output_label = Label(root, text="Переведенный текст:", font='Arial 12')
output_box = Text(root, height=8, width=80, font='Arial 13')

translate_button = Button(root, text='Перевести', command=translate_text, font='Arial 12 bold', bg='#4CAF50', fg='white')
rBtn_to_russian = Radiobutton(root, text='Переводить на русский', variable=translation_direction, value=0, font='Arial 11')
rBtn_to_english = Radiobutton(root, text='Переводить на английский', variable=translation_direction, value=1, font='Arial 11')

# Размещение виджетов в окне
input_label.pack(pady=(10, 0))
input_box.pack(pady=(0, 10))
rBtn_to_russian.pack(side=LEFT, padx=(50, 10))
rBtn_to_english.pack(side=LEFT, padx=(10, 50))
translate_button.pack(pady=10)
output_label.pack(pady=(10, 0))
output_box.pack(pady=(0, 10))