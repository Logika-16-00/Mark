from app import *
from PyQt5.QtWidgets import QPushButton, QSpinBox, QRadioButton, QLabel, QButtonGroup, QVBoxLayout,QHBoxLayout, QGroupBox, QWidget
from PyQt5.QtCore import Qt


btn_sleep = QPushButton("Відпочити")
box_minutes = QSpinBox()
box_minutes.setValue(30)
lb_min = QLabel("хвилин")

btn_menu = QPushButton("Меню")
btn_ans = QPushButton("Відповісти")
lb_ans = QLabel("Запитання")


btn_ans1 = QRadioButton("1")
btn_ans2 = QRadioButton("2")
btn_ans3 = QRadioButton("3")
btn_ans4 = QRadioButton("4")

AnswersGroupBox = QGroupBox("Варіанти відповідей")

RadioGroup = QButtonGroup()
RadioGroup.addButton(btn_ans1)
RadioGroup.addButton(btn_ans2)
RadioGroup.addButton(btn_ans3)
RadioGroup.addButton(btn_ans4)

layout1 = QHBoxLayout()
layout1.addWidget(btn_menu, alignment= Qt.AlignRight)
layout1.addStretch(3)
layout1.addWidget(btn_sleep, alignment=Qt.AlignRight)
layout1.addWidget(box_minutes, alignment= Qt.AlignRight)


line_btn_ans1 = QVBoxLayout()
line_btn_ans1.addWidget(btn_ans1)
line_btn_ans1.addWidget(btn_ans3)

line_btn_ans2 = QVBoxLayout()
line_btn_ans2.addWidget(btn_ans2)
line_btn_ans2.addWidget(btn_ans4)

mainline_btn_ans = QHBoxLayout()
mainline_btn_ans.addLayout(line_btn_ans1)
mainline_btn_ans.addLayout(line_btn_ans2)
AnswersGroupBox.setLayout(mainline_btn_ans)

main_line = QVBoxLayout()
main_line.addLayout(layout1)
main_line.addStretch(1)

main_line.addWidget(lb_ans,alignment=Qt.AlignCenter)
main_line.addStretch(1)
main_line.addWidget(AnswersGroupBox,stretch=5)

ResGroupBox = QGroupBox("Результат:")
lb_res = QLabel("Правильність")
lb_correct = QLabel("Правильна відповідь")
line_res = QVBoxLayout()
line_res.addWidget(lb_res)
line_res.addWidget(lb_correct)
ResGroupBox.setLayout(line_res)
main_line.addWidget(ResGroupBox)
main_line.addWidget(btn_ans)

ResGroupBox.hide()
