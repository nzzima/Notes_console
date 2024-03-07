from Model import backend_functions


class BasicModel(object):
    def __init__(self):
        pass

    @staticmethod
    def create_notes_file():
        backend_functions.create_notes_file()

    @staticmethod
    def load_notes():
        return backend_functions.load_notes()

    @staticmethod
    def create_note(notes, title, message):
        return backend_functions.create_note(notes, title, message)

    @staticmethod
    def edit_note(note_id, new_title, new_message):
        return backend_functions.edit_note(note_id, new_title, new_message)

    @staticmethod
    def save_notes(notes):
        backend_functions.save_notes(notes)

    @staticmethod
    def delete_note(note_id):
        return backend_functions.delete_note(note_id)
