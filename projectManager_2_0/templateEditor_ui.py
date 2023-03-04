# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'templateEditor.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_templateEditor(object):
    def setupUi(self, templateEditor):
        if not templateEditor.objectName():
            templateEditor.setObjectName(u"templateEditor")
        templateEditor.resize(406, 551)
        self.verticalLayout = QVBoxLayout(templateEditor)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.add_btn = QPushButton(templateEditor)
        self.add_btn.setObjectName(u"add_btn")
        self.add_btn.setMinimumSize(QSize(30, 30))
        self.add_btn.setMaximumSize(QSize(30, 30))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.add_btn.setFont(font)

        self.horizontalLayout_2.addWidget(self.add_btn)

        self.remove_btn = QPushButton(templateEditor)
        self.remove_btn.setObjectName(u"remove_btn")
        self.remove_btn.setMinimumSize(QSize(30, 30))
        self.remove_btn.setMaximumSize(QSize(30, 30))
        self.remove_btn.setFont(font)

        self.horizontalLayout_2.addWidget(self.remove_btn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.save_btn = QPushButton(templateEditor)
        self.save_btn.setObjectName(u"save_btn")

        self.horizontalLayout.addWidget(self.save_btn)

        self.close_btn = QPushButton(templateEditor)
        self.close_btn.setObjectName(u"close_btn")

        self.horizontalLayout.addWidget(self.close_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(templateEditor)

        QMetaObject.connectSlotsByName(templateEditor)
    # setupUi

    def retranslateUi(self, templateEditor):
        templateEditor.setWindowTitle(QCoreApplication.translate("templateEditor", u"Form", None))
        self.add_btn.setText(QCoreApplication.translate("templateEditor", u"+", None))
        self.remove_btn.setText(QCoreApplication.translate("templateEditor", u"-", None))
        self.save_btn.setText(QCoreApplication.translate("templateEditor", u"Save", None))
        self.close_btn.setText(QCoreApplication.translate("templateEditor", u"Close", None))
    # retranslateUi

