

from typing import Reversible
from PyQt5.sip import enableautoconversion
from numpy.core.numeric import True_
from Halt import Halt


class Bus2:
    simbol=1
    action_space=4
    map=None
    halts={}
    def __init__(self,x,y,distance,map,halts) -> None:
        self.x=x
        self.y=y
        self.map=map
        self.score=0
        self.isDone=False
        self.halts=halts
        self.time=0
        self.distance=distance
        #self.capacity=0

    def getHalt(self,x) -> Halt:
        if x==0:
            return self.halts["G"]
        if x==1:
            return self.halts["E"]
        if x==2:
            return self.halts["D"]
        if x==3:
            return self.halts["C"]
        if x==4:
            return self.halts["B"]
        if x==5:
            return self.halts["A"]
        if x==6:
            return self.halts["O"]
        if x==7:
            return self.halts["O"]
        if x==8:
            return self.halts["G"]
        if x==9:
            return self.halts["E"]
    
    def step(self,command):
        """
        0 - V=1/ед.времени
        1 - V=2/ед.времени
        3 - Выбрать путь 1
        4 - Выбрать путь 2
        5 - Пропустить ход
        """
        self.time+=1


        # if self.isDone==True:
        #     self.score=0
        #     return self.encode(self.x,self.y,self.distance),self.score, self.isDone

        # if  command==4:
        #     if self.distance<2:
        #         self.score=1
        #         self.getDistance()
        #         return self.encode(self.x,self.y,self.distance),self.score, self.isDone
        #     else:
        #         self.score=-5000
        #         self.getDistance()
        #         self.map[self.x][self.y]=0
        #         self.isDone=True
        #         return self.encode(self.x,self.y,self.distance),self.score, self.isDone
            
        if command==0:
            if self.distance>0:
                if self.y<(len(self.map[self.x])-1):

                    if self.y!=0:
                        self.map[self.x][self.y]=0
                    self.y=self.y+1
                    self.score=-1
                    self.map[self.x][self.y]=1
                else:
                    self.score=-5000
                    self.isDone=True
                    self.getDistance()
                    return self.encode(self.x,self.y,self.distance),self.score, self.isDone

                halt=self.getHalt(self.x)
                
                if self.y==(len(self.map[self.x])-1):
                    self.score=halt.passengers
                    halt.passengers=0
                    for h in halt.X:
                        self.map[h[0]][h[1]]=9

            else:
                if self.y==(len(self.map[self.x])-1):
                    halt=self.getHalt(self.x)
                    for h in halt.X:
                        self.map[h[0]][h[1]]=halt.simbol
                self.score=-5000
                self.isDone=True
                self.getDistance()
                return self.encode(self.x,self.y,self.distance),self.score, self.isDone
        
        
        if  command==1: 
            if self.distance>1: 
                if self.y<(len(self.map[self.x])-2):
                    if self.y!=0:
                        self.map[self.x][self.y]=0  
                    self.y=self.y+2
                    self.score=-1.5
                    self.map[self.x][self.y]=1
                else:
                    self.score=-5000
                    self.isDone=True
                    self.getDistance()
                    return self.encode(self.x,self.y,self.distance),self.score, self.isDone

                halt=self.getHalt(self.x)
       
                if self.y==(len(self.map[self.x])-1):
                    self.map[self.x][self.y]=0
                    halt.isLocked=True
                    self.score=halt.passengers
                    halt.passengers=0
                    for h in halt.X:
                        self.map[h[0]][h[1]]=9
            else:
                if self.y==(len(self.map[self.x])-1):
                    halt=self.getHalt(self.x)
                    for h in halt.X:
                        self.map[h[0]][h[1]]=halt.simbol
                self.score=-5000
                self.isDone=True
                self.getDistance()
                return self.encode(self.x,self.y,self.distance),self.score, self.isDone
            
            
            #self.map[self.x][self.y]=1
        
        if  command==2:
            if self.y==(len(self.map[self.x])-1):
                halt=self.getHalt(self.x)
                self.map[self.x][self.y]=halt.simbol
                for coord in halt.X:
                    if coord[1]==0:

                        self.x=coord[0]
                        self.y=coord[1]

                for h in halt.X:
                    self.map[h[0]][h[1]]=halt.simbol
            else:
                self.score=-10000
                #self.map[self.x][self.y]=0
                self.isDone=True
                self.getDistance()
                if self.y!=0:
                    self.map[self.x][self.y]=0
                return self.encode(self.x,self.y,self.distance),self.score, self.isDone

        if  command==3:   
            if self.y==(len(self.map[self.x])-1):
                halt=self.getHalt(self.x)
                self.map[self.x][self.y]=halt.simbol
                for coord in reversed(halt.X):
                    if coord[1]==0:
                        self.x=coord[0]
                        self.y=coord[1]

                for h in halt.X:
                    self.map[h[0]][h[1]]=halt.simbol
            else:
                self.score=-10000
                #self.map[self.x][self.y]=0
                self.isDone=True
                self.getDistance()
                if self.y!=0:
                    self.map[self.x][self.y]=0
                return self.encode(self.x,self.y,self.distance),self.score, self.isDone

        
        self.getDistance()

        if self.time>100:           
           self.isDone=True
           self.score=1000
        return self.encode(self.x,self.y,self.distance),self.score, self.isDone

    def encode(self,player_x,player_y,distance):
        i = player_x
        i *= 10
        i += player_y
        i *= 3
        i += distance
        return i

    
    def decode(self,i):
        out=[]
        out.append(i%10)
        i=i // 10
        out.append(i%10)
        i=i // 10
        out.append(i)
        assert(0<=i<10)
        return reversed(out)

    def getDistance(self):
        if self.y<(len(self.map[self.x])-1):#проверка размерности
            if (self.map[self.x][self.y+1]!=1 and self.map[self.x][self.y+1]!=9):
                self.distance=1
                for i in range(self.y+1,len(self.map[self.x])):
                    if (self.map[self.x][i]!=1 and self.map[self.x][i]!=9):
                        self.distance=2
                    else:
                        self.distance=1
                        break
            else:
                self.distance=0
        # if  self.y==(len(self.map[self.x])-1):
        #     self.distance=1