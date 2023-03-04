import os, shutil, json, templateEditor, settings, projectTreeWidget

dataSet = settings.settingsClass().load()
basePath = dataSet.get('path')
projectFile= '.project'
template= json.load(open(templateEditor.templateFile))



def mkFolder(path):
    try:
        # os.mkdir(path)
        os.makedirs(path)
        return True
    except:
        return False

def createProject(data, oldtPath=None, KeyEdit=None):
    print(data)

    if data['objectName'] == '':
        objectName = ''
    else:
        objectName = '_' + data['objectName']

    if data['name'] == '':
        nameName = ''
    else:
        nameName = '_' + data['name']

    clientName= data['client']
    contractName= data['contract'] + objectName
    projectName= data['subcontract'] + nameName
    clientPath= os.path.join(basePath, clientName)
    contractPath= os.path.join(clientPath, contractName)
    projectPath= os.path.join(contractPath, projectName)
    proverkaName= data['contract'] + '_' + data['subcontract'] + ' ' + data['client']


    if not os.path.exists(clientPath):
        mkFolder(clientPath)
        clientData= data.copy()
        clientData['key'] = '1'
        clientData['name']= ''
        clientData['objectName'] = ''
        clientData['contract'] = ''
        clientData['subcontract'] = ''
        clientData['date'] = ''
        clientData['URLpath'] = ''
        clientData['PDF_URLpath'] = ''
        clientData['TPR_URLpath'] = ''
        clientData['TZ_URLpath'] = ''
        clientData['keypdfurl'] = ''
        clientData['keytprurl'] = ''
        clientData['keytzurl'] = ''
        # clientData['path'] = ''
        makeProjectFile(clientPath, clientData)

    if not os.path.exists(contractPath):
        mkFolder(contractPath)
        contractData= data.copy()
        contractData['key'] = '2'
        contractData['name']= ''
        contractData['subcontract'] = ''
        contractData['date'] = ''
        contractData['keypdfurl'] = ''
        contractData['keytprurl'] = ''
        contractData['keytzurl'] = ''
        # contractData['path'] = contractPath
        makeProjectFile(contractPath, contractData)

    # if not os.path.exists(projectPath):
    #     data['path'] = projectPath

    # if not checkLegalCharacters(projectName):
    #     projectName = checkLegalCharacters(data['subcontract'] + '_' + data['name'])

    # pPath= os.path.join(pathProject, projectName)
    if mkFolder(projectPath):
        buildFolders(projectPath, template, proverkaName)
    makeProjectFile(projectPath, data)
    # print(clientData['name'])
    return(projectName)


def editProject(oldpath, newpath, data, keyEdit):
    print('(*editProject')
    projectName = os.path.basename(newpath)
    # makeProjectFile(oldpath, data)
    if not oldpath==newpath:
        restore(oldpath, newpath, data, keyEdit)
        if not os.path.exists(newpath):
            os.renames(oldpath, newpath)
            print('renames:', oldpath, newpath)
        else:
            shutil.copytree(oldpath, newpath, copy_function=shutil.move, dirs_exist_ok=True)
            os.rename(oldpath, os.path.join(basePath, '__temp'))
            # os.rename(oldpath, 'temp')
            print('move:', oldpath, newpath)
    else:
        restore(oldpath, newpath, data, keyEdit)

    print('     *editProject)')
    return (projectName)


def restore(oldpath, newpath, data, keyEdit):
    if keyEdit == 1:
        makeProjectFile(oldpath, data)
        for contract in os.listdir(oldpath):
            if projectTreeWidget.projectTreeClass().isProject(os.path.join(oldpath, contract)):
                keys = ['client']
                if data['checkArchive']:
                    keys.append('archive')
                remakeInfoContract = remakeChildData(os.path.join(oldpath, contract), data, keys)
                makeProjectFile(os.path.join(oldpath, contract), remakeInfoContract)
                for project in os.listdir(os.path.join(oldpath, contract)):
                    if projectTreeWidget.projectTreeClass().isProject(os.path.join(oldpath, contract, project)):
                        # keys = ['client', 'contract', 'objectName', 'date', 'PDF_URLpath']
                        keys = ['client']
                        if data['checkArchive']:
                            keys.append('archive')
                        remakeInfo = remakeChildData(os.path.join(oldpath, contract, project), data, keys)
                        makeProjectFile(os.path.join(oldpath, contract, project), remakeInfo)
    if keyEdit == 2:
        makeProjectFile(oldpath, data)
        for project in os.listdir(oldpath):
            if projectTreeWidget.projectTreeClass().isProject(os.path.join(oldpath, project)):
                keys = ['client', 'contract', 'objectName', 'date']
                if data['checkArchive']:
                    keys.append('archive')
                remakeInfo = remakeChildData(os.path.join(oldpath, project), data, keys)
                makeProjectFile(os.path.join(oldpath, project), remakeInfo)
    if keyEdit == 3:
        makeProjectFile(oldpath, data)



            # if not os.path.exists(newpath):
            #     os.renames(oldpath, newpath)


def remakeChildData(path, newInfo, keys):
    oldInfo= getProjectInfo(path)
    for key in keys:
        if inDictionary(key, newInfo):
            if not newInfo[key]=='':
                if inDictionary(key, oldInfo):
                    if not newInfo[key]==oldInfo[key]:
                        oldInfo[key]=newInfo[key]
                        print('-remake done', oldInfo[key])
                else:
                    oldInfo[key]=newInfo[key]
                    print('+remake done', oldInfo[key])
    return oldInfo




def inDictionary(key, dict):
    return key in dict



def buildFolders(root, folders, proverkaName=None):
    for f in folders:
        if f['name'] == '*name*':
            fname= proverkaName
        else:
            fname= f['name']
        full= os.path.join(root, fname)
        mkFolder(full)
        buildFolders(full, f['children'])

def makeProjectFile(path, data):
    filePath= os.path.join(path, projectFile)
    with open(filePath, 'w') as f:
        json.dump(data, f, indent=4)

def checkLegalCharacters(name):
    return name

def getProjectInfo(path):
    filePath = os.path.join(path, projectFile)
    with open(filePath) as f:
        return json.load(f)

