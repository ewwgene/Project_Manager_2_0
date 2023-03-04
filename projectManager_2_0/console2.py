import sys

from PySide2.QtCore import Signal, Slot, QProcess, QTextCodec
from PySide2 import QtCore, QtWidgets
# import jtextfsm as textfsm


class Widget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.process = QtCore.QProcess(self)
        self.process.setProgram("dirb")
        self.process.setProcessChannelMode(QtCore.QProcess.MergedChannels)

        self.lineedit = QtWidgets.QLineEdit("http://webscantest.com")
        self.button = QtWidgets.QPushButton("Start")
        self.textedit = QtWidgets.QTextEdit(readOnly=True)

        lay = QtWidgets.QGridLayout(self)
        lay.addWidget(self.lineedit, 0, 0)
        lay.addWidget(self.button, 0, 1)
        lay.addWidget(self.textedit, 1, 0, 1, 2)

        self.button.clicked.connect(self.on_clicked)
        self.process.readyReadStandardOutput.connect(self.on_readyReadStandardOutput)
        self.process.finished.connect(self.on_finished)
        print('dcdcdcd')

    @QtCore.Slot()
    def on_clicked(self):
        print('dcdcdcd')
        if self.button.text() == "Start":
            print('dcdcdcd')
            self.textedit.clear()
            print('dcdcdcd')
            self.process.setArguments([self.lineedit.text()])
            print('dcdcdcd')
            self.process.start()
            print('dcdcdcd')
            self.button.setText("Stop")
            print('dcdcdcd')
        elif self.button.text() == "Stop":
            print('dcdcdcd')
            self.process.kill()
            print('dcdcdcd')

    @QtCore.Slot()
    def on_readyReadStandardOutput(self):
        text = self.process.readAllStandardOutput().data().decode()
        print('dcdcdcd')
        self.textedit.append(text)
        print('dcdcdcd')

    @QtCore.Slot()
    def on_finished(self):
        self.button.setText("Start")
        print('dcdcdcd')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = Widget()
    w.show()
    sys.exit(app.exec_())