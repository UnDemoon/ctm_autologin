import sys
import os
import json
from PyQt5 import  QtCore, QtWidgets, uic
#   引入ui文件
from login_view import Ui_MainWindow as Ui
#   引入登录模块
from DecryptLogin import login


class MyApp(QtWidgets.QMainWindow, Ui):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui.__init__(self)
        self.setupUi(self)
        self._initdata();

    def _initdata(self):
        with open("./config.json", encoding='utf-8') as f:
            config = json.load(f)
            for k in config:
                self.platformComboBox.addItem(config[k]["name"])

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
