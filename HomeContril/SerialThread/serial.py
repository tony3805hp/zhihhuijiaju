#!/usr/bin/env python
# coding=utf-8
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import serial
from PyQt5.QtCore import QTimer
import time

# 增加了一个继承自QThread类的类，重新写了它的run()函数
# run()函数即是新线程需要执行的：执行一个循环；发送计算完成的信号。
class SerThread(QThread):
    trigger = pyqtSignal(str)

    def __int__(self):
        super(SerThread, self).__init__()

    def init_serial_port(self):
        print("init serial..")
        self.ser=serial.Serial()
        self.ser.port = 'COM3'
        self.ser.baudrate = 9600
        self.ser.bytesize = 8
        self.ser.stopbits = 1
        self.ser.parity = 'N'
        print("init port %s" % self.ser)

        # 定时器接收数据
        #self.timer = QTimer(self)
        #self.timer.timeout.connect(self.data_receive)

        try:
            self.ser.open()
        except:
            QMessageBox.critical(self, "Port Error", "此串口不能被打开！")
            return None

        # 打开串口接收定时器，周期为2ms
        #self.timer.start(2)

    def data_receive(self):
        try:
            num = self.ser.inWaiting()
        except:
            return None
        if num > 0:
            data = self.ser.read(num)
            num = len(data)
            if num==8:
                return data[4]

        else:
            pass

    def run(self):
        for i in range (0,10000):
            print("this is run %d" % i)
            # 循环完毕后发出信号
            time.sleep(1)
            data = self.data_receive()
            if data != None:
                temp ="emit " +str(i)
                self.trigger.emit(temp)


    def stop_receive(self):
        QMessageBox.about(self, "测试", "点击弹出窗口成功")