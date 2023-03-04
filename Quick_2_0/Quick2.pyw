from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
import QUICK_2_ui as ui

import math


class quickCustomWidget(QWidget):
    def __init__(self):
        super(quickCustomWidget, self).__init__()
        self.resize(400, 200)
        self.setWindowTitle('Sine')

        self.H_num_center= 0
        self.V_num_center = 0
        self.clip= 0
        self.checkV=False
        self.checkZ=False
        self.checkH =True
        self.Z_floor= 0
        self.Z_floor_size = 0
        # self.wave_len = 20
        # self.penWidth = 3
        # self.grid = 30

    def paintEvent(self, event):
        rec = event.rect()
        if False:
            rec=QRect()
        painter = QPainter()
        painter.begin(self)

        # paint
        painter.fillRect(rec, Qt.white)
        # painter.setPen(QPen(QBrush(Qt.gray), 0.5))
        # painter.setFont(QFont('Arial', 8))
        # for i in range(0, rec.width(), self.grid):
        #     painter.drawLine(i, 0, i, rec.height())
        #     if self.grid>20:
        #         painter.drawText(i+3, 12, str(i))
        #
        # for i in range(0, rec.height(), self.grid):
        #     painter.drawLine(0, i, rec.width(), i)
        #
        painter.setRenderHint(QPainter.Antialiasing)
        #
        ############ РИСУЕМ СТЕНУ
        padding= 20
        point_1= QPoint(0+1.5*padding, 0+padding)
        point_11= QPoint(point_1.x()-1*padding, point_1.y()-0.1*padding)
        point_2= QPoint(rec.width()-1.5*padding, rec.height()-padding)
        point_22 = QPoint(point_2.x() + 1 * padding, point_2.y() + 0.1 * padding)
        point_3= QPoint(point_1.x(), point_2.y())
        point_33 = QPoint(point_3.x()-1*padding, point_3.y() + 0.1 * padding)
        point_4 = QPoint(point_2.x(), point_1.y())
        point_44 = QPoint(point_4.x() + 1 * padding, point_4.y() - 0.1 * padding)

        painter.setPen(QPen(QBrush(Qt.black), 3))
        painter.drawRect(QRect(point_1, point_2))
        painter.drawLine(point_1, point_11)
        painter.drawLine(point_2, point_22)
        painter.drawLine(point_3, point_33)
        painter.drawLine(point_4, point_44)

        ############ РИСУЕМ РОЗЕТКУ
        axid = 0.1
        poi_0 = QPoint((rec.width()/2)+(rec.width()*axid), (rec.height()/2)-(rec.height()*axid))
        mult = 0.5
        poi_1 = QPoint(poi_0.x()- 2 * padding * mult, poi_0.y()-padding * mult)
        poi_2 = QPoint(poi_0.x() + 2 * padding * mult, poi_0.y() - padding * mult)
        poi_3 = QPoint(poi_0.x()- 2 * padding * mult, poi_0.y()+padding * mult)
        poi_4 = QPoint(poi_0.x() + 2 * padding * mult, poi_0.y() + padding * mult)
        poi_5 = QPoint(poi_0.x(), poi_0.y()-padding * mult)
        poi_6 = QPoint(poi_0.x(), poi_0.y()+padding * mult)
        poi_01 = QPoint(poi_0.x() - padding * mult, poi_0.y())
        poi_02 = QPoint(poi_0.x() + padding * mult, poi_0.y())
        painter.drawLine(poi_1, poi_2)
        painter.drawLine(poi_2, poi_4)
        painter.drawLine(poi_4, poi_3)
        painter.drawLine(poi_1, poi_3)
        painter.drawLine(poi_5, poi_6)
        painter.drawEllipse(poi_01, (padding/2)*mult, (padding/2)*mult)
        painter.drawEllipse(poi_02, (padding / 2) * mult, (padding / 2) * mult)
        ax_mult = 75 * mult

        if self.Z_floor_size:
            painter.setPen(QPen(QBrush(Qt.black), 1.5))
            zx_1 = QPoint(point_1.x() + ax_mult, point_1.y())
            zx_2 = QPoint(zx_1.x(), zx_1.y()+(ax_mult/2))
            painter.drawLine(zx_1, zx_2)

        ############ РИСУЕМ ОСЬ
        painter.setPen(QPen(QBrush(Qt.red), 1, Qt.DashDotLine))


        if self.checkV:
            ax_1 = QPoint(poi_0.x(), poi_0.y() - ax_mult)
            ax_2 = QPoint(poi_0.x(), poi_0.y() + 1*ax_mult)
            painter.drawLine(ax_1, ax_2)

        if self.checkH:
            ax_3 = QPoint(poi_0.x() - 2*ax_mult, poi_0.y())
            ax_4 = QPoint(poi_0.x() + ax_mult, poi_0.y())
            painter.drawLine(ax_3, ax_4)

        ############ ПИШЕМ ВЫСОТУ
        if self.H_num_center:
            painter.setPen(QPen(QBrush(Qt.red), 1))
            painter.setFont(QFont('Segoe UI', 14, QFont.Bold))
            painter.drawText(ax_3.x()-padding, ax_3.y()+padding, str(self.H_num_center))
            # print(Clip,'<<>>', str(self.H_num_center))
            if self.clip==str(self.H_num_center):
                painter.setPen(QPen(QBrush(Qt.green), 1))
                painter.setFont(QFont('Segoe UI', 14, QFont.Bold))
                painter.drawText(ax_3.x() - padding, ax_3.y() + 2*padding, 'Copy')


        if self.V_num_center:
            painter.setPen(QPen(QBrush(Qt.red), 1))
            painter.setFont(QFont('Segoe UI', 14, QFont.Bold))
            painter.drawText(ax_2.x()-padding, ax_2.y()+padding, str(self.V_num_center))
            # print(Clip, '<<>>', str(self.V_num_center))
            if self.clip==str(self.V_num_center):
                painter.setPen(QPen(QBrush(Qt.green), 1))
                painter.setFont(QFont('Segoe UI', 14, QFont.Bold))
                painter.drawText(ax_2.x()-padding, ax_2.y()+2*padding, 'Copy')

        if self.Z_floor_size:
            painter.setPen(QPen(QBrush(Qt.red), 1))
            painter.setFont(QFont('Segoe UI', 14, QFont.Bold))
            painter.drawText(zx_2.x()-padding, zx_2.y()+padding, str(self.Z_floor_size))
            # print(Clip, '<<>>', str(self.V_num_center))
            if self.clip==str(self.Z_floor_size):
                painter.setPen(QPen(QBrush(Qt.green), 1))
                painter.setFont(QFont('Segoe UI', 14, QFont.Bold))
                painter.drawText(zx_2.x()-padding, zx_2.y()+2*padding, 'Copy')

        if self.Z_floor:
            painter.setPen(QPen(QBrush(Qt.red), 1, Qt.DashDotLine))
            z_1 = QPoint(point_3.x(), point_3.y()-(int(self.Z_floor)/1.5))
            z_2 = QPoint(point_4.x(), point_3.y()-(int(self.Z_floor)/1.5))
            painter.drawLine(z_1, z_2)
            # painter.drawLine()


        # prevx= 0
        # prevy = (0*self.wave_height)+(rec.height()/2)
        # for x in range(1, rec.width()):
        #     s= sin((x*0.1)*self.wave_len*0.1)
        #     y=(s*self.wave_height)+(rec.height()/2)
        #     # painter.drawPoint(x, y)
        #     # painter.drawLine(prevx, prevy, x, y)
        #     painter.drawLine(QPointF(prevx, prevy), QPointF(x, y))
        #     prevx=x
        #     prevy=y
        #     # print(x,y)

        # end
        painter.end()

    def paintH(self, value):
        self.H_num_center= value
        self.update()

    def paintV(self, value):
        self.V_num_center= value
        self.update()

    def paintZ(self, value):
        self.Z_floor= value
        self.update()

    def paintZsize(self, value):
        self.Z_floor_size= value
        self.update()



class QuickClass(QMainWindow, ui.Ui_Form):
    def __init__(self):
        super(QuickClass, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.WindowStaysOnTopHint)

        self.quick = quickCustomWidget()
        self.Paint_lyo.addWidget(self.quick)

        # self.Quick_btn.clicked.connect(self.computeAll)
        self.Clear_btn.clicked.connect(self.clearB)

        self.checkBox_V.setFocusPolicy(Qt.ClickFocus)
        self.checkBox_H.setFocusPolicy(Qt.ClickFocus)
        self.Z_in1.setFocusPolicy(Qt.ClickFocus)
        self.Z_in2.setFocusPolicy(Qt.ClickFocus)
        # self.Quick_btn.setFocusPolicy(Qt.ClickFocus)
        self.Clear_btn.setFocusPolicy(Qt.ClickFocus)
        self.Clear_btn.clicked.connect(self.clearB)



        # self.H_in1.setKeyboardTracking(0)
        # self.H_in1.setMouseTracking(0)
        # self.H_in2.setKeyboardTracking(0)
        # self.H_in2.setMouseTracking(0)
        # self.V_in1.setKeyboardTracking(0)
        # self.V_in1.setMouseTracking(0)
        # self.V_in2.setKeyboardTracking(0)
        # self.V_in2.setMouseTracking(0)
        # self.Z_in1.setKeyboardTracking(0)
        # self.Z_in1.setMouseTracking(0)
        # self.Z_in2.setKeyboardTracking(0)
        # self.Z_in2.setMouseTracking(0)
        # self.H_in1.valueChanged.connect(self.h1)
        self.H_in1.editingFinished.connect(self.h1)
        self.H_in2.editingFinished.connect(self.h2)
        self.V_in1.editingFinished.connect(self.v1)
        self.V_in2.editingFinished.connect(self.v2)
        self.Z_in1.editingFinished.connect(self.z1)
        self.Z_in2.editingFinished.connect(self.z2)
        # self.H_in1.setFocus()
        self.start()
        self.checkBox_V.setChecked(1)
        self.checkBox_V.stateChanged.connect(self.checkV)
        self.checkBox_V.setChecked(0)
        self.checkBox_H.setChecked(1)
        self.checkBox_H.stateChanged.connect(self.checkH)
        self.minus=0

    def keykey(self, event):
        print(event.key)


    def z1(self):
        if not self.Z_in1.text()=='':
            self.quick.paintZ(self.Z_in1.text())
            self.minus=self.Z_in1.value()
            # self.Z_in2.setFocus()
            # self.Z_in2.selectAll()

    def z2(self):
        if not self.Z_in2.text()=='':
            zC = self.Z_in2.value()
            if not self.Z_in1.text()=='':
                zC= zC-self.Z_in1.value()
            self.quick.paintZsize(zC)
            clipboard = QApplication.clipboard()

            self.quick.clip = str(zC)
            clipboard.setText(str(zC))


    def checkV(self, value):
        print('def checkV', value)
        if value:
            self.V_in1.setEnabled(1)
            self.V_in2.setEnabled(1)
            self.quick.checkV = True
        else:
            self.V_in1.setEnabled(0)
            self.V_in2.setEnabled(0)
            self.quick.checkV = False
            self.quick.V_num_center = 0

    def checkH(self, value):
        print('def checkV', value)
        if value:
            self.H_in1.setEnabled(1)
            self.H_in2.setEnabled(1)
            self.quick.checkH = True
        else:
            self.H_in1.setEnabled(0)
            self.H_in2.setEnabled(0)
            self.quick.checkH = False
            self.quick.H_num_center = 0

    def start(self):
        self.H_in1.clear()
        self.H_in1.setFocus()

    def h1(self):
        if not self.H_in1.text()=='':
            self.computeH()
            # self.H_in2.setFocus()
            # self.H_in2.selectAll()

    def h2(self):
        self.computeH()
        # if self.checkBox_V.isChecked():
            # self.V_in1.setFocus()
            # self.V_in1.selectAll()
        # else:
            # self.H_in1.setFocus()
            # self.H_in1.selectAll()

    def v1(self):
        self.computeV()
        # self.V_in2.setFocus()
        # self.V_in2.selectAll()

    def v2(self):
        self.computeV()
        # self.H_in1.setFocus()
        # self.H_in1.selectAll()





    def computeAll(self):
        self.computeH()
        self.computeV()

    def computeH(self):
        h1= self.H_in1.value()
        h2= self.H_in2.value()
        if h1 or h2:
            if h1==0 and h2==0:
                # self.H_Size_Out.setText('Size: ?')
                # self.H_Center_Out.setText('Center: ?')
                print('?')
            else:
                if h1 > h2:
                    hS= h1 - h2
                    hC= (hS / 2) + h2
                else:
                    hS = h2 - h1
                    hC = (hS / 2) + h1

                # self.H_Size_Out.setText('Size: %.2f' % hS)
                # self.H_Center_Out.setText('Center: %.2f' % hC)
                # print('Size: %.2f' % hS)
                # print('Center: %.2f' % hC)
                clipboard = QApplication.clipboard()

                self.quick.clip = str(hC)
                clipboard.setText(str(hC))
                self.quick.paintH(hC)


    def computeV(self):
        v1 = self.V_in1.value()
        v2 = self.V_in2.value()
        if v1 or v2:
            if v1==0 and v2==0:
                # self.V_Size_Out.setText('Size: ?')
                # self.V_Center_Out.setText('Center: ?')
                print('?')
            else:
                if v1 > v2:
                    vS = v1 - v2
                    vC = (vS / 2) + v2 - self.minus
                else:
                    vS = v2 - v1
                    vC = (vS / 2) + v1 - self.minus

                # self.V_Size_Out.setText('Size: %.2f' % vS)
                # self.V_Center_Out.setText('Center: %.2f' % vC)
                # print('Size: %.2f' % vS)
                # print('Center: %.2f' % vC)
                clipboard = QApplication.clipboard()
                self.quick.clip=str(vC)
                clipboard.setText(str(vC))
                # print('clipboard V', vC)
                self.quick.paintV(vC)

    def clearB(self):
        self.H_in1.setValue(0)
        self.H_in2.setValue(0)
        self.V_in1.setValue(0)
        self.V_in2.setValue(0)
        self.Z_in1.setValue(0)
        self.Z_in2.setValue(0)
        self.quick.V_num_center = 0
        self.quick.H_num_center = 0
        self.quick.Z_floor = 0
        self.quick.Z_floor_size = 0
        self.quick.update()
        # self.V_Size_Out.setText('Size')
        # self.V_Center_Out.setText('Center')
        # self.H_Size_Out.setText('Size')
        # self.H_Center_Out.setText('Center')




if __name__ == '__main__':
    app= QApplication([])
    w= QuickClass()
    w.show()
    app.exec_()