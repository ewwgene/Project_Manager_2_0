from PySide2.QtCore import *
from PySide2.QtWidgets import *
import QUICK_ui as ui

import math

# class sineCustomWidget(QWidget):
#     def __init__(self):
#         super(sineCustomWidget, self).__init__()
#         self.resize(400, 200)
#         self.setWindowTitle('Sine')
#
#         self.wave_height= 30
#         self.wave_len = 20
#         self.penWidth = 3
#         self.grid = 30
#
#     def paintEvent(self, event):
#         rec = event.rect()
#         if False:
#             rec=QRect()
#         painter = QPainter()
#         painter.begin(self)
#
#         # paint
#         painter.fillRect(rec, Qt.black)
#         painter.setPen(QPen(QBrush(Qt.gray), 0.5))
#         painter.setFont(QFont('Arial', 8))
#         for i in range(0, rec.width(), self.grid):
#             painter.drawLine(i, 0, i, rec.height())
#             if self.grid>20:
#                 painter.drawText(i+3, 12, str(i))
#
#         for i in range(0, rec.height(), self.grid):
#             painter.drawLine(0, i, rec.width(), i)
#
#         painter.setRenderHint(QPainter.Antialiasing)
#
#
#
#         painter.setPen(QPen(QBrush(Qt.white), self.penWidth))
#         prevx= 0
#         prevy = (0*self.wave_height)+(rec.height()/2)
#         for x in range(1, rec.width()):
#             s= sin((x*0.1)*self.wave_len*0.1)
#             y=(s*self.wave_height)+(rec.height()/2)
#             # painter.drawPoint(x, y)
#             # painter.drawLine(prevx, prevy, x, y)
#             painter.drawLine(QPointF(prevx, prevy), QPointF(x, y))
#             prevx=x
#             prevy=y
#             # print(x,y)
#
#         # end
#         painter.end()


class QuickClass(QWidget, ui.Ui_Form):
    def __init__(self):
        super(QuickClass, self).__init__()
        self.setupUi(self)

        self.Quick_btn.clicked.connect(self.computeAll)
        self.Clear_btn.clicked.connect(self.clearB)
        self.H_in1.editingFinished.connect(self.computeAll)
        self.H_in2.editingFinished.connect(self.computeAll)
        self.V_in1.editingFinished.connect(self.computeAll)
        self.V_in2.editingFinished.connect(self.computeAll)
        self.H_in1.clear()


    def computeAll(self):
        self.computeH()
        self.computeV()

    def computeH(self):
        h1= self.H_in1.value()
        h2= self.H_in2.value()
        if h1 or h2:
            if h1==0 and h2==0:
                self.H_Size_Out.setText('Size: ?')
                self.H_Center_Out.setText('Center: ?')
            else:
                if h1 > h2:
                    hS= h1 - h2
                    hC= (hS / 2) + h2
                else:
                    hS = h2 - h1
                    hC = (hS / 2) + h1

                self.H_Size_Out.setText('Size: %.2f' % hS)
                self.H_Center_Out.setText('Center: %.2f' % hC)


    def computeV(self):
        v1 = self.V_in1.value()
        v2 = self.V_in2.value()
        if v1 or v2:
            if v1==0 and v2==0:
                self.V_Size_Out.setText('Size: ?')
                self.V_Center_Out.setText('Center: ?')
            else:
                if v1 > v2:
                    vS = v1 - v2
                    vC = (vS / 2) + v2
                else:
                    vS = v2 - v1
                    vC = (vS / 2) + v1

                self.V_Size_Out.setText('Size: %.2f' % vS)
                self.V_Center_Out.setText('Center: %.2f' % vC)

    def clearB(self):
        self.H_in1.setValue(0)
        self.H_in2.setValue(0)
        self.V_in1.setValue(0)
        self.V_in2.setValue(0)
        self.V_Size_Out.setText('Size')
        self.V_Center_Out.setText('Center')
        self.H_Size_Out.setText('Size')
        self.H_Center_Out.setText('Center')




if __name__ == '__main__':
    app= QApplication([])
    w= QuickClass()
    w.show()
    app.exec_()