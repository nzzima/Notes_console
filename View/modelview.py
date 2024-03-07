import Service.exceptions


class View(object):

    @staticmethod
    def show_start_print():
        print("==================================================================")
        print("================ Welcome to NOTES CONSOLE PROGRAM ================")
        print("==================================================================")

    @staticmethod
    def show_start_commands():
        print("Enable commands: \nadd    =  Создать заметку\n"
                                "edit   =  Редактировать заметку\n"
                                "delete =  Удалить заметку\n"
                                "show   =  Показать список заметок\n"
                                "current = Показать конкретную заметку\n"
                                "exit   =  Завершить программу\n")

    @staticmethod
    def show_note_with_current_id(notes, id):
        print("==================================================================")
        for note in notes:
            if note["id"] == int(id):
                print(
                    f"ID: {note['id']}\nTitle: {note['title']}\nMessage: {note['message']}\nCreated time: {note['timestamp']};")
                break
        print("==================================================================")

    @staticmethod
    def show_notes(notes):
        print("==================================================================")
        for note in notes:
            print(
                f"ID: {note['id']}\nTitle: {note['title']}\nMessage: {note['message']}\nCreated time: {note['timestamp']};")
            print("------------------------------------------------------------------")
        print("==================================================================")



    @staticmethod
    def load_notes():
        print("==================================================================")
        print("Notes was loaded from file notes.json !")
        print("==================================================================")

    @staticmethod
    def save_notes():
        print("==================================================================")
        print("Notes was saved to file notes.json !")
        print("==================================================================")

    @staticmethod
    def display_editing_note(notes, id):
        print("==================================================================")
        print("Editing note with new title and message: ")
        for note in notes:
            if note["id"] == int(id):
                print(
                    f"ID: {note['id']}\nTitle: {note['title']}\nMessage: {note['message']}\nEdit time: {note['timestamp']};")
                break
        print("==================================================================")

    @staticmethod
    def display_empty_notes(error):
        print("******************************************************************")
        print("Sorry, but there are no notes yet to show you!")
        print("{}".format(error.args[0]))
        print("******************************************************************")

    @staticmethod
    def display_not_exist_note(note_id, error):
        print("******************************************************************")
        print("Sorry, but there are no note with id {}".format(note_id))
        print("{}".format(error.args[0]))
        print("******************************************************************")

    @staticmethod
    def display_deleted_note(note_id):
        print("==================================================================")
        print("Success deleted note with id {}".format(note_id))
        print("==================================================================")

    @staticmethod
    def display_invalid_command():
        print("******************************************************************")
        print("Invalid command. Please try again.")
        print("******************************************************************")
