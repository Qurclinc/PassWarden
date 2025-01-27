# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Register.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RegisterWindow(object):
    def setupUi(self, RegisterWindow):
        RegisterWindow.setObjectName("RegisterWindow")
        RegisterWindow.resize(640, 480)
        RegisterWindow.setStyleSheet("background-color: rgb(6, 38, 111);\n"
"font: 14pt \"DejaVu Serif\";\n"
"color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(RegisterWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(140, 100, 391, 261))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setStyleSheet("font: 16pt \"DejaVu Serif\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.login_line = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.login_line.setStyleSheet("border:none;\n"
"background-color: rgb(70, 113, 213);")
        self.login_line.setObjectName("login_line")
        self.verticalLayout_2.addWidget(self.login_line)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.passwd_line = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.passwd_line.setStyleSheet("border:none;\n"
"background-color: rgb(70, 113, 213);\n"
"")
        self.passwd_line.setObjectName("passwd_line")
        self.passwd_line.setEchoMode(QtWidgets.QLineEdit.Password)
        self.verticalLayout_2.addWidget(self.passwd_line)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.passwd2_line = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.passwd2_line.setStyleSheet("border:none;\n"
"background-color: rgb(70, 113, 213);")
        self.passwd2_line.setObjectName("passwd2_line")
        self.passwd2_line.setEchoMode(QtWidgets.QLineEdit.Password)
        self.verticalLayout_2.addWidget(self.passwd2_line)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.register_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.register_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(42, 68, 128);\n"
"    color: white;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(18, 64, 171);\n"
"}")
        self.register_btn.setObjectName("register_btn")
        self.horizontalLayout.addWidget(self.register_btn)
        self.log_in_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.log_in_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(42, 68, 128);\n"
"    color: white;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(18, 64, 171);\n"
"}")
        self.log_in_btn.setObjectName("log_in_btn")
        self.horizontalLayout.addWidget(self.log_in_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.verticalWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalWidget_2.setGeometry(QtCore.QRect(520, 410, 111, 54))
        self.verticalWidget_2.setObjectName("verticalWidget_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalWidget_2)
        self.verticalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.credits = QtWidgets.QLabel(self.verticalWidget_2)
        self.credits.setStyleSheet("font: italic 10pt \"Droid Sans Fallback\";")
        self.credits.setObjectName("credits")
        self.verticalLayout_4.addWidget(self.credits)
        self.label_6 = QtWidgets.QLabel(self.verticalWidget_2)
        self.label_6.setStyleSheet("font: italic 10pt \"Droid Sans Fallback\";\n"
"")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)
        RegisterWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(RegisterWindow)
        QtCore.QMetaObject.connectSlotsByName(RegisterWindow)

    def retranslateUi(self, RegisterWindow):
        _translate = QtCore.QCoreApplication.translate
        RegisterWindow.setWindowTitle(_translate("RegisterWindow", "Регистрация"))
        self.label.setText(_translate("RegisterWindow", "Регистрация"))
        self.label_2.setText(_translate("RegisterWindow", "Логин"))
        self.label_3.setText(_translate("RegisterWindow", "Пароль"))
        self.label_4.setText(_translate("RegisterWindow", "Повтор пароля"))
        self.register_btn.setText(_translate("RegisterWindow", "Регистрация"))
        self.log_in_btn.setText(_translate("RegisterWindow", "Войти"))
        self.credits.setText(_translate("RegisterWindow", "v. 0.0.1"))
        self.label_6.setText(_translate("RegisterWindow", "made by CXDER"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RegisterWindow = QtWidgets.QMainWindow()
    ui = Ui_RegisterWindow()
    ui.setupUi(RegisterWindow)
    RegisterWindow.show()
    sys.exit(app.exec_())
