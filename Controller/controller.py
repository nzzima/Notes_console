import Service.exceptions
from Service import basic_model
from View import modelview


class Controller(object):
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def start(self):
        self.view.show_start_print()
        self.view.show_start_commands()

    def create_notes_file(self):
        self.model.create_notes_file()

    def create_note(self, notes, title, message):
        self.model.create_note(notes, title, message)
        self.model.save_notes(notes)
        self.view.save_notes()

    def show_notes(self):
        notes = self.model.load_notes()
        try:
            self.view.show_notes(notes)
        except Service.exceptions.EmptyNotes as e:
            self.view.display_empty_notes(e)

    def show_note_with_current_id(self, note_id):
        notes = self.model.load_notes()
        try:
            self.view.show_note_with_current_id(notes, note_id)
        except Service.exceptions.NoteNotExist as e:
            self.view.display_not_exist_note(note_id, e)

    def edit_note(self, note_id, new_title, new_message):
        try:
            edit_notes = self.model.edit_note(note_id, new_title, new_message)
            self.view.display_editing_note(edit_notes, note_id)
            self.view.save_notes()
        except Service.exceptions.NoteNotExist as e:
            self.view.display_not_exist_note(note_id, e)

    def delete_note(self,note_id):
        try:
            edit_notes = self.model.delete_note(note_id)
            self.view.display_deleted_note(note_id)
        except Service.exceptions.NoteNotExist as e:
            self.view.display_not_exist_note(note_id, e)

    def invalid(self):
        self.view.display_invalid_command()


def main():
    c = Controller(basic_model.BasicModel(), modelview.View())
    c.create_notes_file()
    notes = []
    c.start()
    while True:
        user_command = input("Enter command:")

        if user_command == "add":
            user_enter_title = input("Enter note title: ")
            user_enter_message = input("Enter note message: ")
            c.create_note(notes, user_enter_title, user_enter_message)

        elif user_command == "edit":
            user_enter_id = input("Enter note id: ")
            user_enter_new_title = input("Enter new note title: ")
            user_enter_new_message = input("Enter new note message: ")
            c.edit_note(user_enter_id, user_enter_new_title, user_enter_new_message)

        elif user_command == "show":
            c.show_notes()

        elif user_command == "current":
            user_enter_id = input("Enter note id: ")
            c.show_note_with_current_id(user_enter_id)

        elif user_command == "delete":
            user_enter_id = input("Enter note id: ")
            c.delete_note(user_enter_id)

        elif user_command == "exit":
            break

        else:
            c.invalid()


if __name__ == '__main__':
    main()
