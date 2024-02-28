# Project "Notes_console"
## Information about project
It is necessary to write a project containing functionality for working with notes.
The program should be able to create a note, save it, read a list
notes, edit a note, delete a note.

## Task
Create a notes console application, with saving, reading,
adding, editing and deleting notes. The note should
contain the identifier, title, body of the note, and creation date/time, or
the note was last modified. Saving notes must be done in
json or csv format (it is recommended to separate fields using
semicolon). The student can implement the user interface
do as it is more convenient for him, you can do it as program launch parameters
(command, data), can be done as a command request from the console and
subsequent data entry, or otherwise, at the discretion of the student. For example:

    python notes.py add --title "новая заметка" –msg "тело новой заметки"

or 

    python note.py
    Введите команду: add
    Введите заголовок заметки: новая заметка
    Введите тело заметки: тело новой заметки
    Заметка успешно сохранена
    Введите команду:

When reading a list of notes, implement filtering by date.