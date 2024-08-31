from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow
import random

class Widget(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.generation)
    def generation(self):
        signs = ""
        if self.ui.checkBox_2.isChecked():
            signs += "abcdefgeigklmopqrstuwwsyz"
        if self.ui.checkBox_3.isChecked():
            signs += "1234567890"
        if self.ui.checkBox.isChecked():
            signs += "+= ~!@#$%^&*()_+"
        # else:
        #     self.ui.label_2.setText("Параметри пароля не вибрані")
        #     return
        res = ""
        num = random.randint(8,12)
        for i in range(num):
            res += random.choice(signs)
        self.ui.label_2.setText(res)

app = QApplication([])
ex = Widget()
ex.show()
app.exec_()