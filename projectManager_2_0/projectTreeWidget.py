from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
import settings
import createProject
import os

class projectTreeClass(QTreeWidget):
    def __init__(self):
        super(projectTreeClass, self).__init__()

        self.setHeaderHidden(1)
        self.setSelectionMode(QAbstractItemView.ExtendedSelection)
        # self.setAcceptDrops(True)
        self.setExpandsOnDoubleClick(0)
        self.y = 0
        self.x = 0
        self.z = False
        self.fStock = None
        self.parentStock = None
        self.fullPathStock = None


    # def dragEnterEvent(self, event):
    #     if event.mimeData().hasUrls:
    #         event.accept()
    #     else:
    #         event.ignore()
    #
    # def dragMoveEvent(self, event):
    #     if event.mimeData().hasUrls:
    #         event.setDropAction(Qt.CopyAction)
    #         event.accept()
    #     else:
    #         event.ignore()
    #
    # def dropEvent(self, event):
    #     if event.mimeData().hasUrls:
    #         event.setDropAction(Qt.CopyAction)
    #         event.accept()
    #         links = []
    #         for url in event.mimeData().urls():
    #             links.append(str(url.toLocalFile()))
    #         print('Has drop Event! ')
    #     else:
    #         event.ignore()




    def clearProjectList(self):
        self.clear()
        data = settings.settingsClass().load()
        path = data.get('path')
        return path

    def updateProjectList(self, path=None, parent=None):
        Clist=[]
        Alist=[]
        if not path:

            self.clearProjectList()
            data = settings.settingsClass().load()
            path = data.get('path')

            self.updateProjectList(path)
        else:
            if os.path.exists(path):
                for f in os.listdir(path):
                    fullPath = os.path.join(path, f)
                    if self.isProject(fullPath):
                        # Clist.append(f)
                        info = createProject.getProjectInfo(fullPath)
                        if self.inDictionary('archive', info) and info['archive']:
                            Clist.append(fullPath)
                        else:
                            Alist.append(fullPath)

        for fullPathClist in Alist:
            f= os.path.basename(fullPathClist)
            fullPath= fullPathClist
            # self.y = self.y + 1
            # childCount = len([f for f in os.listdir(fullPath) if self.isProject(os.path.join(fullPath, f))])
            # if self.z:
            # f= self.fStock + '_' + f
            # parent= self.parentStock
            # item = self.addProject(self.fStock + '_' + f, self.parentStock, fullPath)
            item = self.addProject(f, parent, fullPath)

            item.setData(0, 32, fullPath)
            # self.z = False
            # self.parentStock = None
            # self.fStock = None
            self.updateProjectListHide(fullPath, item)

            # else:
            #     if childCount == 1:
            #         self.x = self.x + 1
            #         # print('x=', self.x,'y=', self.y,  f)
            #         self.fStock = f
            #         self.parentStock = parent
            #         # self.fullPathStock=fullPath
            #         self.z = True
            #         self.updateProjectListHide(fullPath, None)
            #     else:
            #         item = self.addProject(f, parent, fullPath)
            #         item.setData(0, 32, fullPath)
            #         self.updateProjectListHide(fullPath, item)


        for fullPathClist in Clist:
            f= os.path.basename(fullPathClist)
            fullPath= fullPathClist
            # self.y = self.y + 1
            # childCount = len([f for f in os.listdir(fullPath) if self.isProject(os.path.join(fullPath, f))])
            # if self.z:
            # f= self.fStock + '_' + f
            # parent= self.parentStock
            # item = self.addProject(self.fStock + '_' + f, self.parentStock, fullPath)
            item = self.addProject(f, parent, fullPath)
            item.setData(0, 32, fullPath)
            # self.z = False
            # self.parentStock = None
            # self.fStock = None
            self.updateProjectListHide(fullPath, item)

            # else:
            #     if childCount == 1:
            #         self.x = self.x + 1
            #         # print('x=', self.x,'y=', self.y,  f)
            #         self.fStock = f
            #         self.parentStock = parent
            #         # self.fullPathStock=fullPath
            #         self.z = True
            #         self.updateProjectListHide(fullPath, None)
            #     else:
            #         item = self.addProject(f, parent, fullPath)
            #         item.setData(0, 32, fullPath)
            #         self.updateProjectListHide(fullPath, item)


        # print(Clist)
        return path

    def updateProjectListHide(self, path=None, parent=None):
        box_a=[]
        box_b=[]
        box_c=[]
        new_b=[]
        new_a=[]
        new_с=[]
        few_b = []
        few_a = []
        few_с = []
        if os.path.exists(path):
            Pinfo = createProject.getProjectInfo(path)
            if self.inDictionary('sortA', Pinfo):
                print('SORT')
                for f in os.listdir(path):
                    fullPath = os.path.join(path, f)
                    if self.isProject(fullPath):
                        info = createProject.getProjectInfo(fullPath)
                        if self.inDictionary('sort', info):
                            print(fullPath)
                            box_a.append(fullPath)
                            box_b.append(info['sort'])
                            new_b, new_a = zip(*[(b, a) for b, a in sorted(zip(box_b, box_a))])
                        else:
                            box_c.append(fullPath)
                print(new_b)
                print(new_a)
                for nn in new_a:
                    few_a.append(nn)
                few_с=few_a+box_c
                #     new_a.append(cc)
                #     print(cc)
                # new_с = new_a + box_c
                print(few_с)


                self.updateProjectListSort(few_с, parent)
                # else:
                #     self.updateProjectListSort(fullPath, f, parent)
            else:
                for f in os.listdir(path):
                    fullPath = os.path.join(path, f)
                    if self.isProject(fullPath):
                        info = createProject.getProjectInfo(fullPath)
                        self.y = self.y + 1
                        childCount = len([f for f in os.listdir(fullPath) if self.isProject(os.path.join(fullPath, f))])
                        if self.z:
                            # f= self.fStock + '_' + f
                            # parent= self.parentStock
                            item = self.addProject(self.fStock + '_' + f, self.parentStock, fullPath)

                            item.setData(0, 32, fullPath)
                            self.z = False
                            self.parentStock = None
                            self.fStock = None
                            self.updateProjectListHide(fullPath, item)

                        else:
                            if childCount == 1:
                                self.x = self.x + 1
                                # print('x=', self.x,'y=', self.y,  f)
                                self.fStock = f
                                self.parentStock = parent
                                # self.fullPathStock=fullPath
                                self.z = True
                                self.updateProjectListHide(fullPath, None)
                            else:
                                item = self.addProject(f, parent, fullPath)
                                item.setData(0, 32, fullPath)
                                self.updateProjectListHide(fullPath, item)

    def updateProjectListSort(self, ListA=None, parent=None):

        for f in ListA:
            fullPath = f
            f= os.path.basename(fullPath)
            if self.isProject(fullPath):
                info = createProject.getProjectInfo(fullPath)
                self.y = self.y + 1
                childCount = len([f for f in os.listdir(fullPath) if self.isProject(os.path.join(fullPath, f))])
                if self.z:
                    # f= self.fStock + '_' + f
                    # parent= self.parentStock
                    item = self.addProject(self.fStock + '_' + f, self.parentStock, fullPath)

                    item.setData(0, 32, fullPath)
                    self.z = False
                    self.parentStock = None
                    self.fStock = None
                    self.updateProjectListHide(fullPath, item)

                else:
                    if childCount == 1:
                        self.x = self.x + 1
                        # print('x=', self.x,'y=', self.y,  f)
                        self.fStock = f
                        self.parentStock = parent
                        # self.fullPathStock=fullPath
                        self.z = True
                        self.updateProjectListHide(fullPath, None)
                    else:
                        item = self.addProject(f, parent, fullPath)
                        item.setData(0, 32, fullPath)
                        self.updateProjectListHide(fullPath, item)

    # def singleStock(self, f, parent, fullPath):
    #     self.y = self.y + 1
    #     childCount = len([f for f in os.listdir(fullPath) if self.isProject(os.path.join(fullPath, f))])
    #     if self.z:
    #         # f= self.fStock + '_' + f
    #         # parent= self.parentStock
    #         item = self.addProject(self.fStock + '_' + f, self.parentStock, fullPath)
    #
    #         item.setData(0, 32, fullPath)
    #         self.z = False
    #         self.parentStock = None
    #         self.fStock = None
    #         self.updateProjectList(fullPath, item)
    #     else:
    #
    #         if childCount == 1:
    #             self.x = self.x + 1
    #             # print('x=', self.x,'y=', self.y,  f)
    #             self.fStock = f
    #             self.parentStock = parent
    #             # self.fullPathStock=fullPath
    #             self.z = True
    #             self.updateProjectList(fullPath, None)
    #         else:
    #
    #             item = self.addProject(f, parent, fullPath)
    #             item.setData(0, 32, fullPath)
    #             self.updateProjectList(fullPath, item)

    def isProject(self, path):
        if os.path.exists(os.path.join(path, createProject.projectFile)):
            info = createProject.getProjectInfo(path)
            if info['contract']:
                return 1
            else:
                return 2


    def addClient(self):
        pass

    def addMain(self):
        pass

    def inDictionary(self, key, dict):
        if key in dict:
            return dict[key]
        else:
            return ''

    def addProject(self, name, parent=None, selPath=None):
        selInfo = createProject.getProjectInfo(selPath)
        if not parent:
            parent = self.invisibleRootItem()
        item= QTreeWidgetItem()
        item.setText(0, name)
        if self.inDictionary('archive', selInfo):
            # print('yes')
            if selInfo['archive']:
                # item.setBackgroundColor(0, QColor(Qt.gray))
                item.setForeground(0, QColor(Qt.gray))
        parent.addChild(item)
        print('add ', name)
        # item.setExpanded(1)
        return item

    def get_subtree_nodes(self, tree_widget_item):
        """Returns all QTreeWidgetItems in the subtree rooted at the given node."""
        nodes = []
        nodes.append(tree_widget_item)
        for i in range(tree_widget_item.childCount()):
            nodes.extend(self.get_subtree_nodes(tree_widget_item.child(i)))
        return nodes

    def get_all_items(self):
        """Returns all QTreeWidgetItems in the given QTreeWidget."""
        all_items = []
        for i in range(self.topLevelItemCount()):
            top_item = self.topLevelItem(i)
            all_items.extend(self.get_subtree_nodes(top_item))
        return all_items

    def findClient(self, client):
        return self.findItems(client, Qt.MatchFixedString | Qt.MatchRecursive, 0)

    def findContracts(self, client):
        source = self.findClient(client)
        nodes = []
        # for i in range(source.childCount()):
        #     nodes.append(item.child(i))
        print(client)




