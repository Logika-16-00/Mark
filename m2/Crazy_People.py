from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QMessageBox
    
app = QApplication([])

main_win = QWidget()
main_win.setWindowTitle('Конкурс від Crazy People')
main_win.move(500,250)

def show_win():
    victory_win = QMessageBox()
    victory_win.move(825,250)
    victory_win.setWindowTitle('🎆Юху!🎉')
    victory_win.setText("Правильно!\nВи виграли гіроскутер")
    victory_win.exec_()

def show_lose():
    lose = QMessageBox()
    lose.move(825,250)
    lose.setWindowTitle('Oops😓')
    lose.setText("Ні, в 2015 році.\nВи виграли фірмовий плакат")
    lose.exec_()

question = QLabel('В якому році канал отримав «золоту кнопку» від YouTube?')


btn_answer1 = QRadioButton('2005')
btn_answer2 = QRadioButton('2010')
btn_answer3 = QRadioButton('2015')
btn_answer4 = QRadioButton('2020')

btn_answer1.clicked.connect(show_win)
btn_answer2.clicked.connect(show_lose)
btn_answer3.clicked.connect(show_lose)
btn_answer4.clicked.connect(show_lose)
layout_question = QHBoxLayout()
layout_question.addWidget(question, alignment=Qt.AlignCenter)

layout_h1 = QHBoxLayout()
layout_h1.addWidget(btn_answer1, alignment=Qt.AlignCenter)
layout_h1.addWidget(btn_answer2, alignment=Qt.AlignCenter)

layout_h2 = QHBoxLayout()
layout_h2.addWidget(btn_answer3, alignment=Qt.AlignCenter)
layout_h2.addWidget(btn_answer4, alignment=Qt.AlignCenter)


layout_main = QVBoxLayout()
layout_main.addLayout(layout_question)
layout_main.addLayout(layout_h1)
layout_main.addLayout(layout_h2)

main_win.setLayout(layout_main)
main_win.show()

app.exec_()

