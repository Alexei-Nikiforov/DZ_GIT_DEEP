# Приложение заметки (Python)

# Информация о проекте
# Необходимо написать проект, содержащий функционал работы с заметками.
# Программа должна уметь создавать заметку, сохранять её, читать список заметок, редактировать заметку, удалять заметку.

# Задание
# Реализовать консольное приложение заметки, с сохранением, чтением, добавлением, редактированием и удалением заметок. Заметка должна
# содержать идентификатор, заголовок, тело заметки и дату/время создания или последнего изменения заметки. Сохранение заметок необходимо сделать
# в формате json или csv формат (разделение полей рекомендуется делать через точку с запятой). Реализацию пользовательского интерфейса студент может
# делать как ему удобнее, можно делать как параметры запуска программы (команда, данные), можно делать как запрос команды с консоли и
# последующим вводом данных, как-то ещё, на усмотрение студента. При чтении списка заметок реализовать фильтрацию по дате.

import os
import json
from datetime import datetime

class Notes:

    # инициализация класса Notes
    def __init__(self):
        self.notes = []

    # загрузка (чтение) данных из файла notes.json
    def load_notes(self):
        if os.path.exists("notes.json"):
            with open("notes.json", "r", encoding='utf-8') as file:
                self.notes = json.load(file)

    # сохранение данных в файл notes.json
    def save_notes(self):
        with open("notes.json", "w", encoding='utf-8') as file:
            json.dump(self.notes, file)

    # создание данных заметки с сохранением в файл
    def create_note(self, title, content):
        note = {"title": title, "content": content, "date": str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))}
        self.notes.append(note)
        self.save_notes()
        print(f"Заметка '{title}' успешно создана.")

    # распечатывание списка заметок
    def print_list_notes(self):
        if not self.notes:
            print("У Вас нет заметок.")
        else:
            print("Список Ваших заметок:")
            for idx, note in enumerate(self.notes):
                print(f"{idx + 1}. {note['title']}. {note['content']}. {note['date']}")

    # редактирование заметок
    def edit_note(self, index, new_title, new_content):
        if 0 <= index < len(self.notes):
            self.notes[index]["title"] = new_title
            self.notes[index]["content"] = new_content
            self.save_notes()
            print(f"Заметка успешно отредактирована.")
        else:
            print(f"Не удалось выполнить редактирование заметки. Попробуйте снова.")

    # удаление заметок
    def delete_note(self, index):
        if 0 <= index < len(self.notes):
            deleted_note = self.notes.pop(index)
            self.save_notes()
            print(f"Заметка '{deleted_note['title']}' успешно удалена.")
        else:
            print(f"Не удалось выполнить удаление заметки. Попробуйте снова.")

# активация приложения Заметки
if __name__ == "__main__":

    app = Notes()
    app.load_notes()

    while True:
        print("\nВведите команду:")
        print("1. Создать заметку")
        print("2. Читать список заметок")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выйти")

        choice = input("Введите номер действия: ")
        
        if choice == "1":
            title = input("Введите заголовок заметки: ")
            content = input("Введите текст заметки: ")
            app.create_note(title, content)

        elif choice == "2":
            app.print_list_notes()
        
        elif choice == "3":
            try:
                index = int(input("Введите номер заметки для ее редактирования: ")) - 1
                if 0 <= index < len(app.notes):
                    new_title = input("Введите новый заголовок: ")
                    new_content = input("Введите новый текст: ")
                    app.edit_note(index, new_title, new_content)
                else:
                    print("Такого номера заметки нет. Попробуйте снова")
            except Exception:
                print('Не удалось отредактировать заметку. Попробуйте снова')
        
        elif choice == "4":
            try:
                index = int(input("Введите номер заметки для удаления: ")) - 1
                if 0 <= index < len(app.notes):
                    app.delete_note(index)
                else:
                    print("Такого номера заметки нет. Попробуйте снова")
            except Exception:
                print('Не удалось удалить заметку. Попробуйте снова')
        
        elif choice == "5":
            break
        
        else:
            print("Такой команды нет. Попробуйте снова")