import datetime
import json

import Service.exceptions

filename = "notes.json"


def create_notes_file():
    with open(filename, "w") as file:
        json.dump([], file)


def load_notes():
    try:
        with open(filename, "r") as file:
            notes = json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        create_notes_file()
        notes = []
    return notes


def create_note(notes, title, message):
    note_id = len(notes) + 1
    timestamp = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    note = {"id": note_id, "title": title, "message": message, "timestamp": timestamp}
    notes.append(note)
    return notes


def edit_note(note_id, new_title, new_message):
    with open(filename, "r") as file:
        notes = json.load(file)
        for note in notes:
            if note["id"] == int(note_id):
                note["title"] = new_title
                note["message"] = new_message
                note["timestamp"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                break
            else:
                raise Service.exceptions.NoteNotExist("Note does not exist!")
    with open(filename, "w") as file:
        json.dump(notes, file, indent=4)
    return notes


def save_notes(notes):
    with open(filename, "w") as file:
        json.dump(notes, file, indent=4)


def delete_note(note_id):
    check = 0
    with open(filename, "r") as file:
        notes = json.load(file)
        for note in notes:
            check += 1
            if note["id"] == int(note_id):
                notes.remove(note)
                break
            elif check == notes.__len__() - 1:
                raise Service.exceptions.NoteNotExist("Note does not exist!")
    with open(filename, "w") as file:
        json.dump(notes, file, indent=4)
    return notes
