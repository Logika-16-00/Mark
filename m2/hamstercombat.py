from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import randint
i = 0 
m  = 0
def click():
    global i
    global m
    num_win = randint(0,100)
    txt.setText("Hamster Coins:")
    txt2.setText(str(i))
    money.setText(str(m)+"$")
    i = i + 1
    m = m + 0.1
app = QApplication([])
win1 = QWidget()
win1.resize(500,250)
win1.move(250,150)
win1.setWindowTitle("hamster combat")
txt = QLabel("Click")
txt2 = QLabel("?")
tx2 = QLabel("Money:")
money = QLabel("0")
bnt = QPushButton("Натисни на мене")
bnt.clicked.connect(click)
line = QVBoxLayout()
line.addWidget(txt, alignment = Qt.AlignCenter)
line.addWidget(txt2, alignment = Qt.AlignCenter)
line.addWidget(bnt)
line.addWidget(tx2)
line.addWidget(money)
win1.setLayout(line)
win1.show()
app.exec_()
