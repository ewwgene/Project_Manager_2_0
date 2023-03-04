from PySide2.QtWidgets import *
from widgets import editProject_ui as ui
import createProject

class projectManagerClass(QDialog, ui.Ui_editDialog):
    def __init__(self, parent):
        super(projectManagerClass, self).__init__(parent)
        self.setupUi(self)

        #connects
        self.edit_btn.clicked.connect(self.doEdit)
        self.cancel_btn.clicked.connect(self.reject)



    def doEdit(self):
        if self.name_lbl.text():
            self.accept()

    def fillInfo(self, item):
        info = createProject.getProjectInfo(item.data(32))
        if info:
            self.name_lbl.setText(info['name'])


    def getDialogData(self):
        return dict(
            name=self.name_lbl.text(),
            comment=self.comment_txe.toPlainText()

        )