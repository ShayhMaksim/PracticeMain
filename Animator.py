from PyQt5.QtGui import QBrush, QColor
from PyQt5.QtWidgets import QApplication, QGraphicsScene, QGraphicsTextItem,QGraphicsView, QWidget
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
        """
        0 - свободная клетка
        1 - игрок
        2 - A
        3 - B
        4 - C
        5 - D
        6 - E
        7 - G
        8 - O
        9 - занято
        """
        i=0
        j=0
        c=50
        self.scene.clear()
        while i<10:
            k=len(self.city.chart[i])
            text=None
            while j<k:
                
                if self.city.chart[i][j]==0:
                    self.scene.addRect(QRectF(i*c,j*c,c,c),QColor(0,255,255))
                if self.city.chart[i][j]==1:
                    self.scene.addRect(QRectF(i*c,j*c,c,c),QColor(0,255,0),QBrush(QColor(0,255,0)))
                if self.city.chart[i][j]==2:
                    self.scene.addRect(QRectF(i*c,j*c,c,c),QColor(0,0,255),QBrush(QColor(0,0,255)))
                    text=QGraphicsTextItem("A")
                    text.setScale(2)
                    text.setPos(i*c,j*c)
                    self.scene.addItem(text)
                if self.city.chart[i][j]==3:
                    self.scene.addRect(QRectF(i*c,j*c,c,c),QColor(255,0,0),QBrush(QColor(255,0,0)))
                    text=QGraphicsTextItem("B")
                    text.setScale(2)
                    text.setPos(i*c,j*c)    
                    self.scene.addItem(text) 
                if self.city.chart[i][j]==4:
                    self.scene.addRect(QRectF(i*c,j*c,c,c),QColor(255,155,150),QBrush(QColor(255,155,150)))
                    text=QGraphicsTextItem("C")
                    text.setScale(2)
                    text.setPos(i*c,j*c)  
                    self.scene.addItem(text)
                if self.city.chart[i][j]==5:
                    self.scene.addRect(QRectF(i*c,j*c,c,c),QColor(0,155,150),QBrush(QColor(0,155,150)))
                    text=QGraphicsTextItem("D")
                    text.setScale(2)
                    text.setPos(i*c,j*c) 
                    self.scene.addItem(text)
                if self.city.chart[i][j]==6:
                    self.scene.addRect(QRectF(i*c,j*c,c,c),QColor(255,0,150),QBrush(QColor(255,0,150)))
                    text=QGraphicsTextItem("E")
                    text.setScale(2)
                    text.setPos(i*c,j*c) 
                    self.scene.addItem(text)
                if self.city.chart[i][j]==7:
                    self.scene.addRect(QRectF(i*c,j*c,c,c),QColor(255,100,150),QBrush(QColor(255,100,150)))
                    text=QGraphicsTextItem("G")
                    text.setScale(2)
                    text.setPos(i*c,j*c)
                    self.scene.addItem(text)
                if self.city.chart[i][j]==8:
                    self.scene.addRect(QRectF(i*c,j*c,c,c),QColor(255,100,0),QBrush(QColor(255,100,0)))
                    text=QGraphicsTextItem("O")
                    text.setScale(2)
                    text.setPos(i*c,j*c)
                    self.scene.addItem(text)
                if self.city.chart[i][j]==9:
                    self.scene.addRect(QRectF(i*c,j*c,c,c),QColor(0,50,0),QBrush(QColor(0,50,0)))
                if self.city.chart[i][j]==10:
                    self.scene.addRect(QRectF(i*c,j*c,c,c),QColor(0,0,0),QBrush(QColor(100,100,100)))
                j=j+1
            i=i+1
            j=0

        self.graphicsView.repaint()
