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

# активация приложения Заметки
if __name__ == "__main__":

    app = Notes()
    app.load_notes()

    while True:
        print("\nВведите команду:")
        print("1. Создать заметку")
        print("2. Читать список заметок")
        print("3. Редактировать заметку")
        print("4. Выйти")

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
            break
        
        else:
            print("Такой команды нет. Попробуйте снова")