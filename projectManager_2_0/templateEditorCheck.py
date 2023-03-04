
from PySide2.QtCore import *
from PySide2.QtWidgets import *
import templateEditor_ui as ui
import os, json
import templateTreeWidget

templateCheckFile= os.path.join(os.path.dirname(__file__), 'templateCheck.json')

class templateEditorCheckClass(QWidget, ui.Ui_templateEditor):
    def __init__(self):
        super(templateEditorCheckClass, self).__init__()
        self.setupUi(self)

        #UI
        self.tree_trw = templateTreeWidget.tamplateTreeClass()
        # self.tree_trw.setDragDropMode(QAbstractItemView.InternalMove)
        # self.tree_trw.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.verticalLayout.addWidget(self.tree_trw)

        #connects
        self.add_btn.clicked.connect(self.addItemBefore)
        self.remove_btn.clicked.connect(self.removeItem)
        self.save_btn.clicked.connect(self.saveTemplate)
        self.close_btn.clicked.connect(self.close)


        #clicked
        #self.tree_trw.itemDoubleClicked.connect(self.addItem)

        #start
        self.loadTemplate()

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
        with open(templateCheckFile, 'w') as f:
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
        if os.path.exists(templateCheckFile):
            with open(templateCheckFile) as f:
                template= json.load(f)
                self.restoreStructure(template)

    def restoreStructure(self, data, parent=None):
        if not parent:
            parent= self.tree_trw.invisibleRootItem()
        for i in data:
            item= self.addItem(i['name'], parent)
            self.restoreStructure(i['children'], item)


