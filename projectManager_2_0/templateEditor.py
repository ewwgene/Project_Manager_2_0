
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import templateEditor_ui as ui
import os, json
import templateTreeWidget

templateFile= os.path.join(os.path.dirname(__file__), 'template.json')

class templateEditorClass(QWidget, ui.Ui_templateEditor):
    def __init__(self):
        super(templateEditorClass, self).__init__()
        self.setupUi(self)

        self.tree_trw= templateTreeWidget.tamplateTreeClass()
        # self.tree_trw.setDragDropMode(QAbstractItemView.InternalMove)
        # self.tree_trw.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.verticalLayout.addWidget(self.tree_trw)

        #connects
        self.add_btn.clicked.connect(self.addItemBefore)
        self.remove_btn.clicked.connect(self.removeItem)
        self.save_btn.clicked.connect(self.saveTemplate)
        self.close_btn.clicked.connect(self.close)
        # self.setDragDropMode(QAbstractItemView.DropOnly)
        # self.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.files = []

        #clicked
        #self.tree_trw.itemDoubleClicked.connect(self.addItem)

        #start
        self.loadTemplate()

    # def dropEvent(self, event):
    #     if event.source() is self:
    #         event.ignore()
    #     else:
    #         mimedata= event.mimeData()
    #         if mimedata.hasUrls():
    #             for f in mimedata.urls():
    #                 print(f.toLocalFile())
    #
    # def dragEnterEvent(self, event):
    #     if event.source() is self:
    #         event.ignore()
    #     else:
    #         mimedata = event.mimeData()
    #         if mimedata.hasUrls():
    #             event.accept()
    #         else:
    #             event.ignore()
    #
    # def dragMoveEvent(self, event):
    #     if event.source() is self:
    #         event.ignore()
    #     else:
    #         mimedata = event.mimeData()
    #         if mimedata.hasUrls():
    #             event.accept()
    #         else:
    #             event.ignore()

    def addItemBefore(self):
        parent= self.tree_trw.selectedItems()
        if parent:
            self.addItem('Folder', parent[0])
        else:
            self.addItem()

    def addItem(self, name='Folder', parent=None):
        if not parent:
            parent= self.tree_trw.invisibleRootItem()
        item= QTreeWidgetItem()
        item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable | Qt.ItemIsDragEnabled | Qt.ItemIsDropEnabled)
        item.setText(0, name)
        parent.addChild(item)
        #открыть структуру
        item.setExpanded(1)
        return item

    def removeItem(self):
        items= self.tree_trw.selectedItems()
        for i in items:
            (i.parent() or self.tree_trw.invisibleRootItem()).takeChild(self.tree_trw.indexFromItem(i).row())

    def saveTemplate(self):
        template= self.getStructure()
        with open(templateFile, 'w') as f:
            json.dump(template, f, indent=4)
        self.close()

    def getStructure(self, parent=None):
        level= []
        if not parent:
            parent= self.tree_trw.invisibleRootItem()
        for i in range(parent.childCount()):
            ch= parent.child(i)
            children= self.getStructure(ch)
            level.append({'name':ch.text(0),
                          'children':children})
        return level

    def loadTemplate(self):
        if os.path.exists(templateFile):
            with open(templateFile) as f:
                template= json.load(f)
                self.restoreStructure(template)

    def restoreStructure(self, data, parent=None):
        if not parent:
            parent= self.tree_trw.invisibleRootItem()
        for i in data:
            item= self.addItem(i['name'], parent)
            self.restoreStructure(i['children'], item)


