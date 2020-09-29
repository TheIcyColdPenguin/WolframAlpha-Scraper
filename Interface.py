# Imports
from PyQt5 import QtCore , QtGui, QtWidgets
from Scraper import get_page_answers , save_data , combine_images
from QtThreading import Worker
from New_Win import Ui_MainWindow as Ui_Win2
import os

# The GUI class
class Ui_MainWindow(object):
    '''
    A class to handle the frontend.
    Responsible for creating the GUI and running the functionality
    '''
    def __init__(self , mw:QtWidgets.QMainWindow) :
        '''
        Initialising the class.
        This is called whenever an object of this class is created.

        Parameters:
        mw (QtWidgets.QMainWindow): The main window in which the app is created
        '''
        self.mw = mw

    def setupUi(self, MainWindow:QtWidgets.QMainWindow):
        '''
        Setup the UI. This includes declaring several UI elements such as Buttons, Labels and Images

        Parameters:
        MainWindow (QtWidgets.QMainWindow): The main window in which the app is created
        '''
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(700, 284)
        MainWindow.setWindowIcon(QtGui.QIcon("./assets/Logo.ico"))
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
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())

        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("./assets/Logo.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setWordWrap(False)
        self.label_2.setIndent(-1)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 701, 161))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("./assets/BG.png"))
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

    def retranslateUi(self, MainWindow:QtWidgets.QMainWindow):
        '''
        Editing the various UI elements to display the required text and translation

        Parameters:
        MainWindow (QtWidgets.QMainWindow): The main window in which the app is created
        '''
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "WolframScraper"))
        self.label.setText(_translate("MainWindow", "Search Item : "))
        self.pushButton.setText(_translate("MainWindow", "Search"))
        self.pushButton_2.setText(_translate("MainWindow", "Results"))

    def startSpin(self):
        '''
        Starts the spinning of the app logo
        and starts threading to keep the 
        GUI and the backend on separate threads.
        Also sends a signal to start the calculation
        '''
        if self.lineEdit.text() != "" :
            self.movie = QtGui.QMovie("./assets/Logo_Spinning.gif")
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
        '''
        Using the backend to calculate
        the results of the search item.
        '''
        self.eq = self.lineEdit.text().strip()
        self.answer_imgs, self.answer_txt = get_page_answers(self.eq)
        img_name_list = save_data(self.answer_imgs, self.answer_txt)
        try :
            combine_images(img_name_list)
            self.movie.stop()
            self.label_2.setPixmap(QtGui.QPixmap("./assets/Logo.png"))
            self.pushButton_2.clicked.connect(lambda: ...)
            self.pushButton.setEnabled(True)
            self.pushButton_2.setEnabled(True)
        except ValueError :
            self.lineEdit.setText("Your search did not yield any results")
            self.movie.stop()
            self.label_2.setPixmap(QtGui.QPixmap("./assets/Logo.png"))
            self.pushButton_2.clicked.connect(lambda : ...)
            self.pushButton.setEnabled(True)
            self.pushButton_2.setEnabled(False)
            os.chdir("../")
            os.remove("./result-data/result-text-data.txt")
            os.rmdir("./result-data")

    def results(self) :
        '''
        Setting up the fetched results to
        open up in a new window and
        launch the window
        '''
        from Scraper import getimgsize
        width, height = getimgsize()
        self.win2 = QtWidgets.QMainWindow()
        self.ui2 = Ui_Win2(self.mw , width , height , self)
        self.ui2.setupUi(self.win2)
        
        self.ui2.label.setPixmap(QtGui.QPixmap("./result-data/final-result.png"))
        self.win2.show()
        self.mw.hide()

def main():
    '''
    The main function that sets up the application and launches it.
    '''
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(MainWindow)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
