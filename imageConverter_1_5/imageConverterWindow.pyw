from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from widgets import imageConverter_ui as ui
from widgets import filesWidget
import converter, settings
import os

htmlsame= r'< img src = "C:\Users\eugen\OneDrive\Desktop\Py\2022\icons\icons8-bandage-48.png">'
htmldiff= r'< img src = "C:\Users\eugen\OneDrive\Desktop\Py\2022\icons\icons8-panda-48.png">'


class imageConverterClass (QMainWindow, ui.Ui_imageConverter):
    def __init__(self):
        super(imageConverterClass, self).__init__()
        self.setupUi(self)
        self.list= filesWidget.listWidgetClass()
        self.files_ly.addWidget(self.list)
        self.start_btn.clicked.connect(self.start)
        self.browsSet_btn.clicked.connect(self.showMessage)

        ##########
        self.rezo_cbb.addItem('640')
        self.rezo_cbb.addItem('1024')
        self.rezo_cbb.addItem('2600')
        self.rezo_cbb.addItem('2800')
        self.rezo_cbb.addItem('3200')
        self.ext_cbb.addItem('jpeg')
        self.ext_cbb.addItem('bmp')
        self.ext_cbb.addItem('png')
        self.ext_cbb.addItem('tiff')
        self.ext_cbb.addItem('ico')
        ##########


        self.fillSettings()
        self.rezo_cbb.currentTextChanged.connect(self.getRezo)
        self.ext_cbb.currentTextChanged.connect(self.getExt)

    def showMessage(self):
        data = settings.settingsClass().load()
        path = data.get('path')
        if not path=='':
            startbrows=os.path.dirname(path)
        else:
            startbrows='c:/windows'
        _filter= 'converter(*.exe);; All(*.*)'
        d= QFileDialog.getOpenFileName(self, 'Set folder', startbrows, _filter)
        if not d[0]=='':
            self.sett_le.setText(d[0])
            data= self.getTableData('path', d[0])
            settings.settingsClass().save(data)

    def fillSettings(self):
        data = settings.settingsClass().load()
        path = data.get('path')
        resolution = data.get('resolution')
        ext = data.get('ext')
        self.sett_le.setText(path)
        if not resolution=='':
            self.rezo_cbb.setCurrentText(resolution)
        else:
            self.rezo_cbb.setCurrentText('640')
        if not ext=='':
            self.ext_cbb.setCurrentText(ext)
        else:
            self.ext_cbb.setCurrentText('jpeg')

    def getRezo(self):
        resolution = self.rezo_cbb.currentText()
        data = self.getTableData('resolution', resolution)
        settings.settingsClass().save(data)

    def getExt(self):
        ext = self.ext_cbb.currentText()
        data = self.getTableData('ext', ext)
        settings.settingsClass().save(data)

    def getTableData(self, key, value):
        data = settings.settingsClass().load()
        data[key]= value
        return data

    def start(self):
        files= self.list.getAllFiles()
        if files:
            for f in files:
                name, xt= os.path.splitext(os.path.basename(f))
                outsrc= converter.convert(f)
                item= self.list.findItems(name, Qt.MatchContains)
                item[0].setText(item[0].text()+' :-)')

                    # else:
                    #     print('DIFFERENT')
                    #     item = self.list.findItems(os.path.basename(f), Qt.MatchContains)
                    #     item[0].setText(item[0].text() + ' :)')



if __name__ == '__main__':
    app= QApplication([])
    w= imageConverterClass()
    w.show()
    app.exec_()