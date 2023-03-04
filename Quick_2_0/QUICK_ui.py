# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QUICK.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import sour_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(456, 400)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(0, 300))
        Form.setMaximumSize(QSize(600, 450))
        self.verticalLayout_5 = QVBoxLayout(Form)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_7)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setContentsMargins(0, -1, 0, 0)
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(75, 35))
        self.label.setStyleSheet(u"image: url(:/newPrefix/KAMEA.png);")
        self.label.setTextFormat(Qt.RichText)
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_8.addWidget(self.label)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_3)


        self.gridLayout.addLayout(self.verticalLayout_8, 1, 3, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.V_Center_Out = QLabel(Form)
        self.V_Center_Out.setObjectName(u"V_Center_Out")
        self.V_Center_Out.setMinimumSize(QSize(100, 0))
        self.V_Center_Out.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.V_Center_Out)

        self.V_Size_Out = QLabel(Form)
        self.V_Size_Out.setObjectName(u"V_Size_Out")
        self.V_Size_Out.setMinimumSize(QSize(100, 0))
        self.V_Size_Out.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.V_Size_Out)


        self.gridLayout.addLayout(self.verticalLayout_3, 2, 3, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.H_Center_Out = QLabel(Form)
        self.H_Center_Out.setObjectName(u"H_Center_Out")
        self.H_Center_Out.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.H_Center_Out)

        self.H_Size_Out = QLabel(Form)
        self.H_Size_Out.setObjectName(u"H_Size_Out")
        self.H_Size_Out.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.H_Size_Out)


        self.gridLayout.addLayout(self.verticalLayout, 1, 2, 1, 1)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(-1, -1, 15, -1)
        self.radioButton_2 = QRadioButton(Form)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setMinimumSize(QSize(25, 0))
        self.radioButton_2.setMaximumSize(QSize(16777215, 16777215))
        self.radioButton_2.setLayoutDirection(Qt.RightToLeft)

        self.verticalLayout_9.addWidget(self.radioButton_2)


        self.gridLayout.addLayout(self.verticalLayout_9, 2, 0, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.V_in1 = QSpinBox(Form)
        self.V_in1.setObjectName(u"V_in1")
        self.V_in1.setMinimumSize(QSize(100, 0))
        self.V_in1.setMaximumSize(QSize(100, 16777215))
        self.V_in1.setAlignment(Qt.AlignCenter)
        self.V_in1.setMaximum(99999)

        self.verticalLayout_4.addWidget(self.V_in1)

        self.V_in2 = QSpinBox(Form)
        self.V_in2.setObjectName(u"V_in2")
        self.V_in2.setMinimumSize(QSize(100, 0))
        self.V_in2.setMaximumSize(QSize(100, 16777215))
        self.V_in2.setAlignment(Qt.AlignCenter)
        self.V_in2.setMaximum(99999)

        self.verticalLayout_4.addWidget(self.V_in2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)


        self.gridLayout.addLayout(self.verticalLayout_4, 3, 2, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, -1, -1, 0)
        self.H_in1 = QSpinBox(Form)
        self.H_in1.setObjectName(u"H_in1")
        self.H_in1.setMinimumSize(QSize(100, 0))
        self.H_in1.setMaximumSize(QSize(100, 16777215))
        self.H_in1.setAlignment(Qt.AlignCenter)
        self.H_in1.setMaximum(99999)

        self.verticalLayout_2.addWidget(self.H_in1)

        self.H_in2 = QSpinBox(Form)
        self.H_in2.setObjectName(u"H_in2")
        self.H_in2.setMinimumSize(QSize(50, 0))
        self.H_in2.setMaximumSize(QSize(100, 16777215))
        self.H_in2.setAlignment(Qt.AlignCenter)
        self.H_in2.setMaximum(99999)

        self.verticalLayout_2.addWidget(self.H_in2)


        self.gridLayout.addLayout(self.verticalLayout_2, 2, 1, 1, 1)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(100, 0))
        self.label_2.setMaximumSize(QSize(100, 16777215))
        font = QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)

        self.Quick_btn = QPushButton(Form)
        self.Quick_btn.setObjectName(u"Quick_btn")
        self.Quick_btn.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.Quick_btn, 2, 2, 1, 1)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, -1, 15, -1)
        self.radioButton = QRadioButton(Form)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setMinimumSize(QSize(0, 50))
        self.radioButton.setLayoutDirection(Qt.RightToLeft)

        self.verticalLayout_7.addWidget(self.radioButton)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_4)


        self.gridLayout.addLayout(self.verticalLayout_7, 3, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 4, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_6)

        self.Clear_btn = QPushButton(Form)
        self.Clear_btn.setObjectName(u"Clear_btn")
        self.Clear_btn.setMinimumSize(QSize(0, 50))

        self.verticalLayout_5.addWidget(self.Clear_btn)

        QWidget.setTabOrder(self.H_in1, self.H_in2)
        QWidget.setTabOrder(self.H_in2, self.V_in1)
        QWidget.setTabOrder(self.V_in1, self.V_in2)
        QWidget.setTabOrder(self.V_in2, self.Quick_btn)
        QWidget.setTabOrder(self.Quick_btn, self.Clear_btn)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
        self.V_Center_Out.setText(QCoreApplication.translate("Form", u"Center", None))
        self.V_Size_Out.setText(QCoreApplication.translate("Form", u"Size", None))
        self.H_Center_Out.setText(QCoreApplication.translate("Form", u"Center", None))
        self.H_Size_Out.setText(QCoreApplication.translate("Form", u"Size", None))
        self.radioButton_2.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.Quick_btn.setText(QCoreApplication.translate("Form", u"QUICK", None))
        self.radioButton.setText("")
        self.Clear_btn.setText(QCoreApplication.translate("Form", u"CLEAR", None))
    # retranslateUi

