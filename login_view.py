# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_view.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(287, 271)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.platformLabel = QtWidgets.QLabel(self.centralwidget)
        self.platformLabel.setObjectName("platformLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.platformLabel)
        self.platformComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.platformComboBox.setObjectName("platformComboBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.platformComboBox)
        self.user_nameLabel = QtWidgets.QLabel(self.centralwidget)
        self.user_nameLabel.setObjectName("user_nameLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.user_nameLabel)
        self.user_nameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.user_nameLineEdit.setObjectName("user_nameLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.user_nameLineEdit)
        self.user_pwdLabel = QtWidgets.QLabel(self.centralwidget)
        self.user_pwdLabel.setObjectName("user_pwdLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.user_pwdLabel)
        self.user_pwdLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.user_pwdLineEdit.setObjectName("user_pwdLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.user_pwdLineEdit)
        self.verticalLayout.addLayout(self.formLayout)
        self.signinButton = QtWidgets.QPushButton(self.centralwidget)
        self.signinButton.setObjectName("signinButton")
        self.verticalLayout.addWidget(self.signinButton)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 287, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.platformLabel.setText(_translate("MainWindow", "平台"))
        self.user_nameLabel.setText(_translate("MainWindow", "用户名"))
        self.user_pwdLabel.setText(_translate("MainWindow", "密码"))
        self.signinButton.setText(_translate("MainWindow", "Sign In"))
