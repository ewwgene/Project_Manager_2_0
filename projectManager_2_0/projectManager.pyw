import os.path
# import sys
# PYTHONPATH=r'C:\Users\eugen\OneDrive\Desktop\Py\2022\PycharmProjects\pythonProject\projectManager\widgets'
import sys
import textwrap

html= r'< img src = "C:\Users\eugen\OneDrive\Desktop\Py\2022\icons\icons8-panda-16.png">'

from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
import json
import projectManager_ui as ui
import projectTreeWidget, dialogTextPlain_ui
import createProjectDialog, settingsDialog, templateEditor, templateEditorCheck, settings, createProject, logo
import webbrowser, shutil

from redirect_ui import Ui_MainWindow
def p(x):
    print (x)


class projectManagerClass(QMainWindow, ui.Ui_projectManager):
    # def __init__(self):
    def __init__(self):

        super(projectManagerClass, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon(logo.picts['icon']))

        ##############################################
        # self.process = QProcess(self)
        # self.process.readyRead.connect(self.stdoutReady)
        # ###############
        # # self.process.readyReadStandardOutput.connect(self.stdoutReady)
        # # self.process.readyReadStandardError.connect(self.stderrReady)
        # ###############
        # self.process.started.connect(lambda: p('Started!'))
        # self.process.finished.connect(lambda: p('Finished!'))
        #
        # print('Starting process')
        # self.process.start('python', ['speak.py'])
        ##############################################
        # self.textEdit.setVisible(0)



        #logo
        logof = QPixmap(logo.picts['logo']).scaled(120, 120,
                                                   Qt.KeepAspectRatio,
                                                   Qt.FastTransformation,
                                                   )

        self.pix_lbl.setPixmap(logof)
        # sys.stdout= EmittingStream(textWritten= self.onrmalOutputWritten)
        # self.old_stdout = sys.stdout
        self.textBrowser_txt.setVisible(1)
        self.textBrowser_txt.setWordWrapMode(QTextOption.WrapAnywhere)
        # sys.stdout = EmittingStream()
        # self.write2Console(self.old_stdout)
        # logo.picts['logo']
        # self.textBrowser_txt.setText('C:/Users/eugen/OneDrive/Desktop/Py/2022/PycharmProjects/pythonProject/projectManager/projectManager.pyw')
        #tree
        self.projectTree_ltw = projectTreeWidget.projectTreeClass()

        self.projectList_lyo.addWidget(self.projectTree_ltw)

        self.settings_btn.setIcon(QIcon(logo.picts['tool']))
        # self.edit_btn.setIcon(QIcon(logo.picts['hammer']))
        # self.projectList_ltw= projectListWidget.projectListClass()
        # self.projectList_lyo.addWidget(self.projectList_ltw)
        # self.url_btn.setStyleSheet("text-align: left;")
        # self.local_btn.setStyleSheet("text-align: left;")

        #connects
        self.create_btn.clicked.connect(self.createProject)
        # self.edit_btn.setDisabled(1)
        self.settings_btn.clicked.connect(self.openSettingsDialog)
        self.templateEditor_btn.clicked.connect(self.openTemplateEditorDialog)
        self.templateCheckEditor_btn.clicked.connect(self.openTemplateEditorCheckDialog)
        # self.projectList_ltw.itemClicked.connect(self.showInfo)
        self.projectTree_ltw.itemClicked.connect(self.showInfo)
        self.projectTree_ltw.itemPressed.connect(self.showInfo)
        self.projectTree_ltw.itemDoubleClicked.connect(self.openProject)
        self.edit_btn.clicked.connect(self.editProject)
        self.expand_btn.clicked.connect(self.expandCollapse)
        self.newClient_btn.clicked.connect(self.updateList)
        self.minimize_btn.clicked.connect(self.Minimize)
        self.URL_lbl.mouseReleaseEvent = self.eventURL
        self.LOC_lbl.mouseReleaseEvent = self.eventLOC
        self.PDF_lbl.mouseReleaseEvent = self.eventPDF
        self.TPR_lbl.mouseReleaseEvent = self.eventTPR
        self.TZ_lbl.mouseReleaseEvent = self.eventTZ
        self.OBR_lbl.mouseReleaseEvent = self.eventOBR
        self.URL_lbl.mouseDoubleClickEvent = self.openURL
        self.LOC_lbl.mouseDoubleClickEvent = self.openLOC
        self.PDF_lbl.mouseDoubleClickEvent = self.openPDF
        self.TPR_lbl.mouseDoubleClickEvent = self.openTPR
        self.TZ_lbl.mouseDoubleClickEvent = self.openTZ
        self.OBR_lbl.mouseDoubleClickEvent = self.openOBR
        self.projectTree_ltw.mouseReleaseEvent = self.eventBase
        self.toolButton_btn.mousePressEvent = self.toolButtonEvent
        self.textBrowser_txt.mouseDoubleClickEvent = self.browserLarge

        # self.projectTree_ltw.fileDropped.connect(self.pictureDropped)

        # self.QPLabel.mousePressEvent = self.doSomething
        # self.local_btn.clicked.connect(self.copyLOCAL)
        # self.local_btn.mouseDoubleClickEvent().connect(self.copyLOCAL)
        self.info_lbl.setText('')
        self.updateList()
        self.expand_btn.setText('\u2BC6')
        self.minimize_btn.setText('\u2BC7')

    def browserLarge(self, what=None):
        if self.textBrowser_txt.maximumHeight()==50:
            self.textBrowser_txt.setMaximumHeight(325)
        else:
            self.textBrowser_txt.setMaximumHeight(50)

    def printd(self, text=None):
        # pass
        self.textBrowser_txt.append(QTime.currentTime().toString() +' '+ text)
        cursor = self.textBrowser_txt.textCursor()
        cursor.movePosition(QTextCursor.End)
        self.textBrowser_txt.setTextCursor(cursor)

    def print(self, text=None):
        # pass
        self.textBrowser_txt.append(text)



    # def append(self, text):
    #     cursor = self.textEdit.textCursor()
    #     cursor.movePosition(cursor.End)
    #     cursor.insertText(text)
    #
    # def stdoutReady(self):
    #     text = str(self.process.readAllStandardOutput())
    #     print (text.strip())
    #     self.append('\n' + text)
    #
    # def stderrReady(self):
    #     text = str(self.process.readAllStandardError())
    #     ###############
    #     # print (text.strip())
    #     ###############
    #     self.append(text)






    def get_size(self):
        dataPath = settings.settingsClass().load()
        basePath = dataPath.get('path')
        total_size = 0
        total_files = 0
        for dirpath, dirnames, filenames in os.walk(basePath):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                total_size += os.path.getsize(fp)
                total_files +=1
        info= 'Total size: '+ str(round((total_size/1024/1024), 2))+ 'mb  |  Total files: '+ str(total_files)
        return info


    def newClient(self):
        countBs= self.projectTree_ltw.selectedItems()
        countB= countBs[0]
        level= countB.columnCount()
        print(countB, level)
        return countB

    def Minimize(self):
        if self.minimize_btn.text()== '\u2BC7':
            self.minimize_btn.setText('\u2BC8')
            self.widget.setVisible(0)
            self.textBrowser_txt.setVisible(0)
            # self.resize(100, 661)
            self.flags=self.windowFlags()
            self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
            self.show()
            self.setMinimumSize(290, self.height())
            print(self.minimumSize())
            self.resize(100, self.height())
            self.move(0, 0)
            if self.expand_btn.text() == '\u2BC6':
                self.expandCollapse()
                self.expandCollapse()


        else:
            self.minimize_btn.setText('\u2BC7')
            self.widget.setVisible(1)
            self.textBrowser_txt.setVisible(1)
            self.resize(675, self.height())
            self.setWindowFlags(self.flags)
            self.show()




    def expandCollapse(self):
        if self.expand_btn.text()== '\u2BC6':
            self.expand_btn.setText('\u2BC8')
            self.expandItemFirst()
        else:
            if self.expand_btn.text()== '\u2BC8':
                self.expand_btn.setText('\u2BC5')
                self.projectTree_ltw.expandAll()
            else:
                self.expand_btn.setText('\u2BC6')
                self.projectTree_ltw.collapseAll()

    def expandItemFirst(self):
        for i in range(self.projectTree_ltw.topLevelItemCount()):
            item= self.projectTree_ltw.topLevelItem(i)
            info= createProject.getProjectInfo(item.data(0, 32))
            if info['contract']=='':
                self.projectTree_ltw.expandItem(item)



    # \u23F7
    # \u2BEF
    # \u23F6

    def updateList(self, path=None):

        self.print('Load Path from Settings >>>> '+ self.projectTree_ltw.updateProjectList())
        self.print(self.get_size())
        self.printd('')
        self.textBrowser_txt.insertHtml(html)
        self.textBrowser_txt. insertPlainText(' ПРИВЕТ')
        # self.printd('ПРИВЕТ ')
        # self.textBrowser_txt.insertHtml(html)
        print(QIcon(logo.picts['tool']))
        # < img src = r"C:\Users\eugen\OneDrive\Desktop\Py\2022\icons\icons8-europe-48.png" >

        #открытие списка
        if path:
            item= self.projectTree_ltw.findItems(os.path.basename(path), Qt.MatchRecursive | Qt.MatchEndsWith, 0)[0]
            self.projectTree_ltw.expandItem(item)
            self.projectTree_ltw.setCurrentItem(item)

    def openSettingsDialog(self):
        self.dial = settingsDialog.settingsDialogClass(self)
        if self.dial.exec_():
            data= self.dial.getTableData()
            settings.settingsClass().save(data)
        self.updateList()

    def openTemplateEditorDialog(self):
        self.edit = templateEditor.templateEditorClass()
        self.edit.show()

    def openTemplateEditorCheckDialog(self):
        self.edit = templateEditorCheck.templateEditorCheckClass()
        self.edit.show()

    def createProject(self):
        print('>>>>Create Project')
        # print(self.projectTree_ltw.selectedItems())
        dataPath = settings.settingsClass().load()
        basePath = dataPath.get('path')
        selClient = None
        selContract = None
        selObject = None
        selPath = None

        if self.projectTree_ltw.selectedItems():
            selItems= self.projectTree_ltw.selectedItems()
            selItem= selItems[0]
            selPath= selItem.data(0, 32)
            selInfo= createProject.getProjectInfo(selPath)

            if selInfo['client']:
                selClient= selInfo['client']
            if selInfo['contract']:
                selContract= selInfo['contract']
                if self.inDictionary('objectName', selInfo):
                    selObject= selInfo['objectName']
            if selInfo['subcontract']:
                selPath= os.path.dirname(selPath)

        self.dial= createProjectDialog.projectManagerClass(self)

        if selClient:
            self.dial.startBox()
            self.dial.createProject(selClient, selContract, selObject, None, selPath)
        else:
            self.dial.startBox()

        if self.dial.exec_():
            data = self.dial.getDialogData()
            # pathProject = os.path.join(basePath, data['path'], data['subcontract'] + '_' + data['name'])
            #
            #
            #
            #
            projectName= createProject.createProject(data)
            self.updateList(projectName)
            self.print('Creat Project >>>> '+ data['client']+' '+data['contract']+'/'+data['subcontract']+'_'+data['name'])
            # print(pName)
            # print((self.projectTree_ltw.findItems(os.path.basename(newpath), Qt.MatchRecursive, 0))[0])

    def editProject(self):
        print('----------------------------editProject')
        print(self.projectTree_ltw.selectedItems())

        dataPath = settings.settingsClass().load()
        basePath = dataPath.get('path')
        selClient = None
        selContract = None
        selSubcontract = None
        selObject = None
        keyEdit = True
        if not self.projectTree_ltw.selectedItems():
            pass
        else:
            selItems = self.projectTree_ltw.selectedItems()
            selItem = selItems[0]
            selPath = selItem.data(0, 32)
            selInfo = createProject.getProjectInfo(selPath)

            if selInfo['client']:
                selClient= selInfo['client']
            if selInfo['contract']:
                selContract= selInfo['contract']
                if self.inDictionary('objectName', selInfo):
                    selObject= selInfo['objectName']

            if selInfo['client']:
                selClient = selInfo['client']
                keyEdit = 1
            if selInfo['contract']:
                selContract = selInfo['contract']
                keyEdit = 2
            if selInfo['subcontract']:
                selSubcontract = selInfo['subcontract']
                keyEdit = 3


            self.dial = createProjectDialog.projectManagerClass(self)
            self.dial.keyLabel= QLabel()
            # self.dial.keyEdit_lyo.setAlignment(Qt.AlignHCenter)
            self.dial.arrowLabel = QLabel()
            self.dial.keyEdit_lyo.addWidget(self.dial.keyLabel)
            self.dial.keyEdit_lyo.addWidget(self.dial.arrowLabel)
            self.dial.keyLabel.setText(self.inDictionary('client', selInfo) + ' ' + self.inDictionary('contract', selInfo) + '/' +  self.inDictionary('subcontract', selInfo) + ' ' +  self.inDictionary('name', selInfo))
            self.dial.arrowLabel.setText('  \u2BEF')

            if selClient:
                self.dial.startBox(keyEdit, selPath)
                self.dial.createProject(selClient, selContract, selObject, selSubcontract, selPath)
            else:
                pass

            if self.dial.exec_():
                data = self.dial.getDialogData()
                if data['objectName']=='' or data['objectName']==None:
                    objectName = ''
                else:
                    objectName = '_' + data['objectName']

                if data['name']=='':
                    nameName = ''
                else:
                    nameName = '_' + data['name']

                if keyEdit == 3:
                    pathProject = os.path.join(basePath, data['client'], data['contract'] + objectName, data['subcontract'] + nameName)
                if keyEdit == 2:
                    pathProject = os.path.join(basePath, data['client'], data['contract'] + objectName)
                if keyEdit == 1:
                    pathProject = os.path.join(basePath, data['client'])
                #
                print('********************************')
                print('OLDPATH:', selPath)
                print('NEWPATH:', pathProject)
                print('DATA:', data)
                print('KEYEDIT:', keyEdit)
                projectName = createProject.editProject(selPath, pathProject, data, keyEdit)
                self.updateList(projectName)
                self.print('Edit Project >>>> '+ projectName)
                if data['checkArchive']:
                    self.archiveProject(pathProject)

                # print((self.projectTree_ltw.findItems(os.path.basename(newpath), Qt.MatchRecursive, 0))[0])

    def archiveProject(self, path):
        if self.projectTree_ltw.isProject(path):
            data = createProject.getProjectInfo(path)
            if data['archive']:
                if data['subcontract']!='':
                    self.archiveFiles(path, data)
                    # print('ARcHIVE! ', path)
                else:
                    for p in os.listdir(path):
                        self.archiveProject(os.path.join(path, p))


    def archiveFiles(self, path, data):
        dwg = '.dwg'
        pdf = '.pdf'
        leaveDWG = self.leaveFiles(path, data, dwg)
        leavePDF = self.leaveFiles(path, data, pdf)
        leave = leaveDWG+leavePDF
        self.archiveDelete(path, leave)

    def archiveDelete(self, path, leave):
        for f in os.listdir(path):
            if os.path.isfile(os.path.join(path, f)):
                # name, ext = os.path.splitext(f)
                if f == '.project':
                    leave.append(os.path.join(path, f))
                if os.path.join(path, f) not in leave:
                    os.remove(os.path.join(path, f))
                    print('Delete: ', os.path.join(path, f))
            else:
                if f == '_help':
                    for h in os.listdir(os.path.join(path, f)):
                        if os.path.isfile(os.path.join(path, f, h)):
                            os.remove(os.path.join(path, f, h))
                        else:
                            shutil.rmtree(os.path.join(path, f, h), ignore_errors=True)
                    print('Delete _help: ', os.path.join(path, f))
                else:
                    shutil.rmtree(os.path.join(path, f), ignore_errors=True)
                    print('Delete folder: ', os.path.join(path, f))
        print('Leave: ', leave)
        # print('Delete in ', path)
        # print('but Leave ', leave)

    def leaveFiles(self, path, data, extIn):
        files = []
        leave = []
        if data['URLpath']!='':
            for file in os.listdir(path):
                # print('1'+ project)
                if os.path.isfile(os.path.join(path, file)):
                    name, ext = os.path.splitext(file)
                    if ext == extIn:
                        # pathFile = os.path.join(path, file)
                        files.append(file)
        files.sort(key=lambda l: os.path.getmtime(os.path.join(path, l)), reverse=1)
        # print(files)
        for i, file in enumerate(files):
            if i==0:
                self.printd('____ leave: ' + file)
                # print('     leave:', file)
                leave.append(os.path.join(path, file))
            else:
                name, ext= os.path.splitext(file)
                if name[-1]=='!':
                    leave.append(os.path.join(path, file))
        return leave





    def showInfo(self, item):
        info= createProject.getProjectInfo(item.data(0, 32))
        # print(item.data(32))

        if info:
            text= '''Client:
%s

Name:
%s            

Contract:
%s/%s

Object:
%s

Date:
%s

Comment:
%s
''' % (self.inDictionary('client', info), self.inDictionary('name', info), self.inDictionary('contract', info), self.inDictionary('subcontract', info), self.inDictionary('objectName', info), self.inDictionary('date', info), self.inDictionary('comment', info))
        else:
            text= ''
        self.info_lbl.setText(text)
        start=14
        end=26-start
        if self.inDictionary('URLpath', info):
            self.URL_lbl.setText(('URL ' + info['URLpath'])[0:start] + '...' + info['URLpath'][-end:])
        else:
            self.URL_lbl.setText('URL')

        if self.inDictionary('PDF_URLpath', info):
            self.PDF_lbl.setText(('PDF ' + info['PDF_URLpath'])[0:start] + '...' + info['PDF_URLpath'][-end:])
        else:
            if self.inDictionary('keypdfurl', info):
                if info['keypdfurl']:
                    clientInfo=createProject.getProjectInfo(os.path.dirname(item.data(0, 32)))
                    if self.inDictionary('PDF_URLpath', clientInfo):
                        self.PDF_lbl.setText(('PDF ' + clientInfo['PDF_URLpath'])[0:start] + '...' + clientInfo['PDF_URLpath'][-end:])
                else:
                    self.PDF_lbl.setText('PDF')
            else:
                self.PDF_lbl.setText('PDF')

        if self.inDictionary('TPR_URLpath', info):
            self.TPR_lbl.setText(('ТПР ' + info['TPR_URLpath'])[0:start] + '...' + info['TPR_URLpath'][-end:])
        else:
            if self.inDictionary('keytprurl', info):
                if info['keytprurl']:
                    clientInfo=createProject.getProjectInfo(os.path.dirname(item.data(0, 32)))
                    if self.inDictionary('TPR_URLpath', clientInfo):
                        self.TPR_lbl.setText(('ТПР ' + clientInfo['TPR_URLpath'])[0:start] + '...' + clientInfo['TPR_URLpath'][-end:])
                else:
                    self.TPR_lbl.setText('ТПР')
            else:
                self.TPR_lbl.setText('ТПР')

        if self.inDictionary('TZ_URLpath', info):
            self.TZ_lbl.setText(('T3 ' + info['TZ_URLpath'])[0:start] + '...' + info['TZ_URLpath'][-end:])
        else:
            if self.inDictionary('keytzurl', info):
                if info['keytzurl']:
                    clientInfo=createProject.getProjectInfo(os.path.dirname(item.data(0, 32)))
                    if self.inDictionary('TZ_URLpath', clientInfo):
                        self.TZ_lbl.setText(('T3 ' + clientInfo['TZ_URLpath'])[0:start] + '...' + clientInfo['TZ_URLpath'][-end:])
                else:
                    self.TZ_lbl.setText('T3')
            else:
                self.TZ_lbl.setText('T3')

        if self.inDictionary('OBR_URLpath', info):
            self.OBR_lbl.setText(('ОБР ' + info['OBR_URLpath'])[0:start] + '...' + info['OBR_URLpath'][-end:])
        else:
            if self.inDictionary('keyobrurl', info):
                if info['keyobrurl']:
                    clientInfo=createProject.getProjectInfo(os.path.dirname(item.data(0, 32)))
                    if self.inDictionary('OBR_URLpath', clientInfo):
                        self.OBR_lbl.setText(('ОБР ' + clientInfo['OBR_URLpath'])[0:start] + '...' + clientInfo['OBR_URLpath'][-end:])
                else:
                    self.OBR_lbl.setText('ОБР')
            else:
                self.OBR_lbl.setText('ОБР')


        self.LOC_lbl.setText(('LOC ' + item.data(0, 32))[0:start] + '...' + item.data(0, 32)[-end:])

    def toolButtonEvent(self, what):
        print('toolButtonEvent')
        pos = what.globalPos()
        menu= QMenu()
        menuLink = QMenu('Helpful Links')
        # menuLink.setIcon(QIcon(logo.picts['library']))
        menuLink.setIcon(QIcon(logo.picts['help']))


        menu.addAction(QAction(QIcon(logo.picts['upload']), 'UPLOAD ALL', self, triggered=self.uploadAllALL))
        menu.addSeparator()
        menu.addAction(QAction(QIcon(logo.picts['dwg']), 'Upload all .DWG', self, triggered=self.uploadDWGALL))
        menu.addAction(QAction(QIcon(logo.picts['pdf']), 'Upload all .PDF', self, triggered=self.uploadPDFALL))
        menu.addAction(QAction('Upload all TPRs', self, triggered=self.uploadTPRALL))
        menu.addAction(QAction('Upload all _helps', self, triggered=self.uploadhelpALL))
        # menu.addSeparator()
        # menu.addAction(QAction('_renamer_all', self, triggered=self.renamerALL))
        # menu.addAction(QAction('_cleaner_all', self, triggered=self.cleaner_all))
        # menu.addSeparator()
        # menu.addAction(QAction('_chekk', self, triggered=self.chekk))
        menu.addSeparator()
        menuLink.addAction(QAction(QIcon(logo.picts['me']), 'Me', self, triggered=self.helpfulLinks2))
        menuLink.addSeparator()
        menuLink.addAction(QAction(QIcon(logo.picts['library']), 'Эскизы 2022', self, triggered=self.helpfulLinks3))
        menuLink.addAction(QAction(QIcon(logo.picts['measure']), 'Замеры 2022', self, triggered=self.helpfulLinks1))
        menuLink.addAction(QAction('На Проверку', self, triggered=self.helpfulLinks4))
        menu.addMenu(menuLink)

        # self.toolButton_btn.setMenu(menu)
        menu.exec_(pos)
        # self.toolButton_btn.addAction(QAction('SETTINGS', self, triggered=self.openSettingsDialog))
        # self.toolButton_btn.addAction(QAction('TOOL', self, triggered=self.toolSettings))

    def helpfulLinks1(self, key=None):
        path = r'H:\(Kameа) Мельница Лофт\[ ЗАМЕРЫ ]\2022'
        webbrowser.open(path)

    def helpfulLinks2(self, key=None):
        path = r'H:\(Kameа) Мельница Лофт\Евгений Зарипов'
        webbrowser.open(path)

    def helpfulLinks3(self, key=None):
        path = r'H:\Справочные материалы\Эскизы и фото\ЭСКИЗЫ\Камеа\2022'
        webbrowser.open(path)

    def helpfulLinks4(self, key=None):
        path = r'H:\(Kameа) Мельница Лофт\_ПРОВЕРКА ЗАКАЗОВ\НА ПРОВЕРКУ'
        webbrowser.open(path)

    def chekk(self):
        self.printd('что происходит')
        print('что происходит')

    def uploadAllALL(self):
        self.uploadAll(True)

    def uploadAll(self, key=False):
        self.print(' **** (upload ALL...')
        a1=0
        b1=0
        c1=0
        d1=0
        b2=0
        d2=0
        a1=self.uploadhelp(key)
        b1, b2=self.uploadPDF(key, None)
        c1=self.uploadDWG(key)
        d1, d2=self.uploadTPR(key)
        print('*** Uploaded All ***')
        x=a1+b1+c1+d1
        y=b2+d2
        self.printd(' **** uploaded ' + str(x) + ' files & deleted ' + str(y) + ' old files) ')
        self.textBrowser_txt.insertHtml(html)

    def uploadPDFALL(self):
        # self.print('  *** (upload PDF ALL...')
        self.uploadPDF(True, None)

    def uploadTPRALL(self):
        self.uploadTPR(True)

    def uploadhelpALL(self):
        print('(uploadhelpALL')
        # self.print('(uploadhelpALL')
        # self.print(' **** (uploadhelpALL...')
        self.uploadhelp(True)
        # self.print('Uploaded: ' + str(x) + ' all help files')
        # print(' **** Uploaded:' + x + 'all help files')

    def uploadDWGALL(self):
        self.uploadDWG(True)

    def uploadPDF(self, key=None, pathCheck=None):
        print('(def uploadPDF')
        self.print('  *** (upload PDF...')
        x=0
        y=0
        if key:
            selItems = []
            for i in range(self.projectTree_ltw.topLevelItemCount()):
                selItems.append(self.projectTree_ltw.topLevelItem(i))
        else:
            if self.projectTree_ltw.selectedItems():
                selItems = self.projectTree_ltw.selectedItems()
                print(selItems)
            else:
                selItems = []
                for i in range(self.projectTree_ltw.topLevelItemCount()):
                    selItems.append(self.projectTree_ltw.topLevelItem(i))

        for selItem in selItems:
            selPath = selItem.data(0, 32)
            selInfo = createProject.getProjectInfo(selPath)
            # print(selItem)
            if selInfo['subcontract']=='':
                for f in os.listdir(selPath):
                    fpath= os.path.join(selPath, f)

                    if self.projectTree_ltw.isProject(fpath):

                        fInfo = createProject.getProjectInfo(fpath)
                        if fInfo['subcontract']=='':
                            for n in os.listdir(fpath):
                                npath=os.path.join(fpath, n)
                                if self.projectTree_ltw.isProject(npath):

                                    nInfo = createProject.getProjectInfo(npath)
                                    if nInfo['subcontract'] == '':
                                        print('None contracts')
                                    else:
                                        print('go to hide 1')
                                        self.textBrowser_txt.insertPlainText('.')
                                        x1, y1=self.uploadPDFhide(npath, nInfo, pathCheck)
                                        x = x + x1
                                        y = y + y1
                                        # print(npath)

                        else:
                            print('go to hide 2')
                            self.textBrowser_txt.insertPlainText('.')
                            x1, y1=self.uploadPDFhide(fpath, fInfo, pathCheck)
                            x = x + x1
                            y = y + y1
                            # print(fpath)
            else:
                print('go to hide 3')
                self.textBrowser_txt.insertPlainText('.')
                x1, y1=self.uploadPDFhide(selPath, selInfo, pathCheck)
                x = x + x1
                y = y + y1
                # print(selPath)
        print('         def uploadPDF)')
        print('*** uploaded .pdf successfully')
        self.printd('  *** uploaded '+str(x)+' PDF)')
        return x, y


    def uploadTPR(self, key=None, pathCheck=None):
        print('(def uploadTPR')
        x=0
        y=0
        self.print('  *** (upload ТПР...')
        if key:
            selItems = []
            for i in range(self.projectTree_ltw.topLevelItemCount()):
                selItems.append(self.projectTree_ltw.topLevelItem(i))
        else:
            if self.projectTree_ltw.selectedItems():
                selItems = self.projectTree_ltw.selectedItems()
                print(selItems)
            else:
                selItems = []
                for i in range(self.projectTree_ltw.topLevelItemCount()):
                    selItems.append(self.projectTree_ltw.topLevelItem(i))

        for selItem in selItems:
            selPath = selItem.data(0, 32)
            selInfo = createProject.getProjectInfo(selPath)
            # print(selItem)
            if selInfo['subcontract']=='':
                for f in os.listdir(selPath):
                    fpath= os.path.join(selPath, f)

                    if self.projectTree_ltw.isProject(fpath):

                        fInfo = createProject.getProjectInfo(fpath)
                        if fInfo['subcontract']=='':
                            for n in os.listdir(fpath):
                                npath=os.path.join(fpath, n)
                                if self.projectTree_ltw.isProject(npath):

                                    nInfo = createProject.getProjectInfo(npath)
                                    if nInfo['subcontract'] == '':
                                        print('None contracts')
                                    else:
                                        print('go to hide 1')
                                        self.textBrowser_txt.insertPlainText('.')
                                        x1, y1=self.uploadTPRhide(npath, nInfo, pathCheck)
                                        x=x+x1
                                        y=y+y1
                                        # print(npath)

                        else:
                            print('go to hide 2')
                            self.textBrowser_txt.insertPlainText('.')
                            x1, y1=self.uploadTPRhide(fpath, fInfo, pathCheck)
                            x = x + x1
                            y = y + y1
                            # print(fpath)
            else:
                print('go to hide 3')
                self.textBrowser_txt.insertPlainText('.')
                x1, y1=self.uploadTPRhide(selPath, selInfo, pathCheck)
                x = x + x1
                y = y + y1
                # print(selPath)
        print('         def uploadTPR)')
        print('*** uploaded TPR successfully')
        self.printd('  *** uploaded ' + str(x) + ' ТПР)')
        return x, y

    def uploadTZ(self, key=None, pathCheck=None):
        print('(def uploadTZ')
        x=0
        y=0
        self.print('  *** (upload Т3...')
        if key:
            selItems = []
            for i in range(self.projectTree_ltw.topLevelItemCount()):
                selItems.append(self.projectTree_ltw.topLevelItem(i))
        else:
            if self.projectTree_ltw.selectedItems():
                selItems = self.projectTree_ltw.selectedItems()
                print(selItems)
            else:
                selItems = []
                for i in range(self.projectTree_ltw.topLevelItemCount()):
                    selItems.append(self.projectTree_ltw.topLevelItem(i))

        for selItem in selItems:
            selPath = selItem.data(0, 32)
            selInfo = createProject.getProjectInfo(selPath)
            # print(selItem)
            if selInfo['subcontract']=='':
                for f in os.listdir(selPath):
                    fpath= os.path.join(selPath, f)

                    if self.projectTree_ltw.isProject(fpath):

                        fInfo = createProject.getProjectInfo(fpath)
                        if fInfo['subcontract']=='':
                            for n in os.listdir(fpath):
                                npath=os.path.join(fpath, n)
                                if self.projectTree_ltw.isProject(npath):

                                    nInfo = createProject.getProjectInfo(npath)
                                    if nInfo['subcontract'] == '':
                                        print('None contracts')
                                    else:
                                        print('go to hide 1')
                                        self.textBrowser_txt.insertPlainText('.')
                                        x1, y1=self.uploadTZhide(npath, nInfo, pathCheck)
                                        x=x+x1
                                        y=y+y1
                                        # print(npath)

                        else:
                            print('go to hide 2')
                            self.textBrowser_txt.insertPlainText('.')
                            x1, y1=self.uploadTZhide(fpath, fInfo, pathCheck)
                            x = x + x1
                            y = y + y1
                            # print(fpath)
            else:
                print('go to hide 3')
                self.textBrowser_txt.insertPlainText('.')
                x1, y1=self.uploadTZhide(selPath, selInfo, pathCheck)
                x = x + x1
                y = y + y1
                # print(selPath)
        print('         def uploadTZ)')
        print('*** uploaded TZ successfully')
        self.printd('  *** uploaded ' + str(x) + ' Т3)')
        return x, y

    def uploadOBR(self, key=None, pathCheck=None):
        print('(def uploadOBR')
        x=0
        y=0
        self.print('  *** (upload ОБР...')
        if key:
            selItems = []
            for i in range(self.projectTree_ltw.topLevelItemCount()):
                selItems.append(self.projectTree_ltw.topLevelItem(i))
        else:
            if self.projectTree_ltw.selectedItems():
                selItems = self.projectTree_ltw.selectedItems()
                print(selItems)
            else:
                selItems = []
                for i in range(self.projectTree_ltw.topLevelItemCount()):
                    selItems.append(self.projectTree_ltw.topLevelItem(i))

        for selItem in selItems:
            selPath = selItem.data(0, 32)
            selInfo = createProject.getProjectInfo(selPath)
            # print(selItem)
            if selInfo['subcontract']=='':
                for f in os.listdir(selPath):
                    fpath= os.path.join(selPath, f)

                    if self.projectTree_ltw.isProject(fpath):

                        fInfo = createProject.getProjectInfo(fpath)
                        if fInfo['subcontract']=='':
                            for n in os.listdir(fpath):
                                npath=os.path.join(fpath, n)
                                if self.projectTree_ltw.isProject(npath):

                                    nInfo = createProject.getProjectInfo(npath)
                                    if nInfo['subcontract'] == '':
                                        print('None contracts')
                                    else:
                                        print('go to hide 1')
                                        self.textBrowser_txt.insertPlainText('.')
                                        x1, y1=self.uploadOBRhide(npath, nInfo, pathCheck)
                                        x=x+x1
                                        y=y+y1
                                        # print(npath)

                        else:
                            print('go to hide 2')
                            self.textBrowser_txt.insertPlainText('.')
                            x1, y1=self.uploadOBRhide(fpath, fInfo, pathCheck)
                            x = x + x1
                            y = y + y1
                            # print(fpath)
            else:
                print('go to hide 3')
                self.textBrowser_txt.insertPlainText('.')
                x1, y1=self.uploadOBRhide(selPath, selInfo, pathCheck)
                x = x + x1
                y = y + y1
                # print(selPath)
        print('         def uploadOBR)')
        print('*** uploaded OBR successfully')
        self.printd('  *** uploaded ' + str(x) + ' ОБР)')
        return x, y

    def uploadDWG(self, key=None):
        self.print('  *** (upload DWG...')
        x=0
        if key:
            selItems = []
            for i in range(self.projectTree_ltw.topLevelItemCount()):
                selItems.append(self.projectTree_ltw.topLevelItem(i))
        else:

            if self.projectTree_ltw.selectedItems():
                selItems = self.projectTree_ltw.selectedItems()
                print(selItems)
            else:
                selItems = []
                for i in range(self.projectTree_ltw.topLevelItemCount()):
                    selItems.append(self.projectTree_ltw.topLevelItem(i))


        for selItem in selItems:
            selPath = selItem.data(0, 32)
            selInfo = createProject.getProjectInfo(selPath)
            # print(selItem)
            if selInfo['subcontract']=='':
                for f in os.listdir(selPath):
                    fpath= os.path.join(selPath, f)

                    if self.projectTree_ltw.isProject(fpath):

                        fInfo = createProject.getProjectInfo(fpath)
                        if fInfo['subcontract']=='':
                            for n in os.listdir(fpath):
                                npath=os.path.join(fpath, n)
                                if self.projectTree_ltw.isProject(npath):

                                    nInfo = createProject.getProjectInfo(npath)
                                    if nInfo['subcontract'] == '':
                                        print('None contracts')
                                    else:
                                        self.textBrowser_txt.insertPlainText('.')
                                        x=x+self.uploadDWGhide(npath, nInfo, '.dwg')+self.uploadDWGhide(npath, nInfo, '.pdf')
                                        # print(npath)

                        else:
                            self.textBrowser_txt.insertPlainText('.')
                            x=x+self.uploadDWGhide(fpath, fInfo, '.dwg')+self.uploadDWGhide(fpath, fInfo, '.pdf')
                            # print(fpath)
            else:
                self.textBrowser_txt.insertPlainText('.')
                x=x+self.uploadDWGhide(selPath, selInfo, '.dwg')+self.uploadDWGhide(selPath, selInfo, '.pdf')
                # print(selPath)
        print('*** uploaded .dwg successfully')
        self.printd('  *** uploaded ' + str(x) + ' DWG)')
        return x



    def uploadhelp(self, key=None):
        x=0
        print('(def uploadhelp')
        self.print('  *** (upload DWG...')
        if key:
            selItems = []
            for i in range(self.projectTree_ltw.topLevelItemCount()):
                selItems.append(self.projectTree_ltw.topLevelItem(i))
        else:

            if self.projectTree_ltw.selectedItems():
                selItems = self.projectTree_ltw.selectedItems()
                print(selItems)
            else:
                selItems = []
                for i in range(self.projectTree_ltw.topLevelItemCount()):
                    selItems.append(self.projectTree_ltw.topLevelItem(i))

        for selItem in selItems:
            selPath = selItem.data(0, 32)
            selInfo = createProject.getProjectInfo(selPath)

            if selInfo['subcontract']=='':
                for f in os.listdir(selPath):
                    fpath= os.path.join(selPath, f)
                    # print(fpath)
                    if self.projectTree_ltw.isProject(fpath):
                        fInfo = createProject.getProjectInfo(fpath)
                        if fInfo['subcontract']=='':
                            for n in os.listdir(fpath):
                                npath=os.path.join(fpath, n)
                                if self.projectTree_ltw.isProject(npath):
                                    nInfo = createProject.getProjectInfo(npath)
                                    if nInfo['subcontract'] == '':
                                        print('None contracts')
                                    else:
                                        print('go to hide 1')
                                        self.textBrowser_txt.insertPlainText('.')
                                        x = x + self.uploadhelphide(npath, nInfo)
                        else:
                            print('go to hide 2')
                            self.textBrowser_txt.insertPlainText('.')
                            x = x + self.uploadhelphide(fpath, fInfo)
            else:
                print('go to hide 3')
                self.textBrowser_txt.insertPlainText('.')
                x = x + self.uploadhelphide(selPath, selInfo)

        self.printd('  *** uploaded ' + str(x) + ' help)')
        print(' **** Uploaded:' + str(x) + ' help files')
        return x


    def uploadPDFhide(self, path, info, pathCheck=None):
        print('(def uploadPDFhide')
        x=0
        y=0
        files = []
        namefiles = []
        serverPDFs = []
        clientPath = os.path.dirname(path)
        clientInfo = createProject.getProjectInfo(clientPath)
        check=None
        for project in os.listdir(path):
            # print('1'+ project)
            if os.path.isfile(os.path.join(path, project)):
                name, ext = os.path.splitext(project)
                if ext=='.pdf':
                    pathFile= os.path.join(path, project)
                    if (info['subcontract'] + '_' + info['name']) in project:
                        files.append(pathFile)
                        namefile=os.path.basename(pathFile)
                        namefiles.append(namefile)
        if files:
            locFreshFile = max(files, key=os.path.getmtime)
            nameLocFreshFile = os.path.basename(locFreshFile)
            nameLocFreshFileWithDate =QDate.toString(QDate.currentDate(), Qt.ISODateWithMs) + ' ' + nameLocFreshFile
            if pathCheck:
                pathPdf=pathCheck
            else:
                if not self.inDictionary('PDF_URLpath', info):
                    if info['keypdfurl']:
                        pathPdf= clientInfo['PDF_URLpath']
            for pdffile in os.listdir(pathPdf):
                name, ext = os.path.splitext(pdffile)
                if ext == '.pdf':
                    pathpdffile = os.path.join(pathPdf, pdffile)
                    if info['subcontract']!='' and info['name']!='':
                        if (info['subcontract'] + '_' + info['name']) in pdffile:
                            print('Im find URL file:', pdffile)
                            serverPDFs.append(pdffile)
                            if os.path.getmtime(pathpdffile) >= os.path.getmtime(locFreshFile):
                                serverPDFs.remove(pdffile)
                                check = True
                                print('exists new')
                            if pdffile==nameLocFreshFileWithDate:
                                if os.path.getmtime(pathpdffile) >= os.path.getmtime(locFreshFile):
                                    print('exists same new')
                                    check = True
                                if pdffile in serverPDFs:
                                    serverPDFs.remove(pdffile)


            if not check:
                shutil.copy2(locFreshFile, os.path.join(pathPdf, nameLocFreshFileWithDate))
                x=x+1
                print(QTime.currentTime().toString(), 'uploaded>>>', os.path.join(pathPdf, nameLocFreshFileWithDate))
                self.printd('uploaded >>>> ' +os.path.join(pathPdf, nameLocFreshFileWithDate))
            else:
                pass

            for i in serverPDFs:
                try:
                    os.remove(os.path.join(pathPdf, i))
                    y=y+1
                    self.printd('deleted ---- ' +os.path.join(pathPdf, i))
                    print('deleted >>>' + os.path.join(pathPdf, i))

                except:
                    print('cant remove >>>' + os.path.join(pathPdf, i))
                    self.printd('cant delete !!!! ' + os.path.join(pathPdf, i))
                # else:
                #     print('**CHECK URL PDF PATH PLEASE')
        else:
            print('None file in', path)

        print('         def uploadPDFhide)')
        return x, y


    def uploadTPRhide(self, path, info, pathCheck=None):
        x=0
        y=0
        print('(def uploadTPRhide')
        files = []
        tprLoc = None
        namefiles = []
        serverTPRs = []
        clientPath = os.path.dirname(path)
        clientInfo = createProject.getProjectInfo(clientPath)
        check=None
        for folder in os.listdir(os.path.join(path, '_help')):
            if os.path.isdir(os.path.join(path, '_help', folder)):
                # print(folder)
                if ('тпр').lower() in folder.lower() or ('tpr').lower() in folder.lower():
                    print(folder)
                    tprLoc= os.path.join(path, '_help', folder)
                    for tprfile in os.listdir(tprLoc):
                        if os.path.isfile(os.path.join(tprLoc, tprfile)):
                            name, ext = os.path.splitext(tprfile)
                            if ext=='.pdf':
                                print(name)
                                pathFile= os.path.join(tprLoc,  tprfile)
                                if (info['subcontract'] + '_' + info['name']) in tprfile:
                                    # print('--------------------------------------', tprfile)
                                    files.append(pathFile)
                                    namefile=os.path.basename(pathFile)
                                    namefiles.append(namefile)
        if files:
            locFreshFile = max(files, key=os.path.getmtime)
            nameLocFreshFile = os.path.basename(locFreshFile)
            nameLocFreshFileWithDate =QDate.toString(QDate.currentDate(), Qt.ISODateWithMs) + ' ' + nameLocFreshFile
            print(nameLocFreshFileWithDate)

            if pathCheck:
                pathTpr=pathCheck
            else:
                if not self.inDictionary('TPR_URLpath', info):
                    if info['keytprurl']:
                        pathTpr= clientInfo['TPR_URLpath']
            for urltprfile in os.listdir(pathTpr):
                name, ext = os.path.splitext(urltprfile)
                if ext == '.pdf':
                    # print('----------', urltprfile, '>>>', info['subcontract'] + '_' + info['name'])
                    pathtprfile = os.path.join(pathTpr, urltprfile)
                    if info['subcontract']!='' and info['name']!='':
                        if (info['subcontract'] + '_' + info['name']) in urltprfile:
                            print('Im find TPR file:', urltprfile)
                            serverTPRs.append(urltprfile)
                            if os.path.getmtime(pathtprfile) >= os.path.getmtime(locFreshFile):
                                serverTPRs.remove(urltprfile)
                                print('exists new')
                                check = True
                            print(urltprfile)
                            print(nameLocFreshFileWithDate, urltprfile == nameLocFreshFileWithDate)
                            if urltprfile == nameLocFreshFileWithDate:
                                if os.path.getmtime(pathtprfile) >= os.path.getmtime(locFreshFile):
                                    print('exists same new')
                                    check = True
                                if urltprfile in serverTPRs:
                                    print('serverTPRs.remove(urltprfile)')
                                    serverTPRs.remove(urltprfile)
                                else:
                                    print('NO serverTPRs.remove(urltprfile)')

            if not check:
                shutil.copy2(locFreshFile, os.path.join(pathTpr, nameLocFreshFileWithDate))
                x = x + 1
                self.printd('uploaded >>>> ' +os.path.join(pathTpr, nameLocFreshFileWithDate))
                print(QTime.currentTime().toString(), 'uploaded>>>', os.path.join(pathTpr, nameLocFreshFileWithDate))
            else:
                pass

            for i in serverTPRs:
                try:
                    os.remove(os.path.join(pathTpr, i))
                    y=y+1
                    self.printd('deleted ---- ' +os.path.join(pathTpr, i))
                    print('deleted >>>' + os.path.join(pathTpr, i))

                except:
                    print('cant remove >>>' + os.path.join(pathTpr, i))
                    self.printd('cant remove !!!! ' + os.path.join(pathTpr, i))

        else:
            print('None file in', path)

        print('         def uploadTPRhide)')
        return x, y

    def uploadTZhide(self, path, info, pathCheck=None):
        x=0
        y=0
        print('(def uploadTZhide')
        files = []
        tzLoc = None
        namefiles = []
        serverTZs = []
        clientPath = os.path.dirname(path)
        clientInfo = createProject.getProjectInfo(clientPath)
        check=None
        for folder in os.listdir(os.path.join(path, '_help')):
            if os.path.isdir(os.path.join(path, '_help', folder)):
                # print(folder)
                if ('т3').lower() in folder.lower() or ('tz').lower() in folder.lower():
                    print(folder)
                    tzLoc= os.path.join(path, '_help', folder)
                    for tzfile in os.listdir(tzLoc):
                        if os.path.isfile(os.path.join(tzLoc, tzfile)):
                            name, ext = os.path.splitext(tzfile)
                            if ext=='.pdf':
                                print(name)
                                pathFile= os.path.join(tzLoc,  tzfile)
                                if (info['subcontract'] + '_' + info['name']) in tzfile:
                                    # print('--------------------------------------', tzfile)
                                    files.append(pathFile)
                                    namefile=os.path.basename(pathFile)
                                    namefiles.append(namefile)
        if files:
            locFreshFile = max(files, key=os.path.getmtime)
            nameLocFreshFile = os.path.basename(locFreshFile)
            nameLocFreshFileWithDate =QDate.toString(QDate.currentDate(), Qt.ISODateWithMs) + ' ' + nameLocFreshFile
            print(nameLocFreshFileWithDate)

            if pathCheck:
                print(pathCheck)
                pathTz=pathCheck
            else:
                if not self.inDictionary('TZ_URLpath', info):
                    if info['keytzurl']:
                        pathTz= clientInfo['TZ_URLpath']

            for urltzfile in os.listdir(pathTz):
                name, ext = os.path.splitext(urltzfile)
                if ext == '.pdf':
                    # print('----------', urltzfile, '>>>', info['subcontract'] + '_' + info['name'])
                    pathtzfile = os.path.join(pathTz, urltzfile)
                    if info['subcontract']!='' and info['name']!='':
                        if (info['subcontract'] + '_' + info['name']) in urltzfile:
                            print('Im find TZ file:', urltzfile)
                            serverTZs.append(urltzfile)
                            if os.path.getmtime(pathtzfile) >= os.path.getmtime(locFreshFile):
                                serverTZs.remove(urltzfile)
                                print('exists new')
                                check = True
                            print(urltzfile)
                            print(nameLocFreshFileWithDate, urltzfile == nameLocFreshFileWithDate)
                            if urltzfile == nameLocFreshFileWithDate:
                                if os.path.getmtime(pathtzfile) >= os.path.getmtime(locFreshFile):
                                    print('exists same new')
                                    check = True
                                if urltzfile in serverTZs:
                                    print('serverTZs.remove(urltzfile)')
                                    serverTZs.remove(urltzfile)
                                else:
                                    print('NO serverTZs.remove(urltzfile)')

            if not check:
                shutil.copy2(locFreshFile, os.path.join(pathTz, nameLocFreshFileWithDate))
                x = x + 1
                self.printd('uploaded >>>> ' +os.path.join(pathTz, nameLocFreshFileWithDate))
                print(QTime.currentTime().toString(), 'uploaded>>>', os.path.join(pathTz, nameLocFreshFileWithDate))
            else:
                print('pass')

            for i in serverTZs:
                try:
                    os.remove(os.path.join(pathTz, i))
                    y=y+1
                    self.printd('deleted ---- ' +os.path.join(pathTz, i))
                    print('deleted >>>' + os.path.join(pathTz, i))

                except:
                    print('cant remove >>>' + os.path.join(pathTz, i))
                    self.printd('cant remove !!!! ' + os.path.join(pathTz, i))

        else:
            print('None file in', path)

        print('         def uploadTZhide)')
        return x, y

    def uploadOBRhide(self, path, info, pathCheck=None):
        x=0
        y=0
        print('(def uploadOBRhide')
        files = []
        obrLoc = None
        namefiles = []
        serverOBRs = []
        clientPath = os.path.dirname(path)
        clientInfo = createProject.getProjectInfo(clientPath)
        check=None
        for folder in os.listdir(os.path.join(path, '_help')):
            if os.path.isdir(os.path.join(path, '_help', folder)):
                # print(folder)
                if ('образцы').lower() in folder.lower() or ('obr').lower() in folder.lower():
                    print(folder)
                    obrLoc= os.path.join(path, '_help', folder)
                    for obrfile in os.listdir(obrLoc):
                        if os.path.isfile(os.path.join(obrLoc, obrfile)):
                            name, ext = os.path.splitext(obrfile)
                            if ext=='.pdf':
                                print(name)
                                pathFile= os.path.join(obrLoc,  obrfile)
                                print(info['name'], 'and', info['contract'], 'in', obrfile)
                                if info['name'] in obrfile:
                                    print('files.append ', obrfile)
                                    files.append(pathFile)
                                    namefile=os.path.basename(pathFile)
                                    namefiles.append(namefile)
        if files:
            locFreshFile = max(files, key=os.path.getmtime)
            nameLocFreshFile = os.path.basename(locFreshFile)
            nameLocFreshFileWithDate =QDate.toString(QDate.currentDate(), Qt.ISODateWithMs) + ' ' + nameLocFreshFile
            print(nameLocFreshFileWithDate)

            if pathCheck:
                print(pathCheck)
                pathObr=pathCheck
            else:
                if not self.inDictionary('OBR_URLpath', info):
                    if info['keyobrurl']:
                        pathObr = clientInfo['OBR_URLpath']

            for urlobrfile in os.listdir(pathObr):
                name, ext = os.path.splitext(urlobrfile)
                if ext == '.pdf':
                    print('----------', urlobrfile, '>>>', info['subcontract'] + '_' + info['name'])
                    pathobrfile = os.path.join(pathObr, urlobrfile)
                    if info['subcontract']!='' and info['name']!='':
                        if info['name'] in urlobrfile:
                            print('Im find OBR file:', urlobrfile)
                            serverOBRs.append(urlobrfile)
                            if os.path.getmtime(pathobrfile) >= os.path.getmtime(locFreshFile):
                                serverOBRs.remove(urlobrfile)
                                print('exists new')
                                check = True
                            print(urlobrfile)
                            print(nameLocFreshFileWithDate, urlobrfile == nameLocFreshFileWithDate)
                            if urlobrfile == nameLocFreshFileWithDate:
                                if os.path.getmtime(pathobrfile) >= os.path.getmtime(locFreshFile):
                                    print('exists same new')
                                    check = True
                                if urlobrfile in serverOBRs:
                                    print('serverOBRs.remove(urlobrfile)')
                                    serverOBRs.remove(urlobrfile)


            if not check:
                shutil.copy2(locFreshFile, os.path.join(pathObr, nameLocFreshFileWithDate))
                x = x + 1
                self.printd('uploaded >>>> ' +os.path.join(pathObr, nameLocFreshFileWithDate))
                print(QTime.currentTime().toString(), 'uploaded>>>', os.path.join(pathObr, nameLocFreshFileWithDate))
            else:
                pass

            for i in serverOBRs:
                try:
                    os.remove(os.path.join(pathObr, i))
                    y=y+1
                    self.printd('deleted ---- ' +os.path.join(pathObr, i))
                    print('deleted >>>' + os.path.join(pathObr, i))

                except:
                    print('cant remove >>>' + os.path.join(pathObr, i))
                    self.printd('cant remove !!!! ' + os.path.join(pathObr, i))

        else:
            print('None file in', path)

        print('         def uploadOBRhide)')
        return x, y

    def uploadDWGhide(self, path, info, extn):
        x=0
        # print(path)
        files = []
        for project in os.listdir(path):
            # print('1'+ project)
            if os.path.isfile(os.path.join(path, project)):
                name, ext = os.path.splitext(project)
                if ext==extn:
                    pathFile= os.path.join(path, project)
                    # print(info['subcontract'])

                    if project.startswith(info['subcontract']+'_'+info['name']):
                        # pathFile= os.path.join(path, project)
                        # files=[]
                        files.append(pathFile)

        if files:

            locFreshFile = max(files, key=os.path.getmtime)
            nameLocFreshFile = os.path.basename(locFreshFile)
            # dateLocFreshFile = os.path.getctime(locFreshFile)
            # print(nameLocFreshFile, dateLocFreshFile)
            if self.inDictionary('URLpath', info):
                if os.path.exists(os.path.join(info['URLpath'], nameLocFreshFile)):
                    if os.path.getmtime(os.path.join(info['URLpath'], nameLocFreshFile)) < os.path.getmtime(locFreshFile):

                        print('exists old')
                        try:
                            shutil.copy2(locFreshFile, os.path.join(info['URLpath'], nameLocFreshFile))
                            x=x+1
                            self.printd('uploaded >>>> ' +os.path.join(info['URLpath'], nameLocFreshFile))
                            print(QTime.currentTime().toString(), 'uploaded1>>>', os.path.join(info['URLpath'], nameLocFreshFile))
                        except:
                            withoutExt, ext = os.path.splitext(nameLocFreshFile)
                            nameLocFreshFileCopy = withoutExt + '.copy' + ext
                            shutil.copy2(locFreshFile, os.path.join(info['URLpath'], nameLocFreshFileCopy))
                            x=x+1
                            self.printd('uploaded >>>> ' +os.path.join(info['URLpath'], nameLocFreshFileCopy))
                            print(QTime.currentTime().toString(), 'uploaded2>>>', os.path.join(info['URLpath'], nameLocFreshFileCopy))

                    else:
                        print('exists new')
                else:
                    shutil.copy2(locFreshFile, os.path.join(info['URLpath'], nameLocFreshFile))
                    x=x+1
                    self.printd('uploaded >>>> ' +os.path.join(info['URLpath'], nameLocFreshFile))
                    print(QTime.currentTime().toString(), 'uploaded3>>>', os.path.join(info['URLpath'], nameLocFreshFile))

        else:
            print('None files>>>', path)
        return x

    def uploadhelphide(self, path, info):
        print('(uploadhelphide')
        self.textBrowser_txt.insertPlainText('.')
        x=0
        if '_help' in os.listdir(path):
            print('_help')
            if not info['URLpath']=='':
                print('folder_help')
                f='_help'
                if f in os.listdir(info['URLpath']):
                    print('f in ', info['URLpath'])
                    try:
                        print('try')
                        x = x + self.copyFiles(os.path.join(path, '_help'), os.path.join(info['URLpath'], f))
                        # shutil.copytree(os.path.join(path, '_help'), os.path.join(info['URLpath'], f))
                        self.textBrowser_txt.insertPlainText('.')
                    except:
                        print('!!!!!!!!!! i cant...')
                else:
                    print('else')
                    os.mkdir(os.path.join(info['URLpath'], f))
                    self.printd('create _help folder >>>> ' + os.path.join(info['URLpath'], f))
                    x = x + self.copyFiles(os.path.join(path, '_help'), os.path.join(info['URLpath'], f))
                    print('create folder')


        self.textBrowser_txt.insertPlainText('.')
        return x

    def copyFiles(self, old, new):
        self.textBrowser_txt.insertPlainText('.')
        print('(copyFiles')
        x=0
        for o in os.listdir(old):
            if os.path.isfile(os.path.join(old, o)):
                if not os.path.exists(os.path.join(new, o)):
                    shutil.copy2(os.path.join(old, o), os.path.join(new, o))
                    x=x+1
                    # self.printd('uploaded >>>> ' +
                    self.printd('uploaded >>>> ' + str(os.path.join(new, o)))
                    print('uploaded >>>> '+ os.path.join(new, o))
                else:
                    if os.path.getmtime(os.path.join(new, o)) < os.path.getmtime(os.path.join(old, o)):
                        shutil.copy2(os.path.join(old, o), os.path.join(new, o))
                        x = x + 1
                        print('reloaded >>>> ' + os.path.join(new, o))
                        self.printd('reloaded >>>> ' + str(os.path.join(new, o)))
                    else:
                        print('--------пропуск')

            else:
                if not o.endswith('-'):
                    if os.path.exists(os.path.join(new, o)):
                        self.copyFiles(os.path.join(old, o), os.path.join(new, o))
                        self.textBrowser_txt.insertPlainText('.')
                        print('recursive', os.path.join(new, o))
                    else:
                        os.mkdir(os.path.join(new, o))
                        print('os.mkdir', os.path.join(new, o))
                        self.printd('make folder: ' + str(os.path.join(new, o)))
                        self.copyFiles(os.path.join(old, o), os.path.join(new, o))

                else:
                    print('pass folder ----' + os.path.join(old, o))
        print('    copyFiles)')
        self.textBrowser_txt.insertPlainText('.')

        return x

    def renamerALL(self):
        self.renamer(True)



    def renamer(self, key=None):
        print('(def renemer')
        if key:
            selItems = []
            for i in range(self.projectTree_ltw.topLevelItemCount()):
                selItems.append(self.projectTree_ltw.topLevelItem(i))
        else:

            if self.projectTree_ltw.selectedItems():
                selItems = self.projectTree_ltw.selectedItems()
                print(selItems)
            else:
                selItems = []
                for i in range(self.projectTree_ltw.topLevelItemCount()):
                    selItems.append(self.projectTree_ltw.topLevelItem(i))

        for selItem in selItems:
            selPath = selItem.data(0, 32)
            selInfo = createProject.getProjectInfo(selPath)

            if selInfo['subcontract']=='':
                for f in os.listdir(selPath):
                    fpath= os.path.join(selPath, f)
                    # print(fpath)
                    if self.projectTree_ltw.isProject(fpath):
                        fInfo = createProject.getProjectInfo(fpath)
                        if fInfo['subcontract']=='':
                            for n in os.listdir(fpath):
                                npath=os.path.join(fpath, n)
                                if self.projectTree_ltw.isProject(npath):
                                    nInfo = createProject.getProjectInfo(npath)
                                    if nInfo['subcontract'] == '':
                                        print('None contracts')
                                    else:
                                        print('go to hide 1')
                                        self.renamerhide(npath, nInfo)
                        else:
                            print('go to hide 2')
                            self.renamerhide(fpath, fInfo)
            else:
                print('go to hide 3')
                self.renamerhide(selPath, selInfo)


        print('     def renemer)')


    def renamerhide(self, selPath, selInfo):
        for f in os.listdir(selPath):
            if os.path.isfile(os.path.join(selPath, f)):
                name, ext = os.path.splitext(f)
                if ext=='.bak' or ext=='.idw' or ext=='.err' or ext=='.log':
                    os.remove(os.path.join(selPath, f))
                if ext=='.pdf':
                    names= name.split('_')
                    if not names[-1]=='recover':
                        if not names[-1][-1]==')':
                            nname=names[-1]+'()'
                        else:
                            nname = names[-1]
                        newname= selInfo['subcontract']+'_'+selInfo['name']+'_'+nname+ext
                        # newname= QDate.toString(QDate.currentDate(), Qt.ISODateWithMs) + ' ' + selInfo['subcontract']+'_'+selInfo['name']+'_'+nname+ext
                        os.rename(os.path.join(selPath, f), os.path.join(selPath, newname))

                        print(f, '>>>', newname)
                        # print(newname)

                        # print(names)

    def cleaner_all(self):
        x=0
        data = settings.settingsClass().load()
        basePath = data.get('path')
        if os.path.exists(os.path.join(basePath,'_temp')):
            for d in os.listdir(os.path.join(basePath,'_temp')):
                os.remove(os.path.join(basePath,'_temp', d))
                x=x+1
        self.cleaner(True)
        self.printd(' **** deleted ' + str(x) + ' files in _temp folder ')
        self.textBrowser_txt.insertHtml(html)


    def cleaner(self, key=None):
        x=0
        y=0
        print('(def cleaner')
        if key:
            selItems = []
            for i in range(self.projectTree_ltw.topLevelItemCount()):
                selItems.append(self.projectTree_ltw.topLevelItem(i))
        else:
            if self.projectTree_ltw.selectedItems():
                selItems = self.projectTree_ltw.selectedItems()
            else:
                selItems = []
                for i in range(self.projectTree_ltw.topLevelItemCount()):
                    selItems.append(self.projectTree_ltw.topLevelItem(i))

        for selItem in selItems:
            selPath = selItem.data(0, 32)
            selInfo = createProject.getProjectInfo(selPath)

            if selInfo['subcontract']=='':
                for f in os.listdir(selPath):
                    fpath= os.path.join(selPath, f)
                    # print(fpath)
                    if self.projectTree_ltw.isProject(fpath):
                        fInfo = createProject.getProjectInfo(fpath)
                        if fInfo['subcontract']=='':
                            for n in os.listdir(fpath):
                                npath=os.path.join(fpath, n)
                                if self.projectTree_ltw.isProject(npath):
                                    nInfo = createProject.getProjectInfo(npath)
                                    if nInfo['subcontract'] == '':
                                        print('None contracts')
                                    else:
                                        x1, y1= self.cleanerhide(npath, nInfo)
                                        x=x+x1
                                        y=y+y1
                        else:
                            x1, y1= self.cleanerhide(fpath, fInfo)
                            x = x + x1
                            y = y + y1
            else:
                x1, y1= self.cleanerhide(selPath, selInfo)
                x = x + x1
                y = y + y1
        print(x, 'files,', '        def cleaner)')
        self.printd(' **** deleted ' + str(x) + ' files & leaved ' + str(y) + ' old files) ')
        self.textBrowser_txt.insertHtml(html)


    def cleanerhide(self, selPath, selInfo):
        print('(def cleanerhide')
        x=0
        y=0
        z=0
        files =[]
        fordel =[]
        fordelpdf = []
        fordelname =[]
        for f in os.listdir(selPath):
            if os.path.isfile(os.path.join(selPath, f)):
                name, ext = os.path.splitext(f)
                print(name, ext)
                if ext=='.bak' or ext=='.idw' or ext=='.err' or ext=='.log':
                    os.remove(os.path.join(selPath, f))
                    x=x+1
                    self.printd('--delete: ' + f)
                if ext=='.dwg':
                    print(f)
                    # x=x+1
                    files.append(f)
                    # sorted(files, reverse=1, key=lambda x: os.path.getmtime(os.path.join(selPath, x)))
                    # names= name.split('_')
                    # if not names[-1]=='recover':
                    #     if not names[-1][-1]==')':
                    #         nname=names[-1]+'()'
                    #     else:
                    #         nname = names[-1]
                    #     newname= selInfo['subcontract']+'_'+selInfo['name']+'_'+nname+ext
                    #     # newname= QDate.toString(QDate.currentDate(), Qt.ISODateWithMs) + ' ' + selInfo['subcontract']+'_'+selInfo['name']+'_'+nname+ext
                    #     os.rename(os.path.join(selPath, f), os.path.join(selPath, newname))
                    #
                    #     print(f, '>>>', newname)
        # print(sorted(files, reverse=1, key=lambda l: os.path.getmtime(os.path.join(selPath, l))))

        # print(files)
        files.sort(key=lambda l: os.path.getmtime(os.path.join(selPath, l)), reverse=1)
        # print(files)
        for i, file in enumerate(files):
            if 0 <=i<= 1:
                self.printd('____ leave: ' + file)
                y=y+1
                print('     leave:', file)
            else:
                name, ext= os.path.splitext(file)
                if not name[-1]=='!':
                    fordel.append(os.path.join(selPath, file))
                else:
                    self.printd('____ leave: ' + file)
                    y = y + 1
                    print('     leave:', file)

        for d in fordel:
            name, ext = os.path.splitext(d)
            if os.path.exists(name+'.pdf'):
                fordelpdf.append(name+'.pdf')
                fordelname.append(os.path.basename(name+'.pdf'))
                # print('OK')
            fordelname.append(os.path.basename(d))
            # print('OK')
            try:
                os.remove(d)
                x = x + 1
                print('     Deleted: ', d)
                self.printd('--delete: ' + os.path.basename(d))
            except:
                print('     !!! Cant remove ', d)
                self.printd('??!! cant remove: ' + os.path.basename(d))
        for pdf in fordelpdf:
            try:
                os.remove(pdf)
                x = x + 1
                print('     Deleted: ', pdf)
                self.printd('--delete: ' + os.path.basename(pdf))
            except:
                print('     !!! Cant remove ', pdf)
                self.printd('??!! cant remove: ' + os.path.basename(pdf))

        # print('     for delete:', fordelname)
        print(x, 'files,', '        def cleanerhide)')
        return x, y


    def eventBase(self, what=None):
        if what.button() == Qt.MouseButton.RightButton:
            # print('RIGHT****')
            pos = what.globalPos()
            menu = QMenu()
            menuOpen = QMenu('Open')
            menuCopy = QMenu('Copy')
            menuUpload = QMenu('Upload')
            menuCheck = QMenu('НА ПРОВЕРКУ')
            menuUpload.setIcon(QIcon(logo.picts['upload']))

            menu.addAction(QAction(QIcon(logo.picts['create']), 'Create new project', self, triggered=self.createProject))
            menu.addAction(QAction(QIcon(logo.picts['hammer']), 'Edit project', self, triggered=self.editProject))
            menu.addSeparator()

            menuOpen.addAction(QAction(QIcon(logo.picts['home']), 'Open Local', self, triggered=self.openLOC))
            menuOpen.addAction(QAction(QIcon(logo.picts['url']),'Open URL', self, triggered=self.openURL))
            menuOpen.addAction(QAction(QIcon(logo.picts['pdf']), 'Open PDF', self, triggered=self.openPDF))
            menuOpen.addAction(QAction('Open TPR', self, triggered=self.openTPR))
            menuOpen.addAction(QAction('Open TZ', self, triggered=self.openTZ))
            menuOpen.addAction(QAction('Open OBR', self, triggered=self.openOBR))
            menu.addMenu(menuOpen)
            # menu.addSeparator()
            menuCopy.addAction(QAction(QIcon(logo.picts['home']), 'Copy Local', self, triggered=self.copyLOC))
            menuCopy.addAction(QAction(QIcon(logo.picts['url']), 'Copy URL', self, triggered=self.copyURL))
            menuCopy.addAction(QAction(QIcon(logo.picts['pdf']),'Copy PDF', self, triggered=self.copyPDF))
            menuCopy.addAction(QAction('Copy TPR', self, triggered=self.copyTPR))
            menuCopy.addAction(QAction('Copy TZ', self, triggered=self.copyTZ))
            menuCopy.addAction(QAction('Copy OBR', self, triggered=self.copyOBR))
            menu.addMenu(menuCopy)
            # menu.addSeparator()
            menuUpload.addAction(QAction(QIcon(logo.picts['upload']),'Upload All', self, triggered=self.uploadAll))
            menuUpload.addSeparator()
            menuUpload.addAction(QAction(QIcon(logo.picts['dwg']),'Upload .DWG', self, triggered=self.uploadDWG))
            menuUpload.addAction(QAction(QIcon(logo.picts['pdf']),'Upload .PDF', self, triggered=self.uploadPDF))
            menuUpload.addAction(QAction('Upload TPR', self, triggered=self.uploadTPR))
            menuUpload.addAction(QAction('Upload TZ', self, triggered=self.uploadTZ))
            menuUpload.addAction(QAction('Upload OBR', self, triggered=self.uploadOBR))
            menuUpload.addAction(QAction(QIcon(logo.picts['help']), 'UPLOAD _help', self, triggered=self.uploadhelp))
            menu.addMenu(menuUpload)
            menu.addSeparator()
            menuCheck.addAction(QAction('Create', self, triggered=self.checkCreate))
            menuCheck.addAction(QAction('Upload', self, triggered=self.checkUpload))
            menu.addMenu(menuCheck)
            menu.addSeparator()
            menu.addAction(QAction('_renamer', self, triggered=self.renamer))
            menu.addAction(QAction('_cleaner', self, triggered=self.cleaner))

            a = menu.exec_(pos)


    def eventPDF(self, what=None):
        if what.button() == Qt.MouseButton.RightButton:
            pos = what.globalPos()
            menu = QMenu()
            menu.addAction(QAction('COPY', self, triggered=self.copyPDF))
            menu.addAction(QAction('OPEN', self, triggered=self.openPDF))
            a = menu.exec_(pos)

    def eventTPR(self, what=None):
        if what.button() == Qt.MouseButton.RightButton:
            pos = what.globalPos()
            menu = QMenu()
            menu.addAction(QAction('COPY', self, triggered=self.copyTPR))
            menu.addAction(QAction('OPEN', self, triggered=self.openTPR))
            a = menu.exec_(pos)

    def eventTZ(self, what=None):
        if what.button() == Qt.MouseButton.RightButton:
            pos = what.globalPos()
            menu = QMenu()
            menu.addAction(QAction('COPY', self, triggered=self.copyTZ))
            menu.addAction(QAction('OPEN', self, triggered=self.openTZ))
            a = menu.exec_(pos)

    def eventOBR(self, what=None):
        if what.button() == Qt.MouseButton.RightButton:
            pos = what.globalPos()
            menu = QMenu()
            menu.addAction(QAction('COPY', self, triggered=self.copyOBR))
            menu.addAction(QAction('OPEN', self, triggered=self.openOBR))
            a = menu.exec_(pos)

    def eventURL(self, what=None):
        if what.button() == Qt.MouseButton.RightButton:
            pos = what.globalPos()
            menu = QMenu()
            menu.addAction(QAction('COPY', self, triggered=self.copyURL))
            menu.addAction(QAction('OPEN', self, triggered=self.openURL))
            a = menu.exec_(pos)

    def eventLOC(self, what=None):
        # if what.button() == Qt.MouseButton.LeftButton:
        #     pass
            # оставить дефолтные функции
            # super(myButton, self).mousePressEvent(event)
            # print('LEFT****')
        if what.button() == Qt.MouseButton.RightButton:
            # print('RIGHT****')
            pos = what.globalPos()
            menu = QMenu()

            act1 = QAction('COPY', self)
            act2 = QAction('OPEN', self)
            menu.addAction(QAction('COPY', self, triggered=self.copyLOC))
            menu.addAction(QAction('OPEN', self, triggered=self.openLOC))
            a = menu.exec_(pos)


        # if self.projectTree_ltw.selectedItems():
        #     selItems = self.projectTree_ltw.selectedItems()
        #     selItem = selItems[0]
        #     selPath = selItem.data(0, 32)
        #     selInfo = createProject.getProjectInfo(selPath)
    def copyURL(self, what=None):
        old = self.URL_lbl.text()
        if self.projectTree_ltw.selectedItems():
            selItems = self.projectTree_ltw.selectedItems()
            selItem = selItems[0]
            selPath = selItem.data(0, 32)
            selInfo = createProject.getProjectInfo(selPath)
            if self.inDictionary('URLpath', selInfo):
                path = selInfo['URLpath']
                # old= self.URL_lbl.text()
                clipboard = QApplication.clipboard()
                clipboard.setText(path)
                self.URL_lbl.setText('COPIED!')
                print('COPY URL', path)

                QTimer.singleShot(1000, lambda: self.URL_lbl.setText(old))
            else:
                self.URL_lbl.setText('SELECT ITEM PLEASE')
                QTimer.singleShot(1000, lambda: self.URL_lbl.setText(old))
        else:
            self.URL_lbl.setText('SELECT ITEM PLEASE')
            QTimer.singleShot(1000, lambda: self.URL_lbl.setText('URL'))

    def copyPDF(self, what=None):
        old = self.PDF_lbl.text()
        if self.projectTree_ltw.selectedItems():
            selItems = self.projectTree_ltw.selectedItems()
            selItem = selItems[0]
            selPath = selItem.data(0, 32)
            selInfo = createProject.getProjectInfo(selPath)
            print(selInfo)
            # print('sdfsdf:', self.inDictionary('PDF_URLpath', selInfo))
            if self.inDictionary('PDF_URLpath', selInfo):
                if not selInfo['PDF_URLpath']=='':
                    path = selInfo['PDF_URLpath']
                    # old= self.URL_lbl.text()
                    clipboard = QApplication.clipboard()
                    clipboard.setText(path)
                    self.PDF_lbl.setText('COPIED!')
                    print('COPY PDF', path)
            else:
                if self.inDictionary('keypdfurl', selInfo):
                    if selInfo['keypdfurl']:
                        clientInfo = createProject.getProjectInfo(os.path.dirname(selPath))
                        if self.inDictionary('PDF_URLpath', clientInfo):
                            path = clientInfo['PDF_URLpath']
                            clipboard = QApplication.clipboard()
                            clipboard.setText(path)
                            self.PDF_lbl.setText('COPIED!')
                            print('COPY PDF', path)

            QTimer.singleShot(1000, lambda: self.PDF_lbl.setText(old))
            # else:
            #     self.PDF_lbl.setText('SELECT ITEM PLEASE1')
            #     QTimer.singleShot(1000, lambda: self.PDF_lbl.setText(old))
        else:
            self.PDF_lbl.setText('SELECT ITEM PLEASE')
            QTimer.singleShot(1000, lambda: self.PDF_lbl.setText('PDF'))

    def copyTPR(self, what=None):
        old = self.TPR_lbl.text()
        if self.projectTree_ltw.selectedItems():
            selItems = self.projectTree_ltw.selectedItems()
            selItem = selItems[0]
            selPath = selItem.data(0, 32)
            selInfo = createProject.getProjectInfo(selPath)
            print(selInfo)
            # print('sdfsdf:', self.inDictionary('PDF_URLpath', selInfo))
            if self.inDictionary('TPR_URLpath', selInfo):
                if not selInfo['TPR_URLpath']=='':
                    path = selInfo['TPR_URLpath']
                    # old= self.URL_lbl.text()
                    clipboard = QApplication.clipboard()
                    clipboard.setText(path)
                    self.TPR_lbl.setText('COPIED!')
                    print('COPY TPR', path)
            else:
                if self.inDictionary('keytprurl', selInfo):
                    if selInfo['keytprurl']:
                        clientInfo = createProject.getProjectInfo(os.path.dirname(selPath))
                        if self.inDictionary('TPR_URLpath', clientInfo):
                            path = clientInfo['TPR_URLpath']
                            clipboard = QApplication.clipboard()
                            clipboard.setText(path)
                            self.TPR_lbl.setText('COPIED!')
                            print('COPY TPR', path)

            QTimer.singleShot(1000, lambda: self.TPR_lbl.setText(old))
            # else:
            #     self.PDF_lbl.setText('SELECT ITEM PLEASE1')
            #     QTimer.singleShot(1000, lambda: self.PDF_lbl.setText(old))
        else:
            self.TPR_lbl.setText('SELECT ITEM PLEASE')
            QTimer.singleShot(1000, lambda: self.TPR_lbl.setText('TPR'))

    def copyTZ(self, what=None):
        old = self.TZ_lbl.text()
        if self.projectTree_ltw.selectedItems():
            selItems = self.projectTree_ltw.selectedItems()
            selItem = selItems[0]
            selPath = selItem.data(0, 32)
            selInfo = createProject.getProjectInfo(selPath)
            print(selInfo)
            # print('sdfsdf:', self.inDictionary('PDF_URLpath', selInfo))
            if self.inDictionary('TZ_URLpath', selInfo):
                if not selInfo['TZ_URLpath']=='':
                    path = selInfo['TZ_URLpath']
                    # old= self.URL_lbl.text()
                    clipboard = QApplication.clipboard()
                    clipboard.setText(path)
                    self.TZ_lbl.setText('COPIED!')
                    print('COPY TZ', path)
            else:
                if self.inDictionary('keytzurl', selInfo):
                    if selInfo['keytzurl']:
                        clientInfo = createProject.getProjectInfo(os.path.dirname(selPath))
                        if self.inDictionary('TZ_URLpath', clientInfo):
                            path = clientInfo['TZ_URLpath']
                            clipboard = QApplication.clipboard()
                            clipboard.setText(path)
                            self.TZ_lbl.setText('COPIED!')
                            print('COPY TZ', path)

            QTimer.singleShot(1000, lambda: self.TZ_lbl.setText(old))
            # else:
            #     self.PDF_lbl.setText('SELECT ITEM PLEASE1')
            #     QTimer.singleShot(1000, lambda: self.PDF_lbl.setText(old))
        else:
            self.TZ_lbl.setText('SELECT ITEM PLEASE')
            QTimer.singleShot(1000, lambda: self.TZ_lbl.setText('TZ'))

    def copyOBR(self, what=None):
        old = self.OBR_lbl.text()
        if self.projectTree_ltw.selectedItems():
            selItems = self.projectTree_ltw.selectedItems()
            selItem = selItems[0]
            selPath = selItem.data(0, 32)
            selInfo = createProject.getProjectInfo(selPath)
            print(selInfo)
            # print('sdfsdf:', self.inDictionary('PDF_URLpath', selInfo))
            if self.inDictionary('OBR_URLpath', selInfo):
                if not selInfo['OBR_URLpath']=='':
                    path = selInfo['OBR_URLpath']
                    # old= self.URL_lbl.text()
                    clipboard = QApplication.clipboard()
                    clipboard.setText(path)
                    self.OBR_lbl.setText('COPIED!')
                    print('COPY OBR', path)
            else:
                if self.inDictionary('keyobrurl', selInfo):
                    if selInfo['keyobrurl']:
                        clientInfo = createProject.getProjectInfo(os.path.dirname(selPath))
                        if self.inDictionary('OBR_URLpath', clientInfo):
                            path = clientInfo['OBR_URLpath']
                            clipboard = QApplication.clipboard()
                            clipboard.setText(path)
                            self.OBR_lbl.setText('COPIED!')
                            print('COPY OBR', path)

            QTimer.singleShot(1000, lambda: self.OBR_lbl.setText(old))
            # else:
            #     self.PDF_lbl.setText('SELECT ITEM PLEASE1')
            #     QTimer.singleShot(1000, lambda: self.PDF_lbl.setText(old))
        else:
            self.OBR_lbl.setText('SELECT ITEM PLEASE')
            QTimer.singleShot(1000, lambda: self.OBR_lbl.setText('Образцы'))

    def copyLOC(self, what=None):
        old = self.LOC_lbl.text()

        if self.projectTree_ltw.selectedItems():
            selItems = self.projectTree_ltw.selectedItems()
            selItem = selItems[0]
            path = selItem.data(0, 32)
            clipboard = QApplication.clipboard()
            clipboard.setText(path)
            self.LOC_lbl.setText('COPIED!')
            print('COPY LOC', path)

            QTimer.singleShot(1000, lambda: self.LOC_lbl.setText(old))
        else:
            self.LOC_lbl.setText('SELECT ITEM PLEASE')
            QTimer.singleShot(1000, lambda: self.LOC_lbl.setText(old))

    def openURL(self, what=None):
        old = self.LOC_lbl.text()
        if self.projectTree_ltw.selectedItems():
            selItems = self.projectTree_ltw.selectedItems()
            selItem = selItems[0]
            selPath = selItem.data(0, 32)
            selInfo = createProject.getProjectInfo(selPath)
            if self.inDictionary('URLpath', selInfo):
                path = selInfo['URLpath']
                print('OPEN URL', path)
                webbrowser.open(path)
            else:
                self.URL_lbl.setText('SELECT ITEM PLEASE')
                QTimer.singleShot(1000, lambda: self.URL_lbl.setText(old))
        else:
            self.URL_lbl.setText('SELECT ITEM PLEASE')
            QTimer.singleShot(1000, lambda: self.URL_lbl.setText(old))
        # path= item.data(0, 32)
        # webbrowser.open(path)

    def openPDF(self, what=None):
        old = self.PDF_lbl.text()
        if self.projectTree_ltw.selectedItems():
            selItems = self.projectTree_ltw.selectedItems()
            selItem = selItems[0]
            selPath = selItem.data(0, 32)
            selInfo = createProject.getProjectInfo(selPath)
            if self.inDictionary('PDF_URLpath', selInfo):
                path = selInfo['PDF_URLpath']
                print('OPEN PDF', path)
                webbrowser.open(path)
            else:
                if self.inDictionary('keypdfurl', selInfo):
                    if selInfo['keypdfurl']:
                        clientInfo = createProject.getProjectInfo(os.path.dirname(selPath))
                        if self.inDictionary('PDF_URLpath', clientInfo):
                            path = clientInfo['PDF_URLpath']
                            print('OPEN PDF', path)
                            webbrowser.open(path)
                        else:
                            self.PDF_lbl.setText('SELECT ITEM PLEASE')
                            QTimer.singleShot(1000, lambda: self.PDF_lbl.setText(old))
                    else:
                        self.PDF_lbl.setText('SELECT ITEM PLEASE')
                        QTimer.singleShot(1000, lambda: self.PDF_lbl.setText(old))
                else:
                    self.PDF_lbl.setText('SELECT ITEM PLEASE')
                    QTimer.singleShot(1000, lambda: self.PDF_lbl.setText(old))
        else:
            self.PDF_lbl.setText('SELECT ITEM PLEASE')
            QTimer.singleShot(1000, lambda: self.PDF_lbl.setText(old))
        # path= item.data(0, 32)
        # webbrowser.open(path)


    def openTPR(self, what=None):
        old = self.TPR_lbl.text()
        if self.projectTree_ltw.selectedItems():
            selItems = self.projectTree_ltw.selectedItems()
            selItem = selItems[0]
            selPath = selItem.data(0, 32)
            selInfo = createProject.getProjectInfo(selPath)
            if self.inDictionary('TPR_URLpath', selInfo):
                path = selInfo['TPR_URLpath']
                print('OPEN TPR', path)
                webbrowser.open(path)
            else:
                if self.inDictionary('keytprurl', selInfo):
                    if selInfo['keytprurl']:
                        clientInfo = createProject.getProjectInfo(os.path.dirname(selPath))
                        if self.inDictionary('TPR_URLpath', clientInfo):
                            path = clientInfo['TPR_URLpath']
                            print('OPEN TPR', path)
                            webbrowser.open(path)
                        else:
                            self.TPR_lbl.setText('SELECT ITEM PLEASE')
                            QTimer.singleShot(1000, lambda: self.TPR_lbl.setText(old))
                    else:
                        self.TPR_lbl.setText('SELECT ITEM PLEASE')
                        QTimer.singleShot(1000, lambda: self.TPR_lbl.setText(old))
                else:
                    self.TPR_lbl.setText('SELECT ITEM PLEASE')
                    QTimer.singleShot(1000, lambda: self.TPR_lbl.setText(old))
        else:
            self.TPR_lbl.setText('SELECT ITEM PLEASE')
            QTimer.singleShot(1000, lambda: self.TPR_lbl.setText(old))
        # path= item.data(0, 32)
        # webbrowser.open(path)


    def openTZ(self, what=None):
        old = self.TZ_lbl.text()
        if self.projectTree_ltw.selectedItems():
            selItems = self.projectTree_ltw.selectedItems()
            selItem = selItems[0]
            selPath = selItem.data(0, 32)
            selInfo = createProject.getProjectInfo(selPath)
            if self.inDictionary('TZ_URLpath', selInfo):
                path = selInfo['TZ_URLpath']
                print('OPEN TZ', path)
                webbrowser.open(path)
            else:
                if self.inDictionary('keytzurl', selInfo):
                    if selInfo['keytzurl']:
                        clientInfo = createProject.getProjectInfo(os.path.dirname(selPath))
                        if self.inDictionary('TZ_URLpath', clientInfo):
                            path = clientInfo['TZ_URLpath']
                            print('OPEN TZ', path)
                            webbrowser.open(path)
                        else:
                            self.TZ_lbl.setText('SELECT ITEM PLEASE')
                            QTimer.singleShot(1000, lambda: self.TZ_lbl.setText(old))
                    else:
                        self.TZ_lbl.setText('SELECT ITEM PLEASE')
                        QTimer.singleShot(1000, lambda: self.TZ_lbl.setText(old))
                else:
                    self.TZ_lbl.setText('SELECT ITEM PLEASE')
                    QTimer.singleShot(1000, lambda: self.TZ_lbl.setText(old))
        else:
            self.TZ_lbl.setText('SELECT ITEM PLEASE')
            QTimer.singleShot(1000, lambda: self.TZ_lbl.setText(old))

    def openOBR(self, what=None):
        old = self.OBR_lbl.text()
        if self.projectTree_ltw.selectedItems():
            selItems = self.projectTree_ltw.selectedItems()
            selItem = selItems[0]
            selPath = selItem.data(0, 32)
            selInfo = createProject.getProjectInfo(selPath)
            if self.inDictionary('OBR_URLpath', selInfo):
                path = selInfo['OBR_URLpath']
                print('OPEN OBR', path)
                webbrowser.open(path)
            else:
                if self.inDictionary('keyobrurl', selInfo):
                    if selInfo['keyobrurl']:
                        clientInfo = createProject.getProjectInfo(os.path.dirname(selPath))
                        if self.inDictionary('OBR_URLpath', clientInfo):
                            path = clientInfo['OBR_URLpath']
                            print('OPEN OBR', path)
                            webbrowser.open(path)
                        else:
                            self.OBR_lbl.setText('SELECT ITEM PLEASE')
                            QTimer.singleShot(1000, lambda: self.OBR_lbl.setText(old))
                    else:
                        self.OBR_lbl.setText('SELECT ITEM PLEASE')
                        QTimer.singleShot(1000, lambda: self.OBR_lbl.setText(old))
                else:
                    self.OBR_lbl.setText('SELECT ITEM PLEASE')
                    QTimer.singleShot(1000, lambda: self.OBR_lbl.setText(old))
        else:
            self.OBR_lbl.setText('SELECT ITEM PLEASE')
            QTimer.singleShot(1000, lambda: self.OBR_lbl.setText(old))



    def openLOC(self, what=None):
        old = self.LOC_lbl.text()
        if self.projectTree_ltw.selectedItems():
            selItems = self.projectTree_ltw.selectedItems()
            selItem = selItems[0]
            path = selItem.data(0, 32)
            print('OPEN LOC', path)
            webbrowser.open(path)
        else:
            self.LOC_lbl.setText('SELECT ITEM PLEASE')
            QTimer.singleShot(1000, lambda: self.LOC_lbl.setText(old))

        # path= item.data(0, 32)
        # webbrowser.open(path)

    def checkCreate(self, uploadPDF=None, uploadTPR=None, uploadTZ=None, uploadOBR=None):
        template = json.load(open(templateEditorCheck.templateCheckFile))
        dataPath = settings.settingsClass().load()
        checkPath = dataPath.get('checkpath')
        if self.projectTree_ltw.selectedItems():
            selItems = self.projectTree_ltw.selectedItems()
            selItem = selItems[0]
            selPath = selItem.data(0, 32)
            selInfo = createProject.getProjectInfo(selPath)
            if selInfo['subcontract']!='':
                proverkaName = selInfo['contract'] + '_' + selInfo['subcontract'] + ' ' + selInfo['client'] + ' (' + selInfo['name'] + ')'
                print(proverkaName)

                if os.path.exists(os.path.join(checkPath, proverkaName)):
                    print(os.path.join(checkPath, proverkaName), 'Yes')
                else:
                    print('No')
                    self.buildCheckFolders(checkPath, template, proverkaName)

                if uploadPDF:
                    self.uploadPDF(None, os.path.join(checkPath, proverkaName, 'Эскизы'))
                if uploadTPR:
                    self.uploadTPR(None, os.path.join(checkPath, proverkaName, 'ТПР или фото помещения с ремонтом'))
                if uploadTZ:
                    self.uploadTZ(None, os.path.join(checkPath, proverkaName, 'Дополнительно'))
                if uploadOBR:
                    self.uploadOBR(None, os.path.join(checkPath, proverkaName, 'Образцы'))

    def buildCheckFolders(self, root, folders, proverkaName=None):
        print(folders)
        for f in folders:
            if f['name'] == '*name*':
                fname = proverkaName
            else:
                fname = f['name']
            full = os.path.join(root, fname)
            self.mkCheckFolder(full)
            self.buildCheckFolders(full, f['children'])

    def mkCheckFolder(self, path):
        try:
            # os.mkdir(path)
            os.makedirs(path)
            return True
        except:
            return False

    def checkUpload(self):
        self.checkUploadPDF()
        self.checkUploadTPR()
        self.checkUploadTZ()
        self.checkUploadOBR()

    def checkUploadPDF(self):
        self.checkCreate(True)

    def checkUploadTPR(self):
        self.checkCreate(None, True)

    def checkUploadTZ(self):
        self.checkCreate(None, None, True)

    def checkUploadOBR(self):
        self.checkCreate(None, None, None, True)

    def inDictionary(self, key, dict):
        if key in dict:
            return dict[key]
        else:
            return ''

    def openProject(self, item):
        path= item.data(0, 32)
        webbrowser.open(path)


    def probuem(self):
        pass
        # print(self.projectTree_ltw.

    def treeRight(self, what):
        print(what)

# class EmittingStream(QTextBrowser):
#      textWritten= QTextBrowser.signa






if __name__ == '__main__':
    app= QApplication([])
    w= projectManagerClass()
    w.show()
    app.exec_()
