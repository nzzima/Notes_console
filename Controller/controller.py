from Model.basicmodel import BasicModel
from View.modelview import View


def main():
    notes = BasicModel.create_notes_file()

    while True:
        View.show_start_print()
        View.show_start_commands()
        command = input("Enter command: ")

        if command == "add":
            title = input("Введите заголовок заметки: ")
            message = input("Введите текст заметки: ")
            notes = BasicModel.create_note(notes, title, message)
            BasicModel.save_notes(notes)
            print("Заметка успешно сохранена.")

        elif command == "read":
            for note in notes:
                print(f"ID: {note['id']}, Заголовок: {note['title']}, Время создания: {note['timestamp']}")

        elif command == "edit":
            note_id = int(input("Введите ID заметки для редактирования: "))
            new_title = input("Введите новый заголовок заметки: ")
            new_message = input("Введите новый текст заметки: ")
            notes = BasicModel.edit_note(notes, note_id, new_title, new_message)
            BasicModel.save_notes(notes)
            print("Заметка успешно отредактирована.")

        elif command == "delete":
            note_id = int(input("Введите ID заметки для удаления: "))
            notes = BasicModel.delete_note(notes, note_id)
            BasicModel.save_notes(notes)
            print("Заметка успешно удалена.")

        elif command == "show":
            note_id = int(input("Введите ID заметки для просмотра: "))
            BasicModel.show_note(notes, note_id)

        elif command == "exit":
            break

        else:
            print("Некорректная команда. Попробуйте снова.")


if __name__ == "__main__":
    main()