

from PyQt5.sip import enableautoconversion
from Halt import Halt


class Bus:
    symbol=1
    action_space=4
    def __init__(self,x,y,map,halts) -> None:
        self.x=x
        self.y=y
        self.map=map
        self.score=0
        self.isDone=False
        self.halts=halts
        self.capacity=0

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
        if command==0:
            if self.y<(len(self.map[self.x])-1):
                if self.map[self.x][self.y+1]==1:#если впереди есть автобус, то штраф
                    self.score=self.score-5000
                    self.map[self.x][self.y]=0
                    self.isDone=True
                    return self.encode(self.x,self.y),self.score, self.isDone 

                self.map[self.x][self.y]=0
                self.y=self.y+1
                self.score=self.score-1
                self.map[self.x][self.y]=1

            halt=self.getHalt(self.x)
            if self.y==(len(self.map[self.x])-1) and halt.isLocked==False:
                halt.isLocked=True
                self.score=self.score+halt.passengers
                halt.passengers=0
                self.map[self.x][self.y]=9
            
            if  self.y==(len(self.map[self.x])-1) and halt.isLocked==True: #занято  
                self.score=self.score-5000
                self.isDone=True
                return self.encode(self.x,self.y),self.score, self.isDone    


    def encode(self,player_x,player_y):
        i = player_x
        i *= 10
        i += player_y
        return i

    
    def decode(self,i):
        out=[]
        out.append(i%10)
        i=i // 10
        out.append(i)
        assert(0<=i<10)
        return reversed(out)