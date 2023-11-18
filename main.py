import json

from PyQt5.QtWidgets import (QAppLication, QWidget, QPushButton, QLabel, QListWidget, QLineEdit, QTextEdit, QInputDialog, QHBoxLayout, QVBoxLayout, QFormLayout )

app = QAppLication([])

notes_win = QWidget()
notes_win.setWindowTitle('')
notes_win.resize(900, 600)
list_notes = QListWidget()
list_notes_label = QLabel('')
button_note_del = QPushButton('')
button_note_create = QPushButton('')
button_note_save = QPushButton('')

field_tag = QLineEdit('')
field_tag.setPlaceholderText('')
field_text = QTextEdit()
button_note_add = QPushButton('')
button_note_del = QPushButton('')
button_note_search = QPushButton('')
list_tags = QListWidget()
list_tags_label = QLabel()

layout_notes = QHBoxLayout()
col_1 = QVBoxLayout()
col_1.addWidget(list_notes)

col_2 = QVBoxLayout()
col_2.addWidget(list_notes_label)
col_2.addWidget(list_notes)

row_1 = QHBoxLayout()
row_1.addWidget(button_note_create)
row_1.addWidget(button_note_del)

row_2 = QHBoxLayout()
row_2.addWidget(button_note_save)

col_2.addLayout(row_1)
col_2.addLayout(row_2)

col_2.addWidget(list_tags_label)
col_2.addWidget(list_tags)
col_2.addWidget(field_tag)

row_3 = QHBoxLayout()
row_3.addWidget(button_note_add)
row_3.addWidget(button_note_del)

row_4 = QHBoxLayout()
row_4.addWidget(button_note_search)

col_2.addLayout(row_3)
col_2.addLayout(row_4)

layout_notes.addLayout(col_1, stretch=2)
layout_notes.addLayout(col_2, stretch=1)
notes_win.setLayout(layout_notes)
notes_win.show()

def add_note():
    note_name, ok = QInputDialog.getText(notes_win, 'Дотати замітку', 'Назва замітки' )
    if ok and note_name != '':
        notes[note_name] = {'текст': '', 'теги': []}
        list_notes.addItems(note_name)
        list_tags.addItems(notes[note_name]['теги'])
        print(notes)
button_note_create.clicked.connect(add_note())

def show_note():
    key = list_notes.selectedItems()[0].text()
    print(key)
    field_text.setText(notes[key]['текст'])
    list_tags.clear()
    list_tags.addItems(notes[key]['теги'])
list_notes.itemClicked.connect(show_note)

def save_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        notes[key][''] = field_text.toPlainText()
        with open('notes_data.json', 'w') as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
        print(notes)
    else:
        print('')
button_note_save.clicked(save_note)

def del_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        del notes[key]
        list_notes.clear()
        list_tags.clear()
        field_text.clear()
        list_notes.addItems(notes)
        with open('notes_data.json', 'w') as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
        print(notes)
    else:
        print('замітка для видалення не вибрана!')
button_note_del.clicked.connect(del_note)

with open('notes_data.json', 'r') as file:
    notes = json.load(file)
list_notes.addItems((notes))

app.exec_()
