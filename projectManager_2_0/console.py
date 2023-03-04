#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from PySide2.QtCore import Signal, Slot, QProcess, QTextCodec
from PySide2.QtGui import QTextCursor
from PySide2.QtWidgets import QApplication, QPlainTextEdit


class ProcessOutputReader(QProcess):
    produce_output = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent=parent)

        # merge stderr channel into stdout channel
        self.setProcessChannelMode(QProcess.MergedChannels)

        # prepare decoding process' output to Unicode
        codec = QTextCodec.codecForLocale()
        self._decoder_stdout = codec.makeDecoder()
        # only necessary when stderr channel isn't merged into stdout:
        # self._decoder_stderr = codec.makeDecoder()

        self.readyReadStandardOutput.connect(self._ready_read_standard_output)
        # only necessary when stderr channel isn't merged into stdout:
        # self.readyReadStandardError.connect(self._ready_read_standard_error)
        print('sdfsdfsdfsdf')


    @Slot()
    def _ready_read_standard_output(self):
        raw_bytes = self.readAllStandardOutput()
        text = self._decoder_stdout.toUnicode(raw_bytes)
        self.produce_output.emit(text)
        print('sdfsdfsdfsdf')

    # only necessary when stderr channel isn't merged into stdout:
    # @pyqtSlot()
    # def _ready_read_standard_error(self):
    #     raw_bytes = self.readAllStandardError()
    #     text = self._decoder_stderr.toUnicode(raw_bytes)
    #     self.produce_output.emit(text)


class MyConsole(QPlainTextEdit):

    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.setReadOnly(True)
        self.setMaximumBlockCount(10000)  # limit console to 10000 lines

        self._cursor_output = self.textCursor()
        print('sdfsdfsdfsdf')

    @Slot(str)
    def append_output(self, text):
        self._cursor_output.insertText(text)
        self.scroll_to_last_line()
        print('sdfsdfsdfsdf')

    def scroll_to_last_line(self):
        cursor = self.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.movePosition(QTextCursor.Up if cursor.atBlockStart() else
                            QTextCursor.StartOfLine)
        self.setTextCursor(cursor)
        print('sdfsdfsdfsdf')


# create the application instance
app = QApplication(sys.argv)

# create a process output reader
reader = ProcessOutputReader()

# create a console and connect the process output reader to it
console = MyConsole()
reader.produce_output.connect(console.append_output)

reader.start('python3', ['-u', 'test.py'])  # start the process
console.show()                              # make the console visible
app.exec_()                                 # run the PyQt main loop
