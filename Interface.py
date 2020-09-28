from PyQt5 import QtCore, QtGui, QtWidgets
from Scraper import get_page_answers, save_data, combine_images
from QtThreading import Worker
from New_Win import Ui_MainWindow as Ui_Win2
import os

# constants
LOGO1_PATH = "./assets/Logo.png"
LOGO2_PATH = "./assets/Logo.ico"
BG_PATH = "./assets/BG.png"
SPINNING_LOGO_GIF = "./assets/Logo_Spinning.gif"


class Ui_MainWindow(object):

    def __init__(self, mw):
        self.mw = mw

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(700, 284)
        MainWindow.setWindowIcon(QtGui.QIcon(LOGO2_PATH))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 130, 161, 41))

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)

        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setObjectName("label")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(190, 130, 491, 41))

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)

        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 180, 671, 45))

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)

        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.startSpin)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 230, 671, 45))

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)

        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(290, 5, 121, 121))

        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_2.sizePolicy().hasHeightForWidth())

        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(LOGO1_PATH))
        self.label_2.setScaledContents(True)
        self.label_2.setWordWrap(False)
        self.label_2.setIndent(-1)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 701, 161))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(BG_PATH))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")

        self.label.raise_()
        self.lineEdit.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.label_2.raise_()

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "WolframScraper"))
        self.label.setText(_translate("MainWindow", "Search Item : "))
        self.pushButton.setText(_translate("MainWindow", "Search"))
        self.pushButton_2.setText(_translate("MainWindow", "Results"))

    def startSpin(self):
        if self.lineEdit.text() != "":
            self.movie = QtGui.QMovie(SPINNING_LOGO_GIF)
            self.label_2.setMovie(self.movie)
            self.movie.setSpeed(650)
            self.movie.start()
            self.threadpool = QtCore.QThreadPool()
            worker = Worker(self.calc)
            self.threadpool.start(worker)
            self.pushButton_2.clicked.connect(self.results)
            self.pushButton.setEnabled(False)
            self.pushButton_2.setEnabled(False)
        else:
            self.lineEdit.setText("Error : Please enter a valid search item")

    def calc(self):
        self.eq = self.lineEdit.text().strip()
        self.answer_imgs, self.answer_txt = get_page_answers(self.eq)
        img_name_list = save_data(self.answer_imgs, self.answer_txt)
        try:
            combine_images(img_name_list)
            self.movie.stop()
            self.label_2.setPixmap(QtGui.QPixmap(LOGO1_PATH))
            self.pushButton_2.clicked.connect(lambda: ...)
            self.pushButton.setEnabled(True)
            self.pushButton_2.setEnabled(True)
        except ValueError:
            self.lineEdit.setText("Your search did not yield any results")
            self.movie.stop()
            self.label_2.setPixmap(QtGui.QPixmap(LOGO1_PATH))
            self.pushButton_2.clicked.connect(lambda: ...)
            self.pushButton.setEnabled(True)
            self.pushButton_2.setEnabled(False)
            os.chdir("../")
            os.remove("./result-data/result-text-data.txt")
            os.rmdir("./result-data")

    def results(self):
        from Scraper import getimgsize
        width, height = getimgsize()
        self.win2 = QtWidgets.QMainWindow()
        self.ui2 = Ui_Win2(self.mw, width, height, self)
        self.ui2.setupUi(self.win2)

        self.ui2.label.setPixmap(QtGui.QPixmap(
            "./result-data/final-result.png"))
        self.win2.show()
        self.mw.hide()


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(MainWindow)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
