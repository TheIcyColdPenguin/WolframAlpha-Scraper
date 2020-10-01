# imports
from PyQt5 import QtCore, QtGui, QtWidgets
from os import rmdir, remove


class Ui_MainWindow(object):
    '''
    A class to handle the Results window.
    Responsible for creating the GUI and running the functionality
    '''

    def __init__(self, ogwin, width, height, ui):
        '''
        Initialising the class.
        This is called whenever an object of this class is created.
        Parameters:
        ogwin (QtWidgets.QMainWindow): The original main window from where this class was called
        width (int): The width of the window
        height (int): The height of the window
        self (QtWidgets.QtGui): The UI of the window it was called from
        '''
        # Declaring and setting up the variables needed for the geometry of the window
        self.ogwin = ogwin
        self.width = width
        self.height = height
        self.saved = False
        self.ui = ui

    def setupUi(self, MainWindow):
        '''
        Setup the UI. This includes declaring several UI elements such as Buttons, Labels and Images
        Parameters:
        MainWindow (QtWidgets.QMainWindow): The main window in which the app is created
        '''
        # Creating a colour palette and applying it to the Main Window
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        self.MainWindow = MainWindow
        MainWindow.setObjectName("Results")
        MainWindow.setWindowIcon(QtGui.QIcon("./assets/Logo.ico"))
        # Linking the window size to the image size
        if self.height > 795:
            MainWindow.setFixedSize(self.width + 50, 975)
        else:
            MainWindow.setFixedSize(self.width + 50, self.height + 175)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        if self.height > 795:
            self.scrollarea = QtWidgets.QScrollArea(self.centralwidget)
            self.scrollarea.setGeometry(QtCore.QRect(25, 25, self.width, 795))

        self.label = QtWidgets.QLabel()
        self.label.setGeometry(QtCore.QRect(25, 25, self.width, self.height))
        self.label.setText("")

        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)

        if self.height > 795:
            self.pushButton.setGeometry(QtCore.QRect(
                25, 845, self.width, 50))
        else:
            self.pushButton.setGeometry(QtCore.QRect(
                25, 50 + self.height, self.width, 50))

        self.pushButton.clicked.connect(self.back)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)

        if self.height > 795:
            self.pushButton2.setGeometry(QtCore.QRect(
                25, 900, self.width, 50))
        else:
            self.pushButton2.setGeometry(QtCore.QRect(
                25, 100 + self.height, self.width, 50))

        self.pushButton2.setFont(font)
        self.pushButton2.clicked.connect(self.save)

        if self.height > 795:
            self.scrollarea.setWidget(self.label)
        else:
            self.label.setParent(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        '''
        Editing the various UI elements to display the required text and translation
        Parameters:
        MainWindow (QtWidgets.QMainWindow): The main window in which the app is created
        '''
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Back"))
        self.pushButton2.setText(_translate("MainWindow", "Save"))

    def back(self):
        '''
        Executed when the back button is pressed.
        It closes down the current window and reopens
        the main window
        '''
        # Switching to the main window
        self.MainWindow.hide()
        self.ogwin.show()
        self.ui.pushButton_2.setEnabled(False)
        if not self.saved:  # removing cache if not saved
            remove("./result-data/final-result.png")
            rmdir("./result-data")

    def save(self):
        '''
        Saves the folder containing the result-data
        in the current working directory
        '''
        self.saved = True
        self.back()


# To avoid the application being run if imported
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
