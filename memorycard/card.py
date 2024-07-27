from memorycard.app import *
App = QApplication([])


win_card = QWidget([])
win_card.resize(600,500)
win_card.setWindowTitle("Memory Card")
win_card.move(0,0)

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
layout1.addWidget(btn_menu, aligment=Qt.AlignmentLeft)
layout1.addWidget(btn_sleep, alignment=Qt.AlignmentRight)
layout1.addWidget(box_minutes, alignment= Qt.AlignmentRight)


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
main_line.addWidget(lb_ans)
main_line.addWidget(AnswersGroupBox)
main_line.addWidget(btn_ans)
win_card.setLayout(main_line)

win_card.show()
App.exec_()