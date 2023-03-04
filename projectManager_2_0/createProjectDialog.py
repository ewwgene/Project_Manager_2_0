from PySide2.QtCore import *
from PySide2.QtWidgets import *
import createProject_ui as ui
import createProject, settings, projectTreeWidget
import os

data = settings.settingsClass().load()
basePath = data.get('path')
newClient= 'New Client...'
newContract= 'New Contract...'
defClient_lne= 'Фамилия...'
defObjectName_lbl= 'Место...'
defContract_lne= 'Название проекта...'
defPath_lbl= 'Путь на сервере...'

unknown= 'unknown'





class projectManagerClass(QDialog, ui.Ui_createDialog,):
    def __init__(self, parent):
        super(projectManagerClass, self).__init__(parent)
        self.setupUi(self)

        #connects
        self.create_btn.clicked.connect(self.doCreate)
        self.cancel_btn.clicked.connect(self.reject)
        self.client_cbb.currentTextChanged.connect(self.signalClient)
        self.contract_cbb.textActivated.connect(self.signalContract)
        self.PdfCheckBox_chb.setChecked(0)
        self.PdfCheckBox_chb.stateChanged.connect(self.signalPDF)
        self.TprCheckBox_chb.setChecked(0)
        self.TprCheckBox_chb.stateChanged.connect(self.signalTPR)
        self.TzCheckBox_chb.setChecked(0)
        self.TzCheckBox_chb.stateChanged.connect(self.signalTZ)
        self.ObrCheckBox_chb.setChecked(0)
        self.ObrCheckBox_chb.stateChanged.connect(self.signalOBR)
        # self.PdfCheckBox_chb.setVisible(0)
        self.keyEdit = False
        self.checkArchive=False
        self.Archive0_chb.stateChanged.connect(self.setCheckArchive)
        self.Archive_chb.setDisabled(1)
        # self.checkedPDF()
        #start
        # self.startBox()

    # def checkedPDF(self, what=None):
    #     if what:
    #         self.pdfPathServer_lbl.setEnabled(0)
    #         print('000000000000000000000000000000')
    #     else:
    #         self.pdfPathServer_lbl.setEnabled(1)
    #         print('11111111111111111111111111111111')

    def setCheckArchive(self):
        if self.Archive0_chb.isChecked():
            self.checkArchive=True
            self.Archive_chb.setEnabled(1)
        else:
            self.checkArchive = False
            self.Archive_chb.setDisabled(1)

    def startBox(self, keyEdit=False, selPath=None):


        self.keyEdit=keyEdit
        print('(startBox', keyEdit, selPath)
        self.client_cbb.blockSignals(1)
        self.client_cbb.addItem(newClient)
        self.contract_cbb.addItem(newContract)
        # self.PdfCheckBox_chb.setVisible(1)
        # self.TprCheckBox_chb.setVisible(1)
        # self.TzCheckBox_chb.setVisible(1)

        # self.date_dte.setDate(QDate.currentDate())
        self.clearUI()
        # data = settings.settingsClass().load()
        # basePath = data.get('path')
        print('-fillClient:')
        if basePath:
            if os.path.exists(basePath):
                for f in os.listdir(basePath):
                    fullPath = os.path.join(basePath, f)
                    if projectTreeWidget.projectTreeClass().isProject(fullPath):
                        info = createProject.getProjectInfo(fullPath)
                        self.client_cbb.addItem(info['client'])
                        print('     --add:', info['client'])
        self.client_cbb.blockSignals(0)
        if keyEdit:
            self.startKeyEdit(selPath)

        self.name_lbl.selectAll()
        self.name_lbl.setFocus()
        print('         startBox)')

    def startKeyEdit(self, selPath):
        print('(startKeyEdit', selPath)
        info = createProject.getProjectInfo(selPath)
        if self.keyEdit:
            if self.keyEdit == 2 or self.keyEdit == 3:
                if self.keyEdit == 3:
                    self.name_lbl.setText(info['name'])
                    print(' --set', self.name_lbl.text())
                    self.subContract_lne.setText(info['subcontract'])
                    print(' --set', self.subContract_lne.text())
                    # self.PdfCheckBox_chb.setVisible(1)
                    # self.TprCheckBox_chb.setVisible(1)
                    # self.TzCheckBox_chb.setVisible(1)

            self.create_btn.setText('Edit')
            # self.client_cbb.setDisabled(1)
            self.create_btn.clicked.connect(self.doEdit)


        print('     startKeyEdit)')

    def setArchive(self, info):
        if self.inDictionary('archive', info):
            if info['archive']:
                # print('11111111111111111111111111111111111111ive')
                self.Archive_chb.setChecked(1)
            else:
                self.Archive_chb.setChecked(0)
        else:
            self.Archive_chb.setChecked(0)
            # print('000000000000000000000000000000000000NO archive')



    def fillPathes(self, client=None, contract=None, subcontract=None, path=None, info=None):
        print('(fillPathes', client, contract, subcontract, path)
        if info:
            print('info YES')
        else:
            print('info NO')

        # if self.keyEdit:
        self.PdfCheckBox_chb.setVisible(0)
        self.TprCheckBox_chb.setVisible(0)
        self.TzCheckBox_chb.setVisible(0)
        self.ObrCheckBox_chb.setVisible(0)
        # else:
            # self.PdfCheckBox_chb.setVisible(1)
            # self.TprCheckBox_chb.setVisible(1)
            # self.TzCheckBox_chb.setVisible(1)
        # if self.keyEdit:
        print('OK')
        if not info:
            print('OK1')
            if contract and contract!=newContract:
                print('OK3')
                object= self.searchObject(client, contract)
                if not object=='':
                    contractName= contract+'_'+object
                else:
                    contractName = contract

                if subcontract:
                    self.PdfCheckBox_chb.setVisible(1)
                    self.TprCheckBox_chb.setVisible(1)
                    self.TzCheckBox_chb.setVisible(1)
                    self.ObrCheckBox_chb.setVisible(1)

                    path = os.path.join(basePath, client, contractName, subcontract)
                    info = createProject.getProjectInfo(path)
                    self.fillURL(info)
                    print(path)
                    if self.inDictionary('keypdfurl', info):
                        if not info['keypdfurl']=='':
                            self.signalPDF(info['keypdfurl'])
                    else:
                        self.fillPDF(info)

                    if self.inDictionary('keytprurl', info):
                        if not info['keytprurl']=='':
                            self.signalTPR(info['keytprurl'])
                    else:
                        self.fillTPR(info)

                    if self.inDictionary('keytzurl', info):
                        if not info['keytzurl']=='':
                            self.signalTZ(info['keytzurl'])
                    else:
                        self.fillTZ(info)

                    if self.inDictionary('keyobrurl', info):
                        if not info['keyobrurl']=='':
                            self.signalOBR(info['keyobrurl'])
                    else:
                        self.fillOBR(info)
                    self.setArchive(info)

                else:
                    path=os.path.join(basePath, client, contractName)
                    info = createProject.getProjectInfo(path)
                    self.fillURL(info)
                    self.fillPDF(info)
                    self.fillTPR(info)
                    self.fillTZ(info)
                    self.fillOBR(info)
                    self.setArchive(info)

            else:
                path = os.path.join(basePath, client)
                info = createProject.getProjectInfo(path)
        else:
            if self.keyEdit==1:
                self.label_8.setVisible(0)
                self.label_9.setVisible(0)
                self.label_10.setVisible(0)
                self.label_11.setVisible(0)
                self.pdfPathServer_lbl.setVisible(0)
                self.tprPathServer_lbl.setVisible(0)
                self.tzPathServer_lbl.setVisible(0)
                self.PdfCheckBox_chb.setVisible(0)
                self.TprCheckBox_chb.setVisible(0)
                self.TzCheckBox_chb.setVisible(0)
                self.ObrCheckBox_chb.setVisible(0)

            if not info['subcontract']=='':
                self.PdfCheckBox_chb.setVisible(1)
                self.TprCheckBox_chb.setVisible(1)
                self.TzCheckBox_chb.setVisible(1)
                self.ObrCheckBox_chb.setVisible(1)
                if self.inDictionary('keypdfurl', info):
                    if info['keypdfurl']:
                        print('set checked pdf')
                        self.PdfCheckBox_chb.setChecked(1)
                        # self.signalPDF(info['keypdfurl'])
                if self.inDictionary('keytprurl', info):
                    if info['keytprurl']:
                        print('set checked tpr', info['keytprurl'])
                        self.TprCheckBox_chb.setChecked(1)
                        # self.signalTPR(info['keytprurl'])
                if self.inDictionary('keytzurl', info):
                    if info['keytzurl']:
                        print('set checked tz', info['keytzurl'])
                        self.TzCheckBox_chb.setChecked(1)
                if self.inDictionary('keyobrurl', info):
                    if info['keyobrurl']:
                        print('set checked obr', info['keyobrurl'])
                        self.ObrCheckBox_chb.setChecked(1)
                self.setArchive(info)
                self.fillURL(info)

            else:
                # self.PdfCheckBox_chb.setVisible(1)
                # self.TprCheckBox_chb.setVisible(1)
                # self.TzCheckBox_chb.setVisible(1)
                self.fillURL(info)
                self.fillPDF(info)
                self.fillTPR(info)
                self.fillTZ(info)
                self.fillOBR(info)
                self.setArchive(info)


        print('     fillPathes)')

    def signalPDF(self, signal):
        print('signal pdf ', signal)
        client= self.client_cbb.currentText()
        contract= self.contract_cbb.currentText()
        object= self.searchObject(client, contract)
        if not object == '':
            contractName = contract + '_' + object
        else:
            contractName = contract
        subcontract= self.subContract_lne.text()
        namesubcontract= self.name_lbl.text()
        if not namesubcontract==defContract_lne:
            fullnamesubcontract= subcontract+'_'+namesubcontract
            if signal==0:
                path = os.path.join(basePath, client, contractName, fullnamesubcontract)
                info = createProject.getProjectInfo(path)
                self.pdfPathServer_lbl.setEnabled(1)
                self.fillPDF(info)
                # self.pdfPathServer_lbl.selectAll()
                # self.pdfPathServer_lbl.setFocus()
            else:
                path = os.path.join(basePath, client, contractName)
                info = createProject.getProjectInfo(path)
                self.fillPDF(info)
                self.pdfPathServer_lbl.setEnabled(0)
        else:
            print('error')


    def signalTPR(self, signal):
        print('signal tpr ', signal)
        client= self.client_cbb.currentText()
        contract= self.contract_cbb.currentText()
        object= self.searchObject(client, contract)
        if not object == '':
            contractName = contract + '_' + object
        else:
            contractName = contract
        subcontract= self.subContract_lne.text()
        namesubcontract= self.name_lbl.text()
        if not namesubcontract==defContract_lne:
            fullnamesubcontract= subcontract+'_'+namesubcontract
            if signal==0:
                path = os.path.join(basePath, client, contractName, fullnamesubcontract)
                info = createProject.getProjectInfo(path)
                self.tprPathServer_lbl.setEnabled(1)
                self.fillTPR(info)
                # self.pdfPathServer_lbl.selectAll()
                # self.pdfPathServer_lbl.setFocus()
            else:
                path = os.path.join(basePath, client, contractName)
                info = createProject.getProjectInfo(path)
                self.fillTPR(info)
                self.tprPathServer_lbl.setEnabled(0)
        else:
            print('error')

    def signalTZ(self, signal):
        print('signal tz ', signal)
        client= self.client_cbb.currentText()
        contract= self.contract_cbb.currentText()
        object= self.searchObject(client, contract)
        if not object == '':
            contractName = contract + '_' + object
        else:
            contractName = contract
        subcontract= self.subContract_lne.text()
        namesubcontract= self.name_lbl.text()
        if not namesubcontract==defContract_lne:
            fullnamesubcontract= subcontract+'_'+namesubcontract
            if signal==0:
                path = os.path.join(basePath, client, contractName, fullnamesubcontract)
                info = createProject.getProjectInfo(path)
                self.tzPathServer_lbl.setEnabled(1)
                self.fillTZ(info)
                # self.pdfPathServer_lbl.selectAll()
                # self.pdfPathServer_lbl.setFocus()
            else:
                path = os.path.join(basePath, client, contractName)
                info = createProject.getProjectInfo(path)
                self.fillTZ(info)
                self.tzPathServer_lbl.setEnabled(0)
        else:
            print('error')

    def signalOBR(self, signal):
        print('signal obr ', signal)
        client= self.client_cbb.currentText()
        contract= self.contract_cbb.currentText()
        object= self.searchObject(client, contract)
        if not object == '':
            contractName = contract + '_' + object
        else:
            contractName = contract
        subcontract= self.subContract_lne.text()
        namesubcontract= self.name_lbl.text()
        if not namesubcontract==defContract_lne:
            fullnamesubcontract= subcontract+'_'+namesubcontract
            if signal==0:
                path = os.path.join(basePath, client, contractName, fullnamesubcontract)
                info = createProject.getProjectInfo(path)
                self.obrPathServer_lbl.setEnabled(1)
                self.fillOBR(info)
                # self.pdfPathServer_lbl.selectAll()
                # self.pdfPathServer_lbl.setFocus()
            else:
                path = os.path.join(basePath, client, contractName)
                info = createProject.getProjectInfo(path)
                self.fillOBR(info)
                self.obrPathServer_lbl.setEnabled(0)
        else:
            print('error')


    def fillPDF(self, info):
        print('(fillPDF', info)

        if self.inDictionary('PDF_URLpath', info):
            if not info['PDF_URLpath']=='':
                self.pdfPathServer_lbl.setText(info['PDF_URLpath'])
                print(' --set PDF_URLpath:', info['PDF_URLpath'])
            else:
                self.pdfPathServer_lbl.setText(defPath_lbl)
                print(' --set default PDF_URLpath')
        else:
            self.pdfPathServer_lbl.setText(defPath_lbl)
            print(' --set default PDF_URLpath')
            #

    def fillTPR(self, info):
        print('(fillTPR', info)

        if self.inDictionary('TPR_URLpath', info):
            if not info['TPR_URLpath']=='':
                self.tprPathServer_lbl.setText(info['TPR_URLpath'])
                print(' --set TPR_URLpath:', info['TPR_URLpath'])
            else:
                self.tprPathServer_lbl.setText(defPath_lbl)
                print(' --set default TPR_URLpath')
        else:
            self.tprPathServer_lbl.setText(defPath_lbl)
            print(' --set default TPR_URLpath')
        #     #

    def fillTZ(self, info):
        print('(fillTPR', info)
        if self.inDictionary('TZ_URLpath', info):
            if not info['TZ_URLpath']=='':
                self.tzPathServer_lbl.setText(info['TZ_URLpath'])
                print(' --set TZ_URLpath:', info['TZ_URLpath'])
            else:
                self.tzPathServer_lbl.setText(defPath_lbl)
                print(' --set default TZ_URLpath')
        else:
            self.tzPathServer_lbl.setText(defPath_lbl)
            print(' --set default TZ_URLpath')
            #

    def fillOBR(self, info):
        print('(fillOBR', info)
        if self.inDictionary('OBR_URLpath', info):
            if not info['OBR_URLpath']=='':
                self.obrPathServer_lbl.setText(info['OBR_URLpath'])
                print(' --set OBR_URLpath:', info['OBR_URLpath'])
            else:
                self.obrPathServer_lbl.setText(defPath_lbl)
                print(' --set default OBR_URLpath')
        else:
            self.obrPathServer_lbl.setText(defPath_lbl)
            print(' --set default OBR_URLpath')
            #

    def fillURL(self, info):
        if self.inDictionary('URLpath', info):
            if not info['URLpath'] == '':
                self.pathServer_lbl.setText(info['URLpath'])
                print(' --set URLpath:', info['URLpath'])
            else:
                self.pathServer_lbl.setText(defPath_lbl)
                print(' --set default URLpath')
        else:
            self.pathServer_lbl.setText(defPath_lbl)
            print(' --set default URLpath')
            #
            #     print('         fillPathes)')








    def createProject(self, client, contract=None, object=None, subcontract=None, path=None):
        print('(createProject:', client, contract, object, subcontract, path, 'keyEdit=', self.keyEdit)

        self.clearUI()


        if not client == newClient:
            parentPath = os.path.join(basePath, client)
        else:
            parentPath = basePath
        # print('OLD', parentPath)
        # print('NEW', selPath)

        self.fillContracts(parentPath)
        self.chageUI(client, contract, object, subcontract, path)


        print('     createProject)')


    def editProject(self, parent, child=None, subcontract=None):
        print('(editProject:', parent, child, subcontract)

        self.clearUI()
        self.create_btn.setText('Edit')
        # self.client_cbb.setDisabled(1)
        self.create_btn.clicked.connect(self.doEdit)





    def fillContracts(self, clientPath):
        print('(fillContracts')

        # self.contract_cbb.clear()
        # self.contract_cbb.addItem('New Contract')
        # print (parentPath)
        for c in os.listdir(clientPath):
            contractPath = os.path.join(clientPath, c)
            if projectTreeWidget.projectTreeClass().isProject(contractPath):
                info = createProject.getProjectInfo(contractPath)
                self.contract_cbb.addItem(info['contract'])
                print('--', info['contract'])
                # print(info['contract'])

        print('     fillContracts)')


    def signalClient(self, signal):
        print('signalCLIENT: ', signal)
        self.createProject(signal)
        # if not self.keyEdit:
        if signal == newClient:
            self.client_lne.selectAll()
            self.client_lne.setFocus()
        else:
            self.contract_lne.setSelection(3, 6)
            self.contract_lne.setFocus()
        # else:

    def searchObject(self, client, signal):
        if not client:
            client = self.client_cbb.currentText()
        print('**** search object in: ', client)
        object = ''
        for contract in os.listdir(os.path.join(basePath, client)):
            if os.path.isdir(os.path.join(basePath, client, contract)):
                if contract.startswith(signal):
                    info = createProject.getProjectInfo(os.path.join(basePath, client, contract))
                    if self.inDictionary('objectName', info):
                        if not info['objectName'] == '':
                            object = info['objectName']
        print('**** object is: ', object)
        return object

    # def makeFullNameClient(self, contract, object):



    def signalContract(self, signal):
        print('****signalCONTRACT: ', signal)
        if not signal == newContract:
            object = self.searchObject(None, signal)
            client = self.client_cbb.currentText()
            print('output: ', client, signal, object)
            self.chageUI(client, signal, object)
            self.subContract_lne.selectAll()
            self.subContract_lne.setFocus()

        else:
            client = self.client_cbb.currentText()
            # signal = self. contract_cbb.currentText()
            self.chageUI(client)
            self.contract_lne.setSelection(3,6)
            print('??????????')
            self.contract_lne.setFocus()



    def chageUI(self, client=None, contract=None, object=None, subcontract=None, selPath=None):
        print('input: ', client, contract, object, subcontract, selPath)
        contractName=None
        info=None
        if contract:
            if not object:
                object = self.searchObject(client, contract)
            if not object=='' or object==None:
                contractName = contract + '_' + object
            else:
                contractName = contract


        print('(CHAGE UI')
        print('     ', client, contractName, subcontract, 'KeyEdit=', self.keyEdit, 'SEL=', selPath)
        uiMask = {'client_lne': 0,
                  'contract_lne': 0,
                  'objectName': 0
                   }

        if client:
            if not client == newClient:
                if contract:
                    if subcontract:
                        subcontractPath = selPath
                        clientPath = os.path.dirname(subcontractPath)
                        # print(client, parent, child, subcontract)
                        info = createProject.getProjectInfo(subcontractPath)
                        # fatherInfo = createProject.getProjectInfo(os.path.dirname(parentPath))
                        uiMask['client_lne'] = 0
                        uiMask['contract_lne'] = 0
                        uiMask['objectName'] = 1
                        self.PdfCheckBox_chb.setVisible(1)
                        self.TprCheckBox_chb.setVisible(1)
                        self.TzCheckBox_chb.setVisible(1)
                        self.ObrCheckBox_chb.setVisible(1)
                        self.changeVisibleUI(client, contract, subcontract, info, uiMask)

                    else:
                        if not subcontract == newContract:
                            for cont in os.listdir(os.path.join(basePath, client)):
                                if os.path.isdir(os.path.join(basePath, client, cont)):
                                    if selPath:
                                        if selPath==os.path.join(basePath, client, cont):
                                            contractPath=selPath
                                            print(cont, 'OK_0')
                                        else:
                                            print('ERROR1')
                                    else:
                                        if cont.startswith(contract):
                                            contractPath = os.path.join(basePath, client, cont)
                                            print(cont, 'OK2')
                                        else:
                                            print('ERROR2')
                                # else:

                                    # contractPath = os.path.join(basePath, client, cont)
                            # contractPath = os.path.join(basePath, client, contractName)
                            info = createProject.getProjectInfo(contractPath)
                            uiMask['client_lne'] = 0
                            uiMask['contract_lne'] = 0
                            uiMask['objectName'] = 0
                            self.changeVisibleUI(client, contract, None, info, uiMask)
                        else:
                            client = self.client_cbb.currentText()
                            clientPath = os.path.join(basePath, client)
                            info = createProject.getProjectInfo(clientPath)
                            uiMask['client_lne'] = 0
                            uiMask['contract_lne'] = 1
                            uiMask['objectName'] = 1
                            self.changeVisibleUI(client, None, None, info, uiMask)
                else:
                    clientPath = os.path.join(basePath, client)
                    info = createProject.getProjectInfo(clientPath)
                    uiMask['client_lne'] = 0
                    uiMask['contract_lne'] = 1
                    uiMask['objectName'] = 1
                    self.changeVisibleUI(client, None, None, info, uiMask)
            else:
                self.clearUI()
        else:
            self.clearUI()

        if self.keyEdit:
            self.UIKEY1(self.keyEdit)

        self.fillPathes(client, contract, subcontract, selPath, info)


    def changeVisibleUI(self, ActiveClient=None, ActiveContract=None, ActiveSubcontract=None, info=None, uiMask=None):
        print('(changeVisibleUI', ActiveClient, ActiveContract)
        self.client_cbb.blockSignals(1)
        self.contract_cbb.blockSignals(1)
        print(uiMask)
        print('info', info)

        if ActiveClient:
            if not self.client_cbb.currentText()== ActiveClient:
                print(' ****set cbb client:', ActiveClient)
                self.client_cbb.setCurrentText(ActiveClient)
        if ActiveContract:
            if not self.contract_cbb.currentText()== ActiveContract:
                print(' ****set cbb contract:', ActiveContract)
                self.contract_cbb.setCurrentText(ActiveContract)

        if ActiveSubcontract:
            if self.inDictionary('name', info):
                if not info['name'] == '':
                    self.name_lbl.setText(info['name'])
            self.subContract_lne.setText(ActiveSubcontract)

        if self.inDictionary('objectName', info):
            if not info['objectName'] == '':
                self.objectName_lbl.setText(info['objectName'])
            else:
                self.objectName_lbl.setText(defObjectName_lbl)
                self.objectName_lbl.setEnabled(1)
        else:
            self.objectName_lbl.setText(defObjectName_lbl)
            self.objectName_lbl.setEnabled(1)

        self.client_lne.setEnabled(uiMask['client_lne'])
        self.client_lne.setVisible(uiMask['client_lne'])

        self.contract_lne.setEnabled(uiMask['contract_lne'])
        self.contract_lne.setVisible(uiMask['contract_lne'])

        if not info['date']=='':
            self.date_dte.setDate(QDate(int((info['date']).split('.')[2]),
                                        int((info['date']).split('.')[1]),
                                        int((info['date']).split('.')[0])))
        else:
            self.date_dte.setDate(QDate.currentDate())

        # self.fillPathes(self.client_cbb.currentText(), self.contract_cbb.currentText(), self.subContract_lne )

        self.client_cbb.blockSignals(0)
        self.contract_cbb.blockSignals(0)
        print('client:::', self.client_cbb.currentText(), self.client_lne.isVisible(), self.client_lne.isEnabled())
        print('contract:::', self.contract_cbb.currentText(), self.contract_lne.isVisible(), self.contract_lne.isEnabled())
        print('object:::', self.objectName_lbl.isVisible(), self.objectName_lbl.isEnabled())
        print('     changeVisibleUI)')

    def UIKEY1(self, key):
        print('***UI KEY EDIT***', 'key=', key)
        self.client_cbb.blockSignals(1)
        self.contract_cbb.blockSignals(1)

        if key:
            if key==1:
                self.contract_cbb.setEnabled(0)
                self.contract_cbb.setVisible(0)
                self.PdfCheckBox_chb.setVisible(0)

                self.contract_lne.clear()
                self.contract_lne.setEnabled(0)
                self.contract_lne.setVisible(0)

                self.subContract_lne.clear()
                self.subContract_lne.setEnabled(0)
                self.subContract_lne.setVisible(0)

                self.date_dte.clear()
                self.date_dte.setEnabled(0)
                self.date_dte.setVisible(0)

                self.objectName_lbl.clear()
                self.objectName_lbl.setEnabled(0)
                self.objectName_lbl.setVisible(0)

                self.name_lbl.clear()
                self.name_lbl.setEnabled(0)
                self.name_lbl.setVisible(0)

                self.label.setVisible(0)
                self.label_4.setVisible(0)
                self.label_5.setVisible(0)
                self.label_6.setVisible(0)

            if key == 2:
                # self.contract_cbb.setEnabled(0)
                # self.contract_cbb.setVisible(0)

                # self.contract_lne.clear()
                # self.contract_lne.setEnabled(0)
                # self.contract_lne.setVisible(0)

                self.subContract_lne.clear()
                self.subContract_lne.setEnabled(0)
                self.subContract_lne.setVisible(0)
                self.PdfCheckBox_chb.setVisible(0)

                # self.date_dte.clear()
                # self.date_dte.setEnabled(0)
                # self.date_dte.setVisible(0)

                # self.objectName_lbl.clear()
                self.objectName_lbl.setEnabled(1)
                self.objectName_lbl.selectAll()
                self.objectName_lbl.setFocus()
                # self.objectName_lbl.setVisible(0)

                self.name_lbl.clear()
                self.name_lbl.setEnabled(0)
                self.name_lbl.setVisible(0)

                self.label.setVisible(0)
                # self.label_4.setVisible(0)
                self.label_5.setVisible(0)
                # self.label_6.setVisible(0)

        self.client_cbb.blockSignals(0)
        self.contract_cbb.blockSignals(0)


        # uiMask['objectName'] = 1
        # if self.inDictionary('subcontract', info):
        #     if not info['subcontract']=='':
        #         self.subContract_lne.setText(info['subcontract'])
        # if self.inDictionary('name', info):
        #     if not info['name'] == '':
        #         self.name_lbl.setText(info['name'])


    def clearUI(self):
        print('***CLEAR UI***')
        if self.keyEdit:
            pass
        # else:
        self.label_8.setVisible(1)
        self.label_9.setVisible(1)
        self.label_10.setVisible(1)
        self.label_11.setVisible(1)
        self.pdfPathServer_lbl.setVisible(1)
        self.tprPathServer_lbl.setVisible(1)
        self.tzPathServer_lbl.setVisible(1)
        self.obrPathServer_lbl.setVisible(1)
        self.PdfCheckBox_chb.setVisible(0)
        self.TprCheckBox_chb.setVisible(0)
        self.TzCheckBox_chb.setVisible(0)
        self.ObrCheckBox_chb.setVisible(0)

        self.contract_lne.setText('AC.0000')
        self.subContract_lne.setText('00')

        self.date_dte.setDate(QDate.currentDate())

        self.name_lbl.setText(defContract_lne)
        self.name_lbl.setFocus()

        self.objectName_lbl.setText(defObjectName_lbl)

        self.pathServer_lbl.setText(defPath_lbl)
        self.tprPathServer_lbl.setText(defPath_lbl)
        self.tzPathServer_lbl.setText(defPath_lbl)
        self.pdfPathServer_lbl.setText(defPath_lbl)
        self.obrPathServer_lbl.setText(defPath_lbl)



        self.contract_cbb.clear()
        self.contract_cbb.addItem(newContract)

        self.client_lne.setVisible(1)
        self.client_lne.setEnabled(1)
        self.client_lne.setText(defClient_lne)

        self.contract_lne.setVisible(1)
        self.contract_lne.setEnabled(1)

        # self.TprCheckBox_chb.setChecked(0)
        # self.TzCheckBox_chb.setChecked(0)
        # self.PdfCheckBox_chb.setChecked(0)
        #
        # self.TprCheckBox_chb.setVisible(0)
        # self.TzCheckBox_chb.setVisible(0)
        # self.PdfCheckBox_chb.setVisible(0)

    def inDictionary(self, key, dict):
        if key in dict:
            return dict[key]
        else:
            return ''













    def doCreate(self):
        if self.name_lbl.text():
            self.accept()
    #
    #
    #
    #
    def doEdit(self):
        self.accept()
    #
    #
    #
    #
    # def fillDialog(self, fuck=None, itemName=None, path=None):
    #
    #     # print('fuck', fuck)
    #
    #     if not path:
    #         data = settings.settingsClass().load()
    #         path = data.get('path')
    #
    #     if not itemName:
    #         itemName= self.client_cbb.currentText()
    #         if not itemName:
    #             itemName = 'New Client'
    #
    #     # contarctName= None
    #
    #     # contarctName= self.contract_cbb.currentText()
    #     # if contarctName== 'New Contract':
    #     contarctName = ''
    #
    #     if not itemName == 'New Client':
    #         contarctName= self.refreshContracts(itemName, path)

            # self.fillContracts(itemName, path)
            # self.contract_cbb.setCurrentIndex(1)
            # contarctName = self.contract_cbb.currentText()
            # if contarctName == 'New Contract':
            #     contarctName = ''
            # print('A', path)
            # print('B', itemName)
            # print('C', contarctName)
            # fullPath= os.path.join(path, itemName)
            # print('fullPath', fullPath)
        #
        #
        #
        #     info = createProject.getProjectInfo(fullPath)
        #
        #     self.client_lne.setText(info['client'])
        #     self.client_cbb.setCurrentText(itemName)
        #     self.contract_lne.setText(info['contract'])
        #     # try: self.date_dte.setDate(QDate(int((info['date']).split('.')[2]), int((info['date']).split('.')[1]),
        #     #                                     int((info['date']).split('.')[0])))
        # else:
        #     self.client_cbb.setCurrentText('New Client')
        #     self.contract_cbb.setCurrentText('New Contract')
        #     self.contract_lne.clear()
        #     self.contract_lne.setText('AC.0000')


    # def fillContractsOld(self, client=0, path=0):
    #     self.contract_cbb.clear()
    #     self.contract_cbb.addItem('New Contract')
    #     if not path:
    #         data = settings.settingsClass().load()
    #         path = data.get('path')
    #     print('fill', client, path)
    #     if client:
    #         if os.path.exists(path):
    #             for f in os.listdir(path):
    #                 fullPath = os.path.join(path, f)
    #                 if projectTreeWidget.projectTreeClass().isProject(fullPath):
    #                     info = createProject.getProjectInfo(fullPath)
    #                     # print(fullPath)
    #                     if info['client']==client:
    #                         # for i in os.listdir(fullPath):
    #                             if info['contract']!='' and info['subcontract']== '':
    #                                 self.contract_cbb.addItem(info['contract'])
    #                             else:
    #                                 self.fillContracts(client, fullPath)
        # self.refreshContracts()

    # def refreshContracts(self, into=None, path=None):
    #
    #     # self.contract_cbb.setCurrentIndex(0)
    #     contarctName = self.contract_cbb.currentText()
    #     if contarctName:
    #         if contarctName == 'New Contract':
    #             contarctName = ''
    #     else:
    #         contarctName = into
    #     # print('refresh', contarctName, path)
    #     self.fillContracts(contarctName, path)
    #     return contarctName


    def getDialogData(self):
        # if self.keyEdit:
        #     pass
        #
        # else:

        if self.client_lne.isEnabled():
            if not self.client_lne.text() == defClient_lne:
                clientName= self.client_lne.text()
            else:
                clientName = unknown
        else:
            if self.client_cbb.currentText() == newClient:
                clientName = unknown
            else:
                clientName= self.client_cbb.currentText()


        if self.contract_lne.isEnabled():
            contractName= self.contract_lne.text()
        else:
            if self.contract_cbb.currentText()== newContract:
                contractName = unknown
            else:
                contractName= self.contract_cbb.currentText()



        if self.objectName_lbl.isVisible():

            if not self.objectName_lbl.text()== defObjectName_lbl:
                objectName= self.objectName_lbl.text()
            else:
                objectName = ''
        else:
            if not self.objectName_lbl.text() == defObjectName_lbl:
                objectName = self.objectName_lbl.text()
            else:
                objectName = ''


        if not self.name_lbl.text() == defContract_lne:
            name= self.name_lbl.text()
        else: name= unknown

        if not self.pathServer_lbl.text() == defPath_lbl:
            url= self.pathServer_lbl.text()
        else:
            url= ''

        if not self.pdfPathServer_lbl.text() == defPath_lbl:
            pdfurl= self.pdfPathServer_lbl.text()
        else:
            pdfurl= ''

        if not self.tprPathServer_lbl.text() == defPath_lbl:
            tprurl= self.tprPathServer_lbl.text()
        else:
            tprurl= ''

        if not self.tzPathServer_lbl.text() == defPath_lbl:
            tzurl= self.tzPathServer_lbl.text()
        else:
            tzurl= ''

        if not self.obrPathServer_lbl.text() == defPath_lbl:
            obrurl= self.obrPathServer_lbl.text()
        else:
            obrurl= ''

        if self.TprCheckBox_chb.isChecked():
            keytprurl= True
            tprurl = ''
        else:
            keytprurl = False

        if self.TzCheckBox_chb.isChecked():
            keytzurl= True
            tzurl = ''
        else:
            keytzurl = False

        if self.ObrCheckBox_chb.isChecked():
            keyobrurl= True
            obrurl = ''
        else:
            keyobrurl = False

        if self.PdfCheckBox_chb.isChecked():
            keypdfurl= True
            pdfurl = ''
        else:
            keypdfurl = False

        if self.Archive_chb.isChecked():
            archive= True
        else:
            archive= False


        print('Checked: ', self.PdfCheckBox_chb.isChecked(), self.TprCheckBox_chb.isChecked(), self.TzCheckBox_chb.isChecked(), self.ObrCheckBox_chb.isChecked())
        # path=os.path.join(clientName, contractName + '_' + objectName)
        # print(self.client_lne.isVisible())
        # if self.keyEdit:
        if self.keyEdit==1:
            return dict(
                key=1,
                name='',
                client=clientName,
                contract='',
                objectName='',
                subcontract='',
                date='',
                comment=self.comment_txe.toPlainText(),
                # path =          path,
                URLpath=url,
                PDF_URLpath='',
                keypdfurl = '',
                TPR_URLpath='',
                keytprurl='',
                TZ_URLpath='',
                keytzurl='',
                OBR_URLpath = '',
                keyobrurl = '',
                checkArchive = self.checkArchive,
                archive = archive

            )
        if self.keyEdit==2:
            return dict(
                key=2,
                name='',
                client=clientName,
                contract=contractName,
                objectName=objectName,
                subcontract='',
                date=self.date_dte.text(),
                comment=self.comment_txe.toPlainText(),
                # path =          path,
                URLpath=url,
                PDF_URLpath=pdfurl,
                keypdfurl='',
                TPR_URLpath=tprurl,
                keytprurl='',
                TZ_URLpath=tzurl,
                keytzurl='',
                OBR_URLpath=obrurl,
                keyobrurl='',
                checkArchive=self.checkArchive,
                archive=archive

                )


        else:
            return dict(
                key =           None,
                name =          name,
                client =        clientName,
                contract =      contractName,
                objectName =    objectName,
                subcontract =   self.subContract_lne.text(),
                date =          self.date_dte.text(),
                comment =       self.comment_txe.toPlainText(),
                # path =          path,
                URLpath =       url,
                PDF_URLpath=pdfurl,
                keypdfurl=keypdfurl,
                TPR_URLpath=tprurl,
                keytprurl=keytprurl,
                TZ_URLpath=tzurl,
                keytzurl=keytzurl,
                OBR_URLpath=obrurl,
                keyobrurl=keyobrurl,
                checkArchive=self.checkArchive,
                archive=archive


            )

