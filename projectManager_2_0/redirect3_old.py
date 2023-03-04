from PySide2 import QtWidgets, QtCore
from redirect_ui import Ui_MainWindow

def p(x):
    print (x)

class MainWindow(QtWidgets.QMainWindow):
    # def __init__(self, parent=None):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        print('Connecting process')
        self.process = QtCore.QProcess(self)
        self.process.readyRead.connect(
        self.stdoutReady)  # alternative to use print('',flush=True) instead of stdout

        ###############
        # self.process.readyReadStandardOutput.connect(self.stdoutReady)
        # self.process.readyReadStandardError.connect(self.stderrReady)
        ###############
        self.process.started.connect(lambda: p('Started!'))
        self.process.finished.connect(lambda: p('Finished!'))

        print('Starting process')
        self.process.start('python', ['speak.py'])


    def append(self, text):
        cursor = self.ui.textEdit.textCursor()
        cursor.movePosition(cursor.End)
        cursor.insertText(text)
        ###############
        # self.output.ensureCursorVisible()

    def stdoutReady(self):
        text = str(self.process.readAllStandardOutput())
        print (text.strip())
        self.append('\n' + text)

    def stderrReady(self):
        text = str(self.process.readAllStandardError())
        ###############
        # print (text.strip())
        ###############
        self.append(text)

def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()