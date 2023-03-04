from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
            MainWindow.resize(800, 600)
            self.centralwidget = QWidget(MainWindow)
            self.centralwidget.setObjectName(u"centralwidget")
            self.verticalLayout = QVBoxLayout(self.centralwidget)
            self.verticalLayout.setObjectName(u"verticalLayout")
            self.textEdit = QTextEdit(self.centralwidget)
            self.textEdit.setObjectName(u"textEdit")
            font = QFont()
            font.setPointSize(12)
            self.textEdit.setFont(font)
            self.textEdit.setReadOnly(True)

            self.verticalLayout.addWidget(self.textEdit)

            MainWindow.setCentralWidget(self.centralwidget)
            self.statusbar = QStatusBar(MainWindow)
            self.statusbar.setObjectName(u"statusbar")
            MainWindow.setStatusBar(self.statusbar)

            self.retranslateUi(MainWindow)

            QMetaObject.connectSlotsByName(MainWindow)
            # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        # retranslateUi