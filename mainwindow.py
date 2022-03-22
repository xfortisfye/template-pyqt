from config import ABSOLUTE_PATH
from dialog import Dialog

from PyQt5 import uic, QtWidgets, QtCore

from firstworker import FirstWorker

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        # call the inherited classes __init__ method
        super(MainWindow, self).__init__()

        # launch mainwindow.ui file
        uic.loadUi(f"{ABSOLUTE_PATH}/mainwindow.ui", self)

        # set gui window size
        self.setMinimumSize(QtCore.QSize(1280, 820))
        self.setMaximumSize(QtCore.QSize(1280, 820))

        self.pushButton.clicked.connect(lambda: self.popupDialog())
        self.pushButton_2.clicked.connect(lambda: self.importCSVDialog())
        self.pushButton_3.clicked.connect(lambda: self.startThread())
        
        self.threadpool = QtCore.QThreadPool()
        self.dot_counter = 0
        self.first_thread = None
    
    def popupDialog(self):
        
        if self.isSignalConnected(self.pushButton, 'clicked()'):
            self.pushButton.clicked.disconnect()

        dialog = Dialog()
        self.pushButton.clicked.connect(lambda: self.importCSVDialog())
    
    # launch QFileDialog to import CSV
    def importCSVDialog(self):
        # generate dialog window and save the selected file path result as csvUrl
        csvUrl, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Import CSV", "", "CSV Files (*.csv)")
        print(csvUrl)

    # def startTimerAndThread(self):
    #     self.loading_timer = QtCore.QTimer()
    #     self.loading_timer.setInterval(1000)
    #     self.dot_counter = 1
    #     self.loading_timer.timeout.connect(self.print_loading_timer)
    #     self.loading_timer.start()

    #     firstvar = "hello "
    #     secondvar = "world: "
    #     self.worker_thread = FirstWorker(firstvar, secondvar)
    #     self.worker_thread.signals.firstsignal.connect(self.execute_func1)
    #     self.worker_thread.signals.secondsignal.connect(self.passer)
    #     self.threadpool.start(self.worker_thread)

    def startThread(self):
        firstvar = "hello "
        secondvar = "world: "
        self.worker_thread = FirstWorker(firstvar, secondvar)
        self.worker_thread.signals.firstsignal.connect(self.execute_func1)
        self.worker_thread.signals.secondsignal.connect(self.execute_func2)
        self.worker_thread.start()

        # extra commands
        # self.worker_thread.wait() # pause thread
        # self.worker_thread.exit() # exit thread
        # self.worker_thread.signals.firstsignal.disconnect()
        # self.worker_thread.signals.secondsignal.disconnect()
        
    def execute_func1(self, value1):
        print(f"{value1}")
         

    def execute_func2(self, value2):
        print(f"{value2} {self.dot_counter}")

        self.dot_counter = self.dot_counter + 1

        if self.dot_counter > 5:
            self.dot_counter = 0
            self.worker_thread.wait()
            self.worker_thread.exit()

    def print_loading_timer(self):
        self.label.setStyleSheet("QLabel {color: black;}")

        dot_string = ""
        for _ in range(self.dot_counter):
            dot_string += "."
        self.label.setText("Loading " + dot_string)
        self.dot_counter += 1

        if self.dot_counter > 3:
            self.dot_counter = 1
        

    # check for repetitive signals
    def isSignalConnected(self, obj, name):
        index = obj.metaObject().indexOfMethod(name)
        if index > -1:
            method = obj.metaObject().method(index)
            if method:
                return obj.isSignalConnected(method)
        return False