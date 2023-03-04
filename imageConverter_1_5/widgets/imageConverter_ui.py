# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'imageConverter.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_imageConverter(object):
    def setupUi(self, imageConverter):
        if not imageConverter.objectName():
            imageConverter.setObjectName(u"imageConverter")
        imageConverter.resize(338, 418)
        self.centralwidget = QWidget(imageConverter)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.sett_le = QLineEdit(self.centralwidget)
        self.sett_le.setObjectName(u"sett_le")

        self.horizontalLayout.addWidget(self.sett_le)

        self.browsSet_btn = QPushButton(self.centralwidget)
        self.browsSet_btn.setObjectName(u"browsSet_btn")
        self.browsSet_btn.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout.addWidget(self.browsSet_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.files_ly = QVBoxLayout()
        self.files_ly.setObjectName(u"files_ly")

        self.verticalLayout.addLayout(self.files_ly)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.rezo_cbb = QComboBox(self.centralwidget)
        self.rezo_cbb.setObjectName(u"rezo_cbb")

        self.horizontalLayout_2.addWidget(self.rezo_cbb)

        self.ext_cbb = QComboBox(self.centralwidget)
        self.ext_cbb.setObjectName(u"ext_cbb")

        self.horizontalLayout_2.addWidget(self.ext_cbb)

        self.start_btn = QPushButton(self.centralwidget)
        self.start_btn.setObjectName(u"start_btn")

        self.horizontalLayout_2.addWidget(self.start_btn)

        self.horizontalLayout_2.setStretch(2, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalLayout.setStretch(1, 1)
        imageConverter.setCentralWidget(self.centralwidget)

        self.retranslateUi(imageConverter)

        QMetaObject.connectSlotsByName(imageConverter)
    # setupUi

    def retranslateUi(self, imageConverter):
        imageConverter.setWindowTitle(QCoreApplication.translate("imageConverter", u"Image Converter", None))
        self.browsSet_btn.setText(QCoreApplication.translate("imageConverter", u"...", None))
        self.start_btn.setText(QCoreApplication.translate("imageConverter", u"Start", None))
    # retranslateUi

