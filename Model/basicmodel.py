import datetime
import json

filename = "notes.json"


class BasicModel(object):
    def __init__(self):

        pass

    @staticmethod
    def create_notes_file():
        with open(filename, "w") as file:
            json.dump([], file)

    def load_notes(self):
        try:
            with open(filename, "r") as file:
                notes = json.load(file)
        except (json.JSONDecodeError, FileNotFoundError):
            self.create_notes_file()
            notes = []
        return notes

    @staticmethod
    def create_note(notes, title, message):
        note_id = len(notes) + 1
        timestamp = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        note = {"id": note_id, "title": title, "message": message, "timestamp": timestamp}
        notes.append(note)
        return notes

    @staticmethod
    def show_note(notes, note_id):
        for note in notes:
            if note["id"] == note_id:
                print(
                    f"ID: {note['id']}, Title: {note['title']}, Message: {note['message']}, Created time: {note['timestamp']}")
                break
        else:
            print("Заметка с указанным ID не найдена.")

    @staticmethod
    def edit_note(notes, note_id, new_title, new_message):
        for note in notes:
            if note["id"] == note_id:
                note["title"] = new_title
                note["message"] = new_message
                note["timestamp"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                break
        else:
            print("Заметка с указанным ID не найдена.")
        return notes

    @staticmethod
    def save_notes(notes):
        with open(filename, "w") as file:
            json.dump(notes, file, indent=4)

    @staticmethod
    def delete_note(notes, note_id):
        notes = [note for note in notes if note["id"] != note_id]
        return notes
