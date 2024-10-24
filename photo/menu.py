import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QIcon
from ui import Ui_MainWindow


class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Photoshop")
        self.setWindowIcon(QIcon("photo/photo_icon.png"))

        self.media_player = QMediaPlayer()


        url = QUrl.fromLocalFile("among-us-role-reveal-sound.wav")  # Update with your sound file path
        content = QMediaContent(url)
        self.media_player.setMedia(content)


        self.ui.label_2.enterEvent = self.label_2_enter_event
        self.ui.label_2.leaveEvent = self.label_2_leave_event

        btn_list = [self.ui.btn_left, self.ui.btn_right, self.ui.btn_flip, self.ui.btn_bw, self.ui.btn_dir, self.ui.btn_sharp]
        for btn in btn_list:
            btn.setStyleSheet("""
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Widget()
    ex.show()
    sys.exit(app.exec_())