from app import *
from PyQt5.QtWidgets import QPushButton, QLineEdit, QFormLayout, QListView, QWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt

line_ans = QLineEdit("")
line_correct = QLineEdit("")
line_false1 = QLineEdit("")
line_false2 = QLineEdit("")
line_false3 = QLineEdit("")

#вікно для додавання і редагування питання
form = QFormLayout()
form.addRow("Введіть запитання:",line_ans)
form.addRow("Введіть правильну відповідь:",line_correct)
form.addRow("Введіть неправильний варіант №1:",line_false1)
form.addRow("Введіть неправильний варіант №2:",line_false2)
form.addRow("Введіть неправильний варіант №3:",line_false3)

#головне вікно де є список запитань і кнопки

list_q = QListView()

btn_add = QPushButton("Додати запитання")
btn_clear = QPushButton("Очистити запитання")
btn_back = QPushButton("Назад")

wdgt_edit = QWidget()
wdgt_edit.setLayout(form)

line1 = QVBoxLayout()
line1.addWidget(list_q)
line1.addWidget(btn_add)
line2 = QVBoxLayout()
line2.addWidget(wdgt_edit)
line2.addWidget(btn_clear)
line3 = QHBoxLayout()
line3.addLayout(line1)
line3.addLayout(line2)
line4 = QHBoxLayout()
line4.addWidget(btn_back, stretch=2)
main_menu_line = QHBoxLayout()
main_menu_line.addLayout(line3)
main_menu_line.addLayout(line4)