from PyQt5.QtWidgets import QWidget
from card import main_line
from app import App
win_card = QWidget()
win_card.resize(600,500)
win_card.setWindowTitle("Memory Card")
win_card.move(0,0)

win_card.setLayout(main_line)

win_card.show()
App.exec_()