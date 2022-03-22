from config import ABSOLUTE_PATH
from PyQt5 import uic, QtWidgets, QtCore

class Dialog(QtWidgets.QDialog):

    def __init__(self, parent=None):
        super(Dialog, self).__init__()
        # launch mainwindow.ui file
        uic.loadUi(f"{ABSOLUTE_PATH}/dialog.ui", self)

        # set gui window size
        self.setMinimumSize(QtCore.QSize(300, 400))
        self.setMaximumSize(QtCore.QSize(300, 400))
        self.setWindowFlags(QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint
                            | QtCore.Qt.WindowCloseButtonHint)

        if self.isSignalConnected(self.submit_dialog_button, 'clicked()'):
            self.submit_dialog_button.clicked.disconnect()
        self.submit_dialog_button.clicked.connect(lambda: self.getResults())
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)

        self.exec_()

    def getUsername(self):
        return self.username.text()

    def getPassword(self):
        return self.password.text()

    def getResults(self):
        if self.getUsername() and self.getPassword():
            if self.isSignalConnected(self.submit_dialog_button, 'clicked()'):
                self.submit_dialog_button.clicked.disconnect()
            self.close()
            return True
        else:
            if self.isSignalConnected(self.submit_dialog_button, 'clicked()'):
                self.submit_dialog_button.clicked.disconnect()
            self.close()
            return False

    def isSignalConnected(self, obj, name):
        index = obj.metaObject().indexOfMethod(name)
        if index > -1:
            method = obj.metaObject().method(index)
            if method:
                return obj.isSignalConnected(method)
        return False