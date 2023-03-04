from PySide2.QtCore import *
from PySide2.QtWidgets import *
import settingsDialog_ui as ui
import settings

class settingsDialogClass(QDialog, ui.Ui_settingsDialog):
    def __init__(self, parent):
        super(settingsDialogClass, self).__init__(parent)
        self.setupUi(self)

        #UI
        self.table_tbl.setColumnCount(2)
        self.table_tbl.setColumnWidth(1, 350)


        #start
        self.fillTable()

    def fillTable(self):
        data= settings.settingsClass().load()
        for key, value in data.items():
            self.addParm(key, value)


    def addParm(self, parm, value):
        self.table_tbl.insertRow(self.table_tbl.rowCount())
        item= QTableWidgetItem()
        item.setText(parm)
        item.setFlags(item.flags() & ~Qt.ItemIsEditable)
        self.table_tbl.setItem(self.table_tbl.rowCount()-1, 0, item)

        item = QTableWidgetItem()
        item.setText(value)
        self.table_tbl.setItem(self.table_tbl.rowCount()-1, 1, item)

    def getTableData(self):
        data= dict()
        for i in range(self.table_tbl.rowCount()):
            parm= self.table_tbl.item(i, 0).text()
            value = self.table_tbl.item(i, 1).text()
            data[parm]= value
        return data


