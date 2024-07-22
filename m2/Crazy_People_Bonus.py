from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QMessageBox
    
app = QApplication([])

main_win = QWidget()
main_win.setWindowTitle('Конкурс від Crazy People')
main_win.move(500,250)

def show_win():
    victory_win = QMessageBox()
    victory_win.move(900,250)
    victory_win.setWindowTitle('🎆Юху!🎉')
    victory_win.setText("Ви виграли зустріч з творцями каналу!")
    victory_win.exec_()

def show_lose():
    lose = QMessageBox()
    lose.move(900,250)
    lose.setWindowTitle('Oops😓')
    lose.setText("Пощастить іншим разом!")
    lose.exec_()

question = QLabel('Як звали першого ютуб-блогера, який набрав 100000000 підписників?')


btn_answer1 = QRadioButton('PewDiePie')
btn_answer2 = QRadioButton('Рет і Лінк')
btn_answer3 = QRadioButton('SlivkiShow')
btn_answer4 = QRadioButton('TheBrianMaps')
btn_answer5 = QRadioButton('Mister Max')
btn_answer6 = QRadioButton('EeOneGuy')

btn_answer1.clicked.connect(show_win)
btn_answer2.clicked.connect(show_lose)
btn_answer3.clicked.connect(show_lose)
btn_answer4.clicked.connect(show_lose)
btn_answer5.clicked.connect(show_lose)
btn_answer6.clicked.connect(show_lose)

layout_question = QHBoxLayout()
layout_question.addWidget(question, alignment=Qt.AlignCenter)

layout_h1 = QHBoxLayout()
layout_h1.addWidget(btn_answer1, alignment=Qt.AlignCenter)
layout_h1.addWidget(btn_answer2, alignment=Qt.AlignCenter)

layout_h2 = QHBoxLayout()
layout_h2.addWidget(btn_answer3, alignment=Qt.AlignCenter)
layout_h2.addWidget(btn_answer4, alignment=Qt.AlignCenter)

layout_h3 = QHBoxLayout()
layout_h3.addWidget(btn_answer5, alignment=Qt.AlignCenter)
layout_h3.addWidget(btn_answer6, alignment=Qt.AlignCenter)

layout_main = QVBoxLayout()
layout_main.addLayout(layout_question)
layout_main.addLayout(layout_h1)
layout_main.addLayout(layout_h2)
layout_main.addLayout(layout_h3)

main_win.setLayout(layout_main)
main_win.show()
app.exec_()

