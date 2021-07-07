
from PyQt5.QtCore import QRectF
from PyQt5.QtGui import QBrush, QColor
import numpy as np
import pandas as pd
from PyQt5.QtWidgets import QWidget,QApplication,QGraphicsView,QGraphicsScene
import sys
from City import City


app = QApplication(sys.argv)
scene = QGraphicsScene()
graphicsView = QGraphicsView(scene)
graphicsView.show()
graphicsView.resize(1000,1000)


city=City()

i=0
j=0
c=50

while i<10:
    k=len(city.chart[i])
    while j<k:
        if city.chart[i][j]==0:
            scene.addRect(QRectF(i*c,j*c,c,c),QColor(0,255,255))
        if city.chart[i][j]==1:
            scene.addRect(QRectF(i*c,j*c,c,c),QColor(0,255,0),QBrush(QColor(0,255,0)))
        if city.chart[i][j]==2:
            scene.addRect(QRectF(i*c,j*c,c,c),QColor(0,0,255),QBrush(QColor(0,0,255)))
        if city.chart[i][j]==3:
            scene.addRect(QRectF(i*c,j*c,c,c),QColor(255,0,0),QBrush(QColor(255,0,0)))        
        if city.chart[i][j]==4:
            scene.addRect(QRectF(i*c,j*c,c,c),QColor(255,155,150),QBrush(QColor(255,155,150)))
        if city.chart[i][j]==5:
            scene.addRect(QRectF(i*c,j*c,c,c),QColor(0,155,150),QBrush(QColor(0,155,150)))
        if city.chart[i][j]==6:
            scene.addRect(QRectF(i*c,j*c,c,c),QColor(255,0,150),QBrush(QColor(255,0,150)))
        if city.chart[i][j]==7:
            scene.addRect(QRectF(i*c,j*c,c,c),QColor(255,100,150),QBrush(QColor(255,100,150)))
        if city.chart[i][j]==8:
            scene.addRect(QRectF(i*c,j*c,c,c),QColor(255,100,0),QBrush(QColor(255,100,0)))
        j=j+1
    i=i+1
    j=0

sys.exit(app.exec())