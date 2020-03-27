import sys
import os
import json
from PyQt5 import  QtCore, QtWidgets, uic
#   引入ui文件
from login_view import Ui_MainWindow as Ui
#   引入登录模块
from DecryptLogin import login
from PIL import Image



def fname(fuc):
    return fuc

class MyApp(QtWidgets.QMainWindow, Ui):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui.__init__(self)
        self.setupUi(self)
        self._initdata();
        self.signinButton.clicked.connect(self.signin)

    def _initdata(self):
        with open("./config-default.json", encoding='utf-8') as defcfg:
            cfg = json.load(defcfg)
            for k in cfg:
                self.platformComboBox.addItem(cfg[k]["name"], k)

    def signin(self):
        platform = self.platformComboBox.currentData()
        usarname = self.user_nameLineEdit.text()
        userpwd = self.user_pwdLineEdit.text()
        lg = login.Login()
        fuc = getattr(lg, platform, None)
        infos_return, session = fuc(usarname, userpwd, 'pc', app = self)
        print(infos_return, session)

    def userInput(self):
        code, *_ = QtWidgets.QInputDialog.getText(self, "验证码", "请输入验证码:", QtWidgets.QLineEdit.Normal, '')
        return code

    def crackvcFunc(self, imagepath):
        # 打开验证码图片
        img = Image.open(imagepath)
        # 识别验证码图片
        result = Image.IdentifyAPI(img)
        # 返回识别结果(知乎为数字验证码)
        return result

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
