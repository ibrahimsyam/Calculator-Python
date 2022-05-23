# تم تصميم هدي الحاسبة في يوم 20 اغسطس 2021
# المبرمج ابراهيم صيام

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        width = 310
        height = 435
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        MainWindow.setFixedSize(width, height)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it(''))
        self.pushButton.setGeometry(QtCore.QRect(0, 70, 81, 61))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(199, 66, 0);\n"
"background-color: rgb(0, 0, 0)")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_d = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.remove_it())
        self.pushButton_d.setGeometry(QtCore.QRect(80, 70, 131, 61))
        self.pushButton_d.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_d.setStyleSheet("QPushButton{\n"
"font: 75 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(253, 0, 0);\n"
"}\n"
"")
        self.pushButton_d.setObjectName("pushButton_d")
        self.pushButton_44 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it('+'))
        self.pushButton_44.setGeometry(QtCore.QRect(230, 70, 91, 61))
        self.pushButton_44.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_44.setStyleSheet("QPushButton{\n"
"font: 75 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(144, 144, 144);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(144, 144, 144);\n"
"}\n"
"")
        self.pushButton_44.setObjectName("pushButton_44")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it('7'))
        self.pushButton_7.setGeometry(QtCore.QRect(0, 130, 71, 71))
        self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_7.setStyleSheet("QPushButton{\n"
"font: 75 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(144, 144, 144);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(144, 144, 144);\n"
"}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it('8'))
        self.pushButton_8.setGeometry(QtCore.QRect(70, 130, 71, 71))
        self.pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_8.setStyleSheet("QPushButton{\n"
"font: 75 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(144, 144, 144);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(144, 144, 144);\n"
"}")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it('9'))
        self.pushButton_9.setGeometry(QtCore.QRect(140, 130, 71, 71))
        self.pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_9.setStyleSheet("QPushButton{\n"
"font: 75 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(144, 144, 144);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(144, 144, 144);\n"
"}")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_77 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it('-'))
        self.pushButton_77.setGeometry(QtCore.QRect(230, 150, 91, 51))
        self.pushButton_77.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_77.setStyleSheet("QPushButton{\n"
"font: 75 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(144, 144, 144);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(144, 144, 144);\n"
"}")
        self.pushButton_77.setObjectName("pushButton_77")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it('4'))
        self.pushButton_4.setGeometry(QtCore.QRect(0, 200, 71, 71))
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"font: 75 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(144, 144, 144);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(144, 144, 144);\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it('5'))
        self.pushButton_5.setGeometry(QtCore.QRect(70, 200, 71, 71))
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"font: 75 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(144, 144, 144);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(144, 144, 144);\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it('6'))
        self.pushButton_6.setGeometry(QtCore.QRect(140, 200, 71, 71))
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_6.setStyleSheet("QPushButton{\n"
"font: 75 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(144, 144, 144);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(144, 144, 144);\n"
"}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it('1'))
        self.pushButton_1.setGeometry(QtCore.QRect(0, 270, 71, 71))
        self.pushButton_1.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_1.setStyleSheet("QPushButton{\n"
"font: 75 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(144, 144, 144);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(144, 144, 144);\n"
"}")
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it('2'))
        self.pushButton_2.setGeometry(QtCore.QRect(70, 270, 71, 71))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"font: 75 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(144, 144, 144);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(144, 144, 144);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it('3'))
        self.pushButton_3.setGeometry(QtCore.QRect(140, 270, 71, 71))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"font: 75 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(144, 144, 144);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(144, 144, 144);\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget, )
        self.lineEdit.setGeometry(QtCore.QRect(0, 0, 310, 61))
        self.lineEdit.setCursor(QtGui.QCursor(QtCore.Qt.SizeVerCursor))
        self.lineEdit.setMouseTracking(False)
        self.lineEdit.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 20pt \"MS Shell Dlg 2\";")

        self.lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it('*'))
        self.pushButton_10.setGeometry(QtCore.QRect(230, 220, 91, 51))
        self.pushButton_10.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_10.setStyleSheet("QPushButton{\n"
"font: 75 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(144, 144, 144);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(144, 144, 144);\n"
"}")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it('/'))
        self.pushButton_11.setGeometry(QtCore.QRect(230, 290, 91, 51))
        self.pushButton_11.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_11.setStyleSheet("QPushButton{\n"
"font: 75 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(144, 144, 144);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(144, 144, 144);\n"
"}")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.p_s())
        self.pushButton_12.setGeometry(QtCore.QRect(0, 342, 75, 61))
        self.pushButton_12.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_12.setStyleSheet("QPushButton{\n"
"font: 75 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(144, 144, 144);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(144, 144, 144);\n"
"}")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it('0'))
        self.pushButton_13.setGeometry(QtCore.QRect(80, 350, 71, 51))
        self.pushButton_13.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_13.setStyleSheet("QPushButton{\n"
"font: 75 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(144, 144, 144);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(144, 144, 144);\n"
"}")
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.dot_it())
        self.pushButton_14.setGeometry(QtCore.QRect(150, 350, 61, 51))
        self.pushButton_14.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_14.setStyleSheet("QPushButton{\n"
"font: 75 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(144, 144, 144);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(144, 144, 144);\n"
"}")
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.equl())
        self.pushButton_15.setGeometry(QtCore.QRect(230, 360, 91, 41))
        self.pushButton_15.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_15.setStyleSheet("QPushButton{\n"
"font: 75 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(144, 144, 144);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(144, 144, 144);\n"
"}")
        self.pushButton_15.setObjectName("pushButton_15")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def dot_it(self):
        screen = self.lineEdit.text()
        if screen[-1] == "." == ".":
            pass
        else:
            self.lineEdit.setText(f'{screen}.')

    def remove_it(self):
        screen = self.lineEdit.text()
        screen = screen[:-1]
        self.lineEdit.setText(screen)


    def equl(self):
        screen = self.lineEdit.text()
        answer = eval(screen)
        self.lineEdit.setText(str(answer))


    def p_s(self):
        screen = self.lineEdit.text()
        if "-" in screen:
            self.lineEdit.setText(screen.replace("-", ''))
        else:
            self.lineEdit.setText(f'-{screen}')


    def press_it(self, pressed):
        if pressed == '':
            self.lineEdit.setText('0')
        else:
            if self.lineEdit.text() == "0":
                self.lineEdit.setText("")
        self.lineEdit.setText(f'{self.lineEdit.text()}{pressed}')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "c"))
        self.pushButton_d.setText(_translate("MainWindow", "del"))
        self.pushButton_44.setText(_translate("MainWindow", "+"))
        self.pushButton_7.setText(_translate("MainWindow", "7"))
        self.pushButton_8.setText(_translate("MainWindow", "8"))
        self.pushButton_9.setText(_translate("MainWindow", "9"))
        self.pushButton_77.setText(_translate("MainWindow", "-"))
        self.pushButton_4.setText(_translate("MainWindow", "4"))
        self.pushButton_5.setText(_translate("MainWindow", "5"))
        self.pushButton_6.setText(_translate("MainWindow", "6"))
        self.pushButton_1.setText(_translate("MainWindow", "1"))
        self.pushButton_2.setText(_translate("MainWindow", "2"))
        self.pushButton_3.setText(_translate("MainWindow", "3"))
        self.pushButton_10.setText(_translate("MainWindow", "X"))
        self.pushButton_11.setText(_translate("MainWindow", "÷"))
        self.pushButton_12.setText(_translate("MainWindow", "+/-"))
        self.pushButton_13.setText(_translate("MainWindow", "0"))
        self.pushButton_14.setText(_translate("MainWindow", "."))
        self.pushButton_15.setText(_translate("MainWindow", "="))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())