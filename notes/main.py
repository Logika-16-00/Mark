from PyQt5.QtCore import QEvent
from PyQt5.QtWidgets import QApplication,QInputDialog
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QIcon
from notes import Ui_MainWindow
import json


class Widget(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_make.clicked.connect(self.add_note)
        self.ui.list_1.itemClicked.connect(self.show_note)
        for note in notes.keys():
            self.ui.list_1.addItem(note)
        self.ui.btn_save.clicked.connect(self.save_note)
        self.ui.btn_add.clicked.connect(self.add_tag)
        self.ui.btn_delete.clicked.connect(self.delete_notes)
        self.ui.btn_detach.clicked.connect(self.delete_tags)
        self.ui.pushButton.clicked.connect(self.change_theme)
        self.is_dark_theme = False
        self.setWindowTitle("Smart Notes")
        self.setWindowIcon(QIcon("notes/icon_notes.png"))

    
    def show_note(self, item):
        self.ui.list_2.clear()
        note_name= item.text()
        if note_name in notes:
            self.ui.list_2.addItems(notes[note_name]["теги"])
            self.ui.textEdit_2.setText(notes[note_name]["текст"])

    def save_note(self):
        if self.ui.list_1.currentItem():
            key = self.ui.list_1.currentItem().text()
            notes[key]["текст"] = self.ui.textEdit_2.toPlainText()
        self.write_to_file()

    def add_tag(self):
        if self.ui.list_1.currentItem():
            tag_name,ok =QInputDialog.getText(self, "Додати тег", "Введіть тег")
            note_name = self.ui.list_1.currentItem().text()
            if tag_name and ok:
                key = self.ui.list_1.currentItem().text()
                notes[key]["теги"].append(tag_name)
                self.ui.list_2.addItem(tag_name)
        self.write_to_file()

    def delete_notes(self):
        if self.ui.list_1.currentItem():
            note_name = self.ui.list_1.currentItem().text()
            del notes[note_name]
            self.ui.list_1.takeItem(self.ui.list_1.currentRow())
        self.write_to_file()

    def delete_tags(self):
        if self.ui.list_1.currentItem() and self.ui.list_2.currentItem():
            note_name = self.ui.list_1.currentItem().text()
            tag_name = self.ui.list_2.currentItem().text()
            self.ui.list_2.takeItem(self.ui.list_1.currentRow())
            notes[note_name]["теги"].remove(tag_name)
        self.write_to_file()

    def add_note(self):
        note_name,ok = QInputDialog.getText(self, "Додати замітку", "Назва замітки")

        if ok and note_name != "":
            notes[note_name] = {"теги": [], "текст": ""}
            self.ui.list_1.addItem(note_name)
        self.write_to_file()

    def write_to_file(self):
        with open("notes/notes.json","w", encoding="utf-8") as file:
            json.dump(notes, file,ensure_ascii=False) 


    def change_theme(self):
        btn_list = [self.ui.btn_save,self.ui.btn_detach,self.ui.btn_delete,self.ui.btn_add,self.ui.btn_make,self.ui.btn_search]
        self.is_dark_theme = not self.is_dark_theme
        if self.is_dark_theme:
            for btn in btn_list:
                btn.setStyleSheet("border: none;\n"
    "    border-radius: 10px;\n"
    "    text-decoration: none;\n"
    "    color: black;\n"
    "    background: #FFFF33;\n"
    "    box-shadow: 0 5px 0 #003CC5;")

            self.setStyleSheet("background: #808080;")
            self.ui.label_2.setStyleSheet("color: white;")
            self.ui.label.setStyleSheet("color: white;")

            
        else:
            for btn in btn_list:
                btn.setStyleSheet("border: none;\n"
    "    border-radius: 10px;\n"
    "    text-decoration: none;\n"
    "    color: white;\n"
    "    background: #0B63F6;\n"
    "    box-shadow: 0 5px 0 #003CC5;")
            self.setStyleSheet("background: 444;")
            self.ui.label.setStyleSheet("color: black;")
            self.ui.label_2.setStyleSheet("color: black;")

            

with open("notes/notes.json","r", encoding ="utf-8") as file:
    notes = json.load(file)
print(notes)

app = QApplication([])
ex = Widget()
ex.show()
app.exec_()