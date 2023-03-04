# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QUICK_2.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(397, 386)
        self.centralwidget = QWidget(Form)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.checkBox_H = QCheckBox(self.centralwidget)
        self.checkBox_H.setObjectName(u"checkBox_H")

        self.verticalLayout.addWidget(self.checkBox_H)

        self.H_in1 = QSpinBox(self.centralwidget)
        self.H_in1.setObjectName(u"H_in1")
        self.H_in1.setMinimumSize(QSize(70, 0))
        self.H_in1.setMaximum(9999)

        self.verticalLayout.addWidget(self.H_in1)

        self.H_in2 = QSpinBox(self.centralwidget)
        self.H_in2.setObjectName(u"H_in2")
        self.H_in2.setMinimumSize(QSize(70, 0))
        self.H_in2.setMaximum(9999)

        self.verticalLayout.addWidget(self.H_in2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.Paint_lyo = QVBoxLayout()
        self.Paint_lyo.setObjectName(u"Paint_lyo")

        self.gridLayout.addLayout(self.Paint_lyo, 0, 1, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, 0, -1)
        self.checkBox_V = QCheckBox(self.centralwidget)
        self.checkBox_V.setObjectName(u"checkBox_V")

        self.verticalLayout_2.addWidget(self.checkBox_V)

        self.V_in1 = QSpinBox(self.centralwidget)
        self.V_in1.setObjectName(u"V_in1")
        self.V_in1.setMaximumSize(QSize(70, 16777215))
        self.V_in1.setMaximum(9999)

        self.verticalLayout_2.addWidget(self.V_in1)

        self.V_in2 = QSpinBox(self.centralwidget)
        self.V_in2.setObjectName(u"V_in2")
        self.V_in2.setMaximumSize(QSize(70, 16777215))
        self.V_in2.setMaximum(9999)

        self.verticalLayout_2.addWidget(self.V_in2)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 1, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)

        self.Z_in1 = QSpinBox(self.centralwidget)
        self.Z_in1.setObjectName(u"Z_in1")
        self.Z_in1.setMinimumSize(QSize(0, 0))
        self.Z_in1.setMaximumSize(QSize(50, 16777215))
        self.Z_in1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.Z_in1.setMaximum(9999)

        self.verticalLayout_3.addWidget(self.Z_in1)

        self.Z_in2 = QSpinBox(self.centralwidget)
        self.Z_in2.setObjectName(u"Z_in2")
        self.Z_in2.setMinimumSize(QSize(70, 0))
        self.Z_in2.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.Z_in2.setMaximum(9999)

        self.verticalLayout_3.addWidget(self.Z_in2)


        self.gridLayout.addLayout(self.verticalLayout_3, 1, 0, 1, 1)

        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)

        self.verticalLayout_4.addLayout(self.gridLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Clear_btn = QPushButton(self.centralwidget)
        self.Clear_btn.setObjectName(u"Clear_btn")
        self.Clear_btn.setMinimumSize(QSize(0, 50))

        self.horizontalLayout.addWidget(self.Clear_btn)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        Form.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.H_in1, self.H_in2)
        QWidget.setTabOrder(self.H_in2, self.V_in1)
        QWidget.setTabOrder(self.V_in1, self.V_in2)
        QWidget.setTabOrder(self.V_in2, self.Z_in1)
        QWidget.setTabOrder(self.Z_in1, self.Z_in2)
        QWidget.setTabOrder(self.Z_in2, self.checkBox_H)
        QWidget.setTabOrder(self.checkBox_H, self.checkBox_V)
        QWidget.setTabOrder(self.checkBox_V, self.Clear_btn)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"MainWindow", None))
        self.checkBox_H.setText(QCoreApplication.translate("Form", u"Vertical", None))
        self.checkBox_V.setText(QCoreApplication.translate("Form", u"Horizontal", None))
        self.label.setText(QCoreApplication.translate("Form", u"On floor:", None))
        self.Clear_btn.setText(QCoreApplication.translate("Form", u"CLEAR", None))
    # retranslateUi

