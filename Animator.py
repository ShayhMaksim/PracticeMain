from PyQt5.QtGui import QBrush, QColor
from PyQt5.QtWidgets import QApplication, QGraphicsScene,QGraphicsView, QWidget
from PyQt5.QtCore import QObject, QRectF
from City import City
class Animator(QObject):
    def __init__(self,city):
        self.scene = QGraphicsScene()
        self.graphicsView = QGraphicsView(self.scene)
        self.graphicsView.show()
        self.graphicsView.resize(1000,1000)
        self.city=city
        self.Update()
        

    def Update(self):
        i=0
        j=0
        c=50
        self.scene.clear()
        while i<10:
            k=len(self.city.chart[i])
            while j<k:
                if self.city.chart[i][j]==0:
                    self.scene.addRect(QRectF(i*c,j*c,c,c),QColor(0,255,255))
                if self.city.chart[i][j]==1:
                    self.scene.addRect(QRectF(i*c,j*c,c,c),QColor(0,255,0),QBrush(QColor(0,255,0)))
                if self.city.chart[i][j]==2:
                    self.scene.addRect(QRectF(i*c,j*c,c,c),QColor(0,0,255),QBrush(QColor(0,0,255)))
                if self.city.chart[i][j]==3:
                    self.scene.addRect(QRectF(i*c,j*c,c,c),QColor(255,0,0),QBrush(QColor(255,0,0)))        
                if self.city.chart[i][j]==4:
                    self.scene.addRect(QRectF(i*c,j*c,c,c),QColor(255,155,150),QBrush(QColor(255,155,150)))
                if self.city.chart[i][j]==5:
                    self.scene.addRect(QRectF(i*c,j*c,c,c),QColor(0,155,150),QBrush(QColor(0,155,150)))
                if self.city.chart[i][j]==6:
                    self.scene.addRect(QRectF(i*c,j*c,c,c),QColor(255,0,150),QBrush(QColor(255,0,150)))
                if self.city.chart[i][j]==7:
                    self.scene.addRect(QRectF(i*c,j*c,c,c),QColor(255,100,150),QBrush(QColor(255,100,150)))
                if self.city.chart[i][j]==8:
                    self.scene.addRect(QRectF(i*c,j*c,c,c),QColor(255,100,0),QBrush(QColor(255,100,0)))
                if self.city.chart[i][j]==9:
                    self.scene.addRect(QRectF(i*c,j*c,c,c),QColor(0,50,0),QBrush(QColor(0,50,0)))
                j=j+1
            i=i+1
            j=0

        self.graphicsView.repaint()
