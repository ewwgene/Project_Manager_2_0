from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
# import settings
# import createProject
import os

class tamplateTreeClass(QTreeWidget):
    def __init__(self):
        super(tamplateTreeClass, self).__init__()
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.setHeaderItem(__qtreewidgetitem)
        self.setObjectName(u"tree_trw")
        self.setHeaderHidden(True)
        self.setDragDropMode(QAbstractItemView.InternalMove)
        self.setAcceptDrops(True)
        self.setDragEnabled(True)
        self.setDropIndicatorShown(True)
        self.setDragDropOverwriteMode(True)
        self.setMouseTracking(True)
        # self.setDropIndicatorShown(True)
        self.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.files = []




    def dropEvent(self, event):
        print('dropEvent happened')
        mimedata = event.mimeData()
        if mimedata.hasUrls():
            for f in mimedata.urls():
                self.addFile(f.toLocalFile())
            if event.source() is self:
                event.ignore()
                print('Has 1! ')
        super().dropEvent(event)
        # event.setDropAction(Qt.TargetMoveAction)
    #     print('dropEvent happened')
    #     event.acceptProposedAction()

    #     # mimedata = event.mimeData()
    #     pass
        # print(event)
        # event.accept()
        # return super().dropEvent(event)
        # if mimedata.hasUrls():
        #     for f in mimedata.urls():
        #         self.addFile(f.toLocalFile())
    #     # if event.source() is self:
    #     #     event.ignore()
    #     #     print('Has 1! ')
    #     # else:
    #     #     print('Has 2! ')
    #     #     mimedata= event.mimeData()
    #     #     if mimedata.hasUrls():
    #     #         for f in mimedata.urls():
    #     #             self.addFile(f.toLocalFile())
    #     if event.mimeData().hasUrls:
    #         print('Has 3! ')
    #
    #         event.setDropAction(Qt.CopyAction)
    #         event.accept()
    #         # event.ignore()
    #         links = []
    #         for url in event.mimeData().urls():
    #             links.append(str(url.toLocalFile()))
        #
        # else:
        #     print('Has 4! ')
        #     event.ignore()
    #
    def dragEnterEvent(self, event):
        print('dragEnterEvent happened')
        event.acceptProposedAction()
        # mimedata = event.mimeData()
    #     if mimedata.hasUrls():
    #         event.accept()
    #     else:
    #         event.ignore()
    #     if event.source() is self:
    #         event.ignore()
    #         print('Has 5! ')
    #     else:
    #         print('Has 6! ')
    #         mimedata = event.mimeData()
    #         if mimedata.hasUrls():
    #             event.accept()
    #         else:
    #             event.ignore()
    #     if event.mimeData().hasUrls:
    #         print('Has 7! ')
    #         event.accept()
    #     else:
    #         print('Has 8! ')
    #         event.ignore()
    #
    def dragMoveEvent(self, event):
        print('dragMoveEvent happened')
        event.acceptProposedAction()
    #     mimedata = event.mimeData()
    #     if mimedata.hasUrls():
    #         event.accept()
    #     else:
    #         event.ignore()
    #     if event.source() is self:
    #         event.ignore()
    #         print('Has 9! ')
    #     else:
    #         print('Has 10! ')
    #         mimedata = event.mimeData()
    #         if mimedata.hasUrls():
    #             event.accept()
    #         else:
    #             event.ignore()
    #     if event.mimeData().hasUrls:
    #         print('Has 11! ')
    #         event.setDropAction(Qt.CopyAction)
    #         event.accept()
    #     else:
    #         print('Has 12! ')
    #         event.ignore()
    #
    def addFile(self, path):
        if not path in self.files:
            item = QTreeWidgetItem(self)
            item.setText(0, os.path.basename(path))
            item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable | Qt.ItemIsDragEnabled | Qt.ItemIsDropEnabled)
            item.setData(0, Qt.UserRole, path)
            self.files.append(path)
            item.setExpanded(1)
    #     if not path in self.files:
    #         if os.path.isdir(path):
    #         #     # for l in os.listdir(path):
    #         #     self.addFile(os.path.join(path, l))
    #         # else:
    #             item= QTreeWidgetItem(self)
    #             item.setText(0, os.path.basename(path))
    #             item.setData(0, Qt.UserRole, path)
    #             self.files.append(path)

    # def startDrag(self, dropAction):
    #     # self.setDragDropMode(QAbstractItemView.InternalMove)
    #     print(dropAction)
        # drag= QDrag(self)
        # # print(drag, type(drag))
        # # drag.setdr
        # mimedata= QMimeData()
        # urls=[]
        # for i in self.selectedItems():
        #     urls.append(i.data(0, Qt.UserRole))
        # mimedata.setUrls([QUrl.fromLocalFile(x) for x in urls])
        # drag.setMimeData(mimedata)
        # drag.exec_()

    #
    # def deleteSelected(self):
    #     for s in self.selectedItems():
    #         self.files.remove(s.data(0, Qt.UserRole))
    #         self.takeTopLevelItem(self.indexFromItem(s).row())
    #
    # def getAllFiles(self):
    #     return self.files
    #
    # def keyPressEvent(self, event):
    #     if event.key()==Qt.Key_Delete:
    #         self.deleteSelected()
