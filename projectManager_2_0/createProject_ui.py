# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'createProject.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_createDialog(object):
    def setupUi(self, createDialog):
        if not createDialog.objectName():
            createDialog.setObjectName(u"createDialog")
        createDialog.resize(657, 660)
        self.gridLayout_2 = QGridLayout(createDialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.name_lbl = QLineEdit(createDialog)
        self.name_lbl.setObjectName(u"name_lbl")

        self.gridLayout_2.addWidget(self.name_lbl, 4, 1, 1, 2)

        self.ObrCheckBox_chb = QCheckBox(createDialog)
        self.ObrCheckBox_chb.setObjectName(u"ObrCheckBox_chb")
        self.ObrCheckBox_chb.setTristate(False)

        self.gridLayout_2.addWidget(self.ObrCheckBox_chb, 10, 2, 1, 1)

        self.label_2 = QLabel(createDialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_2.setMargin(0)
        self.label_2.setIndent(-1)

        self.gridLayout_2.addWidget(self.label_2, 6, 0, 1, 1)

        self.tzPathServer_lbl = QLineEdit(createDialog)
        self.tzPathServer_lbl.setObjectName(u"tzPathServer_lbl")
        self.tzPathServer_lbl.setMinimumSize(QSize(0, 0))
        self.tzPathServer_lbl.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.tzPathServer_lbl, 9, 1, 1, 1)

        self.label_4 = QLabel(createDialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)

        self.label_9 = QLabel(createDialog)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_9, 8, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.contract_cbb = QComboBox(createDialog)
        self.contract_cbb.setObjectName(u"contract_cbb")
        self.contract_cbb.setMinimumSize(QSize(150, 0))
        self.contract_cbb.setMaximumSize(QSize(150, 16777215))

        self.gridLayout.addWidget(self.contract_cbb, 1, 0, 1, 1)

        self.client_cbb = QComboBox(createDialog)
        self.client_cbb.setObjectName(u"client_cbb")
        self.client_cbb.setMinimumSize(QSize(150, 0))
        self.client_cbb.setMaximumSize(QSize(150, 16777215))

        self.gridLayout.addWidget(self.client_cbb, 0, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.contract_lne = QLineEdit(createDialog)
        self.contract_lne.setObjectName(u"contract_lne")
        self.contract_lne.setMinimumSize(QSize(0, 0))
        self.contract_lne.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_3.addWidget(self.contract_lne)

        self.label_5 = QLabel(createDialog)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_3.addWidget(self.label_5)

        self.subContract_lne = QLineEdit(createDialog)
        self.subContract_lne.setObjectName(u"subContract_lne")

        self.horizontalLayout_3.addWidget(self.subContract_lne)

        self.date_dte = QDateEdit(createDialog)
        self.date_dte.setObjectName(u"date_dte")
        self.date_dte.setMinimumSize(QSize(85, 0))
        self.date_dte.setCalendarPopup(True)

        self.horizontalLayout_3.addWidget(self.date_dte)


        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 1, 1, 1)

        self.client_lne = QLineEdit(createDialog)
        self.client_lne.setObjectName(u"client_lne")

        self.gridLayout.addWidget(self.client_lne, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 2, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 1, 1, 2, 2)

        self.objectName_lbl = QLineEdit(createDialog)
        self.objectName_lbl.setObjectName(u"objectName_lbl")
        self.objectName_lbl.setMinimumSize(QSize(0, 0))
        self.objectName_lbl.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.objectName_lbl, 3, 1, 1, 2)

        self.label = QLabel(createDialog)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label, 4, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.create_btn = QPushButton(createDialog)
        self.create_btn.setObjectName(u"create_btn")
        self.create_btn.setEnabled(True)

        self.horizontalLayout.addWidget(self.create_btn)

        self.cancel_btn = QPushButton(createDialog)
        self.cancel_btn.setObjectName(u"cancel_btn")

        self.horizontalLayout.addWidget(self.cancel_btn)


        self.gridLayout_2.addLayout(self.horizontalLayout, 13, 0, 1, 3)

        self.tprPathServer_lbl = QLineEdit(createDialog)
        self.tprPathServer_lbl.setObjectName(u"tprPathServer_lbl")
        self.tprPathServer_lbl.setMinimumSize(QSize(0, 0))
        self.tprPathServer_lbl.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.tprPathServer_lbl, 8, 1, 1, 1)

        self.comment_txe = QPlainTextEdit(createDialog)
        self.comment_txe.setObjectName(u"comment_txe")

        self.gridLayout_2.addWidget(self.comment_txe, 6, 1, 1, 2)

        self.label_6 = QLabel(createDialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_6, 3, 0, 1, 1)

        self.keyEdit_lyo = QVBoxLayout()
        self.keyEdit_lyo.setObjectName(u"keyEdit_lyo")
        self.keyEdit_lyo.setContentsMargins(50, -1, -1, -1)

        self.gridLayout_2.addLayout(self.keyEdit_lyo, 0, 0, 1, 3)

        self.obrPathServer_lbl = QLineEdit(createDialog)
        self.obrPathServer_lbl.setObjectName(u"obrPathServer_lbl")
        self.obrPathServer_lbl.setMinimumSize(QSize(0, 0))
        self.obrPathServer_lbl.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.obrPathServer_lbl, 10, 1, 1, 1)

        self.TprCheckBox_chb = QCheckBox(createDialog)
        self.TprCheckBox_chb.setObjectName(u"TprCheckBox_chb")
        self.TprCheckBox_chb.setTristate(False)

        self.gridLayout_2.addWidget(self.TprCheckBox_chb, 8, 2, 1, 1)

        self.PdfCheckBox_chb = QCheckBox(createDialog)
        self.PdfCheckBox_chb.setObjectName(u"PdfCheckBox_chb")
        self.PdfCheckBox_chb.setTristate(False)

        self.gridLayout_2.addWidget(self.PdfCheckBox_chb, 7, 2, 1, 1)

        self.label_10 = QLabel(createDialog)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_10, 9, 0, 1, 1)

        self.label_8 = QLabel(createDialog)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_8, 7, 0, 1, 1)

        self.label_7 = QLabel(createDialog)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_7, 11, 0, 1, 1)

        self.label_3 = QLabel(createDialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)

        self.pathServer_lbl = QLineEdit(createDialog)
        self.pathServer_lbl.setObjectName(u"pathServer_lbl")
        self.pathServer_lbl.setMinimumSize(QSize(0, 0))
        self.pathServer_lbl.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.pathServer_lbl, 11, 1, 1, 2)

        self.TzCheckBox_chb = QCheckBox(createDialog)
        self.TzCheckBox_chb.setObjectName(u"TzCheckBox_chb")
        self.TzCheckBox_chb.setTristate(False)

        self.gridLayout_2.addWidget(self.TzCheckBox_chb, 9, 2, 1, 1)

        self.label_11 = QLabel(createDialog)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_11, 10, 0, 1, 1)

        self.pdfPathServer_lbl = QLineEdit(createDialog)
        self.pdfPathServer_lbl.setObjectName(u"pdfPathServer_lbl")
        self.pdfPathServer_lbl.setMinimumSize(QSize(0, 0))
        self.pdfPathServer_lbl.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.pdfPathServer_lbl, 7, 1, 1, 1)

        self.Archive_chb = QCheckBox(createDialog)
        self.Archive_chb.setObjectName(u"Archive_chb")
        self.Archive_chb.setMinimumSize(QSize(114, 0))
        self.Archive_chb.setTristate(False)

        self.gridLayout_2.addWidget(self.Archive_chb, 12, 2, 1, 1)

        self.Archive0_chb = QCheckBox(createDialog)
        self.Archive0_chb.setObjectName(u"Archive0_chb")
        self.Archive0_chb.setTristate(False)

        self.gridLayout_2.addWidget(self.Archive0_chb, 12, 1, 1, 1)

        QWidget.setTabOrder(self.name_lbl, self.client_lne)
        QWidget.setTabOrder(self.client_lne, self.contract_lne)
        QWidget.setTabOrder(self.contract_lne, self.subContract_lne)
        QWidget.setTabOrder(self.subContract_lne, self.date_dte)
        QWidget.setTabOrder(self.date_dte, self.create_btn)
        QWidget.setTabOrder(self.create_btn, self.cancel_btn)
        QWidget.setTabOrder(self.cancel_btn, self.client_cbb)
        QWidget.setTabOrder(self.client_cbb, self.contract_cbb)
        QWidget.setTabOrder(self.contract_cbb, self.comment_txe)

        self.retranslateUi(createDialog)

        QMetaObject.connectSlotsByName(createDialog)
    # setupUi

    def retranslateUi(self, createDialog):
        createDialog.setWindowTitle(QCoreApplication.translate("createDialog", u"Dialog", None))
        self.name_lbl.setText(QCoreApplication.translate("createDialog", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043f\u0440\u043e\u0435\u043a\u0442\u0430", None))
        self.ObrCheckBox_chb.setText(QCoreApplication.translate("createDialog", u"same with contract", None))
        self.label_2.setText(QCoreApplication.translate("createDialog", u"<html><head/><body><p>Comment</p></body></html>", None))
        self.tzPathServer_lbl.setText(QCoreApplication.translate("createDialog", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043e\u0431\u044a\u0435\u043a\u0442\u0430", None))
        self.label_4.setText(QCoreApplication.translate("createDialog", u"Contract", None))
        self.label_9.setText(QCoreApplication.translate("createDialog", u"\u0422\u041f\u0420", None))
        self.contract_lne.setText(QCoreApplication.translate("createDialog", u"AC.0000", None))
        self.label_5.setText(QCoreApplication.translate("createDialog", u"/", None))
        self.subContract_lne.setText(QCoreApplication.translate("createDialog", u"00", None))
        self.client_lne.setText(QCoreApplication.translate("createDialog", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.objectName_lbl.setText(QCoreApplication.translate("createDialog", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043e\u0431\u044a\u0435\u043a\u0442\u0430", None))
        self.label.setText(QCoreApplication.translate("createDialog", u"Project", None))
        self.create_btn.setText(QCoreApplication.translate("createDialog", u"Create", None))
        self.cancel_btn.setText(QCoreApplication.translate("createDialog", u"Cancel", None))
        self.tprPathServer_lbl.setText(QCoreApplication.translate("createDialog", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043e\u0431\u044a\u0435\u043a\u0442\u0430", None))
        self.label_6.setText(QCoreApplication.translate("createDialog", u"Object", None))
        self.obrPathServer_lbl.setText(QCoreApplication.translate("createDialog", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043e\u0431\u044a\u0435\u043a\u0442\u0430", None))
        self.TprCheckBox_chb.setText(QCoreApplication.translate("createDialog", u"same with contract", None))
        self.PdfCheckBox_chb.setText(QCoreApplication.translate("createDialog", u"same with contract", None))
        self.label_10.setText(QCoreApplication.translate("createDialog", u"\u0422/\u0417", None))
        self.label_8.setText(QCoreApplication.translate("createDialog", u"PDF", None))
        self.label_7.setText(QCoreApplication.translate("createDialog", u"URL", None))
        self.label_3.setText(QCoreApplication.translate("createDialog", u"Client", None))
        self.pathServer_lbl.setText(QCoreApplication.translate("createDialog", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043e\u0431\u044a\u0435\u043a\u0442\u0430", None))
        self.TzCheckBox_chb.setText(QCoreApplication.translate("createDialog", u"same with contract", None))
        self.label_11.setText(QCoreApplication.translate("createDialog", u"\u041e\u0431\u0440\u0430\u0437\u0446\u044b", None))
        self.pdfPathServer_lbl.setText(QCoreApplication.translate("createDialog", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043e\u0431\u044a\u0435\u043a\u0442\u0430", None))
        self.Archive_chb.setText(QCoreApplication.translate("createDialog", u">>>archive<<<", None))
        self.Archive0_chb.setText(QCoreApplication.translate("createDialog", u"\u041e\u0421\u0422\u041e\u0420\u041e\u0416\u041d\u041e!!! \u0410\u0440\u0445\u0438\u0432\u0430\u0446\u0438\u044f \u0443\u0434\u0430\u043b\u0438\u0442 \u0432\u0441\u0435 \u043b\u043e\u043a\u0430\u043b\u044c\u043d\u044b\u0435 \u0444\u0430\u0439\u043b\u044b, \u043a\u0440\u043e\u043c\u0435 \u043f\u043e\u0441\u043b\u0435\u0434\u043d\u0435\u0433\u043e DWG \u0438 PDF!!!", None))
    # retranslateUi

