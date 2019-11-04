
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from DiningRoom.zhuwo import Ui_Formzw
from livingroom.keting import Ui_Form
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import QVideoWidget
from SerialThread.serial import SerThread

class MainHome(QWidget):

    def __init__(self, parent=None):
        super(MainHome, self).__init__(parent)
        self.resize(1280, 720)
        self.setWindowTitle("智能家居系统")

        window_pale = QPalette()
        tu = QPixmap("./images/bgall.png").scaled(self.width(), self.height())
        window_pale.setBrush(self.backgroundRole(), QBrush(tu))   # 设置背景图片
        self.setPalette(window_pale)

        player = QMediaPlayer(self)
        vw = QVideoWidget(self)
        vw.setGeometry(10, 50, 320, 240)
        player.setVideoOutput(vw)
        file = QUrl.fromLocalFile("images/1280x720.mp4") #QFileDialog.getOpenFileUrl()[0]

        player.setMedia(QMediaContent(file))  # 选取视频文件
        player.play()  # 播放视频

        self.kt =QPushButton(self)
        self.kt.setGeometry(10,550,200,30)
        self.kt.setStyleSheet("QPushButton{border-image: url(images/ketingbt.png)}")

        self.zw =QPushButton(self)
        self.zw.setGeometry(400,550,200,30)
        self.zw.setStyleSheet("QPushButton{border-image: url(images/zhuwobt.png)}")

        self.flg = QLabel(self)
        self.flg.setGeometry(700,550,200,30)
        self.flg.setText("只是测")

    def show_one_clock(self):
        QMessageBox.about(self, "测试", "点击弹出窗口成功")

    def show_flg(self,data):
        show="get "+data
        self.flg.setText(show)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    ktMainWindow = QMainWindow()
    uia = Ui_Form()
    uia.setupUi(ktMainWindow)
    ktMainWindow.setWindowModality(Qt.ApplicationModal)

    zwMainWindow = QMainWindow()
    uib = Ui_Formzw()
    uib.setupUi(zwMainWindow)

    ex = MainHome()
    ex.kt.clicked.connect(ktMainWindow.show)
    ex.zw.clicked.connect(zwMainWindow.show)
    #uia.pushButtona.clicked.connect(ex.show_one_clock)

    #th=SerThread()
    #th.init_serial_port()
    #th.trigger.connect(ex.show_flg)
    #th.start()

    #ex.init_serial_timer()

    ex.show()
    #ex.showFullScreen()

    sys.exit(app.exec_())