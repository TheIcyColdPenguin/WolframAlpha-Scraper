# Imports
from PyQt5.QtCore import QObject, pyqtSignal, QRunnable, pyqtSlot
from traceback import print_exc, format_exc
from sys import exc_info

class WorkerSignals(QObject):
    '''
    This class handles the signals for the
    worker objects that will be created.
    '''
    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)
    progress = pyqtSignal(int)


class Worker(QRunnable):
    '''
    This class uses multi-threading using QThreading
    '''
    def __init__(self, fn, *args, **kwargs):
        '''
        Initialising the class.
        This is called whenever an object of this class is created.
        Parameters:
        fn (function): The function which will be put on a separate thread
        '''
        super(Worker, self).__init__()

        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

        self.kwargs['progress_callback'] = self.signals.progress

    @pyqtSlot()
    def run(self):
        '''
        Running the thread and signaling the GUI
        '''
        try:
            result = self.fn()
        except Exception:
            print_exc()
            exctype, value = exc_info()[:2]
            self.signals.error.emit((exctype, value, format_exc()))
        else:
            self.signals.result.emit(result)
        finally:
            self.signals.finished.emit()
