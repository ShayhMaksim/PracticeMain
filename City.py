from Halt import Halt
from Bus import Bus
from typing import List
from PyQt5.QtWidgets import QGraphicsScale, QGraphicsScene, QGraphicsView

import numpy as np
import random
#класс карты



class City:
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
    observation=30*30#кол-во исходов
    busses:List[Bus]=[]
    Halts={}
    
    def __init__(self) -> None:
        self.chart=np.asarray(
            [
                [2,0,0,0,7],#A - G
                [7,0,0,0,0,0,0,0,6],#G - E
                [6,0,0,0,0,0,0,0,5],#E - D
                [5,0,0,0,0,0,0,4],#D - C
                [4,0,0,0,0,0,3],#C - B
                [3,0,0,0,2],#B - A
                [3,0,0,0,0,8],#B - O
                [4,0,0,0,8],#C - O
                [8,0,0,0,7],#O - G
                [8,0,0,0,6], #O - E
            ]
        )
        

        self.Halts["A"]=(Halt([[0,0],[5,4]],2,"A"))
        self.Halts["B"]=(Halt([[5,0],[6,0],[4,6]],3,"B"))
        self.Halts["C"]=(Halt([[4,0],[7,0],[3,7]],4,"C"))
        self.Halts["D"]=(Halt([[3,0],[2,8]],5,"D"))
        self.Halts["E"]=(Halt([[2,0],[1,8],[9,4]],6,"E"))
        self.Halts["G"]=(Halt([[1,0],[0,4],[8,4]],7,"G"))
        self.Halts["O"]=(Halt([[9,0],[8,0],[7,4],[6,5]],8,"O"))
    
        #self.player=Bus(x0,y0,self.chart)   
        #self.chart[x0][y0]=self.player.symbol

        


    @classmethod 
    def reset(self):
        return City()#Map(5,5,45,45)

 
    def AddBus(self,busses:List[Bus]):
        self.busses=busses
        for bus in self.busses:
            self.chart[bus.x][bus.y]=bus.simbol
    
    def posPlayer(self):
        encoded=[]
        for bus in self.busses:
            encoded.append(bus.encode(bus.x,bus.y))
        return encoded

    def step(self,command):
        
        for key, _ in self.Halts.items():
            self.Halts[key].generate()
        res=[]
        i=0
        for bus in self.busses:
            res.append(bus.step(command[i]))
            i=i+1
        return res


