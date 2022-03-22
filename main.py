import sys
# import resources
from mainwindow import MainWindow
from PyQt5 import QtWidgets

def main():
    # Launching the GUI
    app = QtWidgets.QApplication(sys.argv)
    app.aboutToQuit.connect(lambda: MainWindow.clear())
    # app.aboutToQuit.connect(lambda: MainWindow.shutdown())
    mainwindow = MainWindow()
    mainwindow.setWindowTitle("Template")
    mainwindow.show()
    sys.exit(app.exec_())    

if __name__ == "__main__":
    main()