# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'projectManager.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import source_qrc

class Ui_projectManager(object):
    def setupUi(self, projectManager):
        if not projectManager.objectName():
            projectManager.setObjectName(u"projectManager")
        projectManager.resize(779, 476)
        self.centralwidget = QWidget(projectManager)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.projectList_lyo = QVBoxLayout()
        self.projectList_lyo.setObjectName(u"projectList_lyo")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.expand_btn = QPushButton(self.centralwidget)
        self.expand_btn.setObjectName(u"expand_btn")
        self.expand_btn.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_6.addWidget(self.expand_btn)

        self.newClient_btn = QPushButton(self.centralwidget)
        self.newClient_btn.setObjectName(u"newClient_btn")

        self.horizontalLayout_6.addWidget(self.newClient_btn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(200, 50))
        self.label.setMaximumSize(QSize(200, 50))
        self.label.setStyleSheet(u"image: url(:/newPrefix/KAMEA.png);")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)

        self.horizontalLayout_6.addWidget(self.label)


        self.projectList_lyo.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_2.addLayout(self.projectList_lyo)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.create_btn = QPushButton(self.centralwidget)
        self.create_btn.setObjectName(u"create_btn")
        self.create_btn.setMinimumSize(QSize(200, 0))

        self.verticalLayout.addWidget(self.create_btn)

        self.templateEditor_btn = QPushButton(self.centralwidget)
        self.templateEditor_btn.setObjectName(u"templateEditor_btn")

        self.verticalLayout.addWidget(self.templateEditor_btn)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 0))
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.edit_btn = QPushButton(self.groupBox)
        self.edit_btn.setObjectName(u"edit_btn")
        self.edit_btn.setMaximumSize(QSize(100, 16777215))
        self.edit_btn.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_3.addWidget(self.edit_btn)

        self.info_lbl = QLabel(self.groupBox)
        self.info_lbl.setObjectName(u"info_lbl")
        self.info_lbl.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.info_lbl)


        self.verticalLayout.addWidget(self.groupBox)

        self.settings_btn = QPushButton(self.centralwidget)
        self.settings_btn.setObjectName(u"settings_btn")

        self.verticalLayout.addWidget(self.settings_btn)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        projectManager.setCentralWidget(self.centralwidget)

        self.retranslateUi(projectManager)

        QMetaObject.connectSlotsByName(projectManager)
    # setupUi

    def retranslateUi(self, projectManager):
        projectManager.setWindowTitle(QCoreApplication.translate("projectManager", u"ProjectManager", None))
        self.expand_btn.setText(QCoreApplication.translate("projectManager", u"\u23f7", None))
        self.newClient_btn.setText(QCoreApplication.translate("projectManager", u"Update", None))
        self.label.setText("")
        self.create_btn.setText(QCoreApplication.translate("projectManager", u"Create Project", None))
        self.templateEditor_btn.setText(QCoreApplication.translate("projectManager", u"Template Editor", None))
        self.groupBox.setTitle(QCoreApplication.translate("projectManager", u"Info", None))
        self.edit_btn.setText(QCoreApplication.translate("projectManager", u"Edit", None))
        self.info_lbl.setText(QCoreApplication.translate("projectManager", u"TextLabel", None))
        self.settings_btn.setText(QCoreApplication.translate("projectManager", u"Settings", None))
    # retranslateUi

