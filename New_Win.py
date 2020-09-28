from PyQt5 import QtCore, QtGui, QtWidgets
from os import rmdir , remove

class Ui_MainWindow(object):

    def __init__(self , ogwin , width , height , ui) :
        self.ogwin = ogwin
        self.width = width
        self.height = height
        self.saved = False
        self.ui = ui

    def setupUi(self, MainWindow):
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")

        MainWindow.setWindowIcon(QtGui.QIcon(
            "./Logo.ico"))

        if self.height > 795 :
            MainWindow.setFixedSize(self.width + 50, 975)
        else :
            MainWindow.setFixedSize(self.width + 50, self.height + 175)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        if self.height > 795 :  
            self.scrollarea = QtWidgets.QScrollArea(self.centralwidget)
            self.scrollarea.setGeometry(QtCore.QRect(25 , 25 , self.width, 795))
        else :
            pass

        self.label = QtWidgets.QLabel()
        self.label.setGeometry(QtCore.QRect(25, 25, self.width, self.height))
        self.label.setText("")
        
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)

        if self.height > 795 :
            self.pushButton.setGeometry(QtCore.QRect(25, 845, self.width, 50))
        else :
            self.pushButton.setGeometry(QtCore.QRect(25, 50 + self.height, self.width, 50))

        self.pushButton.clicked.connect(self.back)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)

        if self.height > 795 :
            self.pushButton2.setGeometry(QtCore.QRect(25, 900, self.width, 50))
        else :
            self.pushButton2.setGeometry(QtCore.QRect(25, 100 + self.height, self.width, 50))

        self.pushButton2.setFont(font)
        self.pushButton2.clicked.connect(self.save)

        if self.height > 795 :
            self.scrollarea.setWidget(self.label)
        else :
            self.label.setParent(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Back"))
        self.pushButton2.setText(_translate("MainWindow", "Save"))


    def back(self) :
        self.MainWindow.hide()
        self.ogwin.show()
        self.ui.pushButton_2.setEnabled(False)
        if self.saved :
            pass
        else :
            remove("./result-data/final-result.png")
            rmdir("./result-data")

    def save(self) :
        self.saved = True

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
