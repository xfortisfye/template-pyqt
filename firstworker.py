from PyQt5 import QtCore

class WorkerSignals(QtCore.QObject):
    """
    default flags. Can be customised as any other variables
    """
    finished = QtCore.pyqtSignal()
    error = QtCore.pyqtSignal(tuple)
    result = QtCore.pyqtSignal(object)
    progress = QtCore.pyqtSignal(int)
    
    firstsignal = QtCore.pyqtSignal(str)
    secondsignal = QtCore.pyqtSignal(str)

class FirstWorker(QtCore.QThread):
    def __init__(self, firstvar, secondvar):
        super(FirstWorker, self).__init__()
        # Store constructor arguments (re-used for processing)
        self.signals = WorkerSignals()
        self.firstvar = firstvar
        self.secondvar = secondvar

    @QtCore.pyqtSlot()
    def run(self):
        while True:
            value1 = self.firstvar + "andy"
            value2 = self.secondvar + "mars"
            self.signals.firstsignal.emit(value1)
            self.signals.secondsignal.emit(value2)


# class Worker(QtCore.QRunnable):
#     def __init__(self, fn, *args, **kwargs):
#         super(Worker, self).__init__()

#         # Store constructor arguments (re-used for processing)
#         self.fn = fn
#         self.args = args
#         self.kwargs = kwargs
#         self.signals = WorkerSignals()

#         # Add the callback to our kwargs
#         # self.kwargs['progress_callback'] = self.signals.progress

#     @QtCore.pyqtSlot()
#     def run(self):
#         '''
#         Initialise the runner function with passed args, kwargs.
#         '''

#         # Retrieve args/kwargs here; and fire processing using them
#         try:
#             result = self.fn(*self.args, **self.kwargs)
#         except:
#             traceback.print_exc()
#             exctype, value = sys.exc_info()[:2]
#             self.signals.error.emit((exctype, value, traceback.format_exc()))
#         else:
#             self.signals.result.emit(result)  # Return the result of the processing
#         finally:
#             self.signals.finished.emit()  # Done