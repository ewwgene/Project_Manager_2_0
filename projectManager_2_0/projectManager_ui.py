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

import source_rc

class Ui_projectManager(object):
    def setupUi(self, projectManager):
        if not projectManager.objectName():
            projectManager.setObjectName(u"projectManager")
        projectManager.resize(750, 675)
        self.centralwidget = QWidget(projectManager)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, 0, 6)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.projectList_lyo = QVBoxLayout()
        self.projectList_lyo.setSpacing(5)
        self.projectList_lyo.setObjectName(u"projectList_lyo")
        self.projectList_lyo.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, -1, 0, -1)
        self.expand_btn = QPushButton(self.centralwidget)
        self.expand_btn.setObjectName(u"expand_btn")
        self.expand_btn.setMinimumSize(QSize(0, 25))
        self.expand_btn.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_6.addWidget(self.expand_btn)

        self.newClient_btn = QPushButton(self.centralwidget)
        self.newClient_btn.setObjectName(u"newClient_btn")
        self.newClient_btn.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_6.addWidget(self.newClient_btn)

        self.toolButton_btn = QPushButton(self.centralwidget)
        self.toolButton_btn.setObjectName(u"toolButton_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_btn.sizePolicy().hasHeightForWidth())
        self.toolButton_btn.setSizePolicy(sizePolicy)
        self.toolButton_btn.setMinimumSize(QSize(25, 25))
        self.toolButton_btn.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_6.addWidget(self.toolButton_btn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)


        self.projectList_lyo.addLayout(self.horizontalLayout_6)


        self.verticalLayout_4.addLayout(self.projectList_lyo)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 6, -1, -1)
        self.textBrowser_txt = QTextBrowser(self.centralwidget)
        self.textBrowser_txt.setObjectName(u"textBrowser_txt")
        self.textBrowser_txt.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setFamily(u"Terminus (TTF) for Windows")
        self.textBrowser_txt.setFont(font)

        self.verticalLayout_2.addWidget(self.textBrowser_txt)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(200, 16777215))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(9, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 4, -1, 10)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.pix_lbl = QLabel(self.widget)
        self.pix_lbl.setObjectName(u"pix_lbl")
        self.pix_lbl.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.pix_lbl)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.create_btn = QPushButton(self.widget)
        self.create_btn.setObjectName(u"create_btn")
        self.create_btn.setMinimumSize(QSize(0, 0))
        font1 = QFont()
        font1.setFamily(u"MS Shell Dlg 2")
        self.create_btn.setFont(font1)

        self.verticalLayout.addWidget(self.create_btn)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.templateEditor_btn = QPushButton(self.widget)
        self.templateEditor_btn.setObjectName(u"templateEditor_btn")

        self.horizontalLayout_2.addWidget(self.templateEditor_btn)

        self.templateCheckEditor_btn = QPushButton(self.widget)
        self.templateCheckEditor_btn.setObjectName(u"templateCheckEditor_btn")

        self.horizontalLayout_2.addWidget(self.templateCheckEditor_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.groupBox = QGroupBox(self.widget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 0))
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setSpacing(9)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(9, 9, 9, 6)
        self.info_lbl = QLabel(self.groupBox)
        self.info_lbl.setObjectName(u"info_lbl")
        self.info_lbl.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.info_lbl)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.OBR_lbl = QLabel(self.groupBox)
        self.OBR_lbl.setObjectName(u"OBR_lbl")
        self.OBR_lbl.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_3.addWidget(self.OBR_lbl)

        self.TZ_lbl = QLabel(self.groupBox)
        self.TZ_lbl.setObjectName(u"TZ_lbl")
        self.TZ_lbl.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_3.addWidget(self.TZ_lbl)

        self.TPR_lbl = QLabel(self.groupBox)
        self.TPR_lbl.setObjectName(u"TPR_lbl")
        self.TPR_lbl.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_3.addWidget(self.TPR_lbl)

        self.PDF_lbl = QLabel(self.groupBox)
        self.PDF_lbl.setObjectName(u"PDF_lbl")
        self.PDF_lbl.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_3.addWidget(self.PDF_lbl)

        self.URL_lbl = QLabel(self.groupBox)
        self.URL_lbl.setObjectName(u"URL_lbl")
        self.URL_lbl.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_3.addWidget(self.URL_lbl)

        self.LOC_lbl = QLabel(self.groupBox)
        self.LOC_lbl.setObjectName(u"LOC_lbl")
        self.LOC_lbl.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_3.addWidget(self.LOC_lbl)

        self.edit_btn = QPushButton(self.groupBox)
        self.edit_btn.setObjectName(u"edit_btn")
        self.edit_btn.setMaximumSize(QSize(16777215, 16777215))
        self.edit_btn.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_3.addWidget(self.edit_btn)


        self.verticalLayout.addWidget(self.groupBox)

        self.settings_btn = QPushButton(self.widget)
        self.settings_btn.setObjectName(u"settings_btn")
        self.settings_btn.setMinimumSize(QSize(0, 0))

        self.verticalLayout.addWidget(self.settings_btn)


        self.horizontalLayout.addWidget(self.widget)

        self.minimize_btn = QPushButton(self.centralwidget)
        self.minimize_btn.setObjectName(u"minimize_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.minimize_btn.sizePolicy().hasHeightForWidth())
        self.minimize_btn.setSizePolicy(sizePolicy1)
        self.minimize_btn.setMinimumSize(QSize(14, 0))
        self.minimize_btn.setMaximumSize(QSize(14, 1000))
        self.minimize_btn.setSizeIncrement(QSize(0, 0))
        font2 = QFont()
        font2.setFamily(u"MS Shell Dlg 2")
        font2.setPointSize(8)
        self.minimize_btn.setFont(font2)
        self.minimize_btn.setLayoutDirection(Qt.RightToLeft)
        self.minimize_btn.setAutoFillBackground(False)
        self.minimize_btn.setAutoDefault(False)
        self.minimize_btn.setFlat(True)

        self.horizontalLayout.addWidget(self.minimize_btn)

        projectManager.setCentralWidget(self.centralwidget)

        self.retranslateUi(projectManager)

        self.minimize_btn.setDefault(False)


        QMetaObject.connectSlotsByName(projectManager)
    # setupUi

    def retranslateUi(self, projectManager):
        projectManager.setWindowTitle(QCoreApplication.translate("projectManager", u"Project Manager 2.0", None))
        self.expand_btn.setText(QCoreApplication.translate("projectManager", u"u25BC", None))
        self.newClient_btn.setText(QCoreApplication.translate("projectManager", u"Update", None))
        self.toolButton_btn.setText(QCoreApplication.translate("projectManager", u"...", None))
        self.textBrowser_txt.setHtml(QCoreApplication.translate("projectManager", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Terminus (TTF) for Windows'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.pix_lbl.setText(QCoreApplication.translate("projectManager", u"r", None))
        self.create_btn.setText(QCoreApplication.translate("projectManager", u"Create Project", None))
        self.templateEditor_btn.setText(QCoreApplication.translate("projectManager", u"Template Editor", None))
        self.templateCheckEditor_btn.setText(QCoreApplication.translate("projectManager", u"Check Editor", None))
        self.groupBox.setTitle(QCoreApplication.translate("projectManager", u"Info", None))
        self.info_lbl.setText(QCoreApplication.translate("projectManager", u"TextLabel", None))
        self.OBR_lbl.setText(QCoreApplication.translate("projectManager", u"\u041e\u0411\u0420", None))
        self.TZ_lbl.setText(QCoreApplication.translate("projectManager", u"T3", None))
        self.TPR_lbl.setText(QCoreApplication.translate("projectManager", u"\u0422\u041f\u0420", None))
        self.PDF_lbl.setText(QCoreApplication.translate("projectManager", u"PDF", None))
        self.URL_lbl.setText(QCoreApplication.translate("projectManager", u"URL", None))
        self.LOC_lbl.setText(QCoreApplication.translate("projectManager", u"LOC", None))
        self.edit_btn.setText(QCoreApplication.translate("projectManager", u"Edit", None))
        self.settings_btn.setText(QCoreApplication.translate("projectManager", u" Settings", None))
        self.minimize_btn.setText(QCoreApplication.translate("projectManager", u"<<", None))
    # retranslateUi

