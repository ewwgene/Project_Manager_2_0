from PySide2 import QtWidgets, QtCore

class PYQT_Process():
    def __init__(self, qmainwindow : QtWidgets.QMainWindow, QTextBrowser : QtWidgets.QTextBrowser, script_for_process : str):
        self.qmainwindow = qmainwindow
        # self.qtextedit = qtextedit
        self.script = script_for_process
        self.textBrowser_txt = QTextBrowser

    def begin_process(self):
        print('Connecting Process')
        self.process = QtCore.QProcess(self.qmainwindow)
        self.process.readyRead.connect(lambda: self.stdoutReady())
        # self.process.readyReadStandardOutput.connect(self.stdoutReady)
        # self.process.readyReadStandardError.connect(lambda: self.stderrReady())
        self.process.started.connect(lambda: print('Started!'))
        self.process.finished.connect(lambda: print('Finished!'))

        print('Starting process')
        self.process.start('python', [self.script])

    def append(self, text):
        cursor = self.qtexedit.textCursor()
        cursor.movePosition(cursor.End)
        cursor.insertText(text)
        # self.qmainwindow.output.ensureCursorVisible()

    def stdoutReady(self):
        text = str(self.process.readAllStandardOutput())
        # print('out')
        # print(text.strip())
        self.qtextedit.append(text)

    def stderrReady(self):
        text = str(self.process.readAllStandardError())
        # print('error')
        # print(text.strip())
        self.qtextedit.append(text)