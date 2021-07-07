
import threading
import time

from PyQt5 import QtCore
from Animator import Animator
from PyQt5.QtCore import QRectF, QThread, QTimer
from PyQt5.QtGui import QBrush, QColor
import numpy as np
import pandas as pd
from PyQt5.QtWidgets import QWidget,QApplication,QGraphicsView,QGraphicsScene
import sys
from City import City
from Bus import Bus
from time import sleep
from threading import Thread
app = QApplication(sys.argv)




city=City()
#animator=Animator(city)
bus = Bus(5,4,city.chart,city.Halts)
city.AddBus([bus])



animator=Animator(city)
#animator.Update()

def Update(app:QApplication,animator:Animator,city:City):
    time.sleep(10)
    city.busses[0].step(2)
    
    #animator.Update()
    

class AThread(QThread):

    def run(self,animator,city,step):
        
        self.sleep(1)
        city.busses[0].step(step)    
        animator.Update()
        QApplication.processEvents()

    


# t = Thread(target=Update,args=(app,animator,city))
# t.start()

QApplication.processEvents()
t = AThread()

# t.run(animator=animator,city=city,step=3)

# t.run(animator=animator,city=city,step=0)

# t.run(animator=animator,city=city,step=1)

# t.run(animator=animator,city=city,step=2)

# t.run(animator=animator,city=city,step=1)
# t.run(animator=animator,city=city,step=1)
# t.run(animator=animator,city=city,step=1)
# t.run(animator=animator,city=city,step=1)


sys.exit(app.exec_())
