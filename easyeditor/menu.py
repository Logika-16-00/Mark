import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QIcon, QPixmap, QImage
from ui import Ui_MainWindow
from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance


class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("EasyEditor")
        self.setWindowIcon(QIcon("easyeditor/photo_icon.png"))

        self.media_player = QMediaPlayer()
        self.image = Image.open("easyeditor/spongebob.jpg")
        self.update_image()
        self.ui.btn_left.clicked.connect(self.rotate_left)
        self.ui.btn_left.clicked.connect(self.rotate_right)
    


        url = QUrl.fromLocalFile("among-us-role-reveal-sound.wav")  
        content = QMediaContent(url)
        self.media_player.setMedia(content)


        self.ui.label_2.enterEvent = self.label_2_enter_event
        self.ui.label_2.leaveEvent = self.label_2_leave_event

        btn_list = [self.ui.btn_left, self.ui.btn_right, self.ui.btn_flip, self.ui.btn_bw, self.ui.btn_dir, self.ui.btn_sharp, self.ui.label, self.ui.listWidget]
        for btn in btn_list:
            btn.setStyleSheet("""
                QListWidget {
                    background-color: white;
                    border-radius: 5px;
                }
                QLabel {
                    border-radius: 5px;
                    background-color: white;
                }
                QPushButton {
                    background-color:#FFB621;
                    border-radius:10px;
                    font-weight: bold;
                }
                QPushButton:hover {
                    background-color: #0B63F6;
                    color: #000000;
                    font-weight: bold;
                    font-style: sans-serif;
                }
            """)

    def label_2_enter_event(self, event):
        self.media_player.play()

    def label_2_leave_event(self, event):
        self.media_player.stop()
    def update_image(self):
        self.ui.label.hide()
        self.image.save("easyeditor/spongebob_copy.jpg")
        pixmap = QPixmap("easyeditor/spongebob.jpg")
        w, h = self.ui.label.width(), self.ui.label.height()
        pixmap = pixmap.scaled(w, h)
        self.ui.label.setPixmap(pixmap)
        self.ui.label.show()
    
    def rotate_left(self):
        self.image = self.image.rotate(90)
        self.update_image()
    def rotate_right(self):
        self.image = self.image.rotate(-90)
        self.update_image()
    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Widget()
    ex.show()
    sys.exit(app.exec_())