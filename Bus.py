

from typing import Reversible
from PyQt5.sip import enableautoconversion
from Halt import Halt


class Bus:
    simbol=1
    action_space=4
    map=None
    halts={}
    def __init__(self,x,y,map,halts) -> None:
        self.x=x
        self.y=y
        self.map=map
        self.score=0
        self.isDone=False
        self.halts=halts
        self.time=0
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
        """
        self.time+=1
        if command==0:
            if self.y<(len(self.map[self.x])-1):
                if self.map[self.x][self.y+1]==1:#если впереди есть автобус, то штраф
                    self.score=-5000
                    #self.map[self.x][self.y]=0
                    self.isDone=True
                    return self.encode(self.x,self.y),self.score, self.isDone 

                self.map[self.x][self.y]=0
                self.y=self.y+1
                self.score=-1
                self.map[self.x][self.y]=1
            else:
                self.score=-5000
                self.isDone=True
                return self.encode(self.x,self.y),self.score, self.isDone

            halt=self.getHalt(self.x)
            if  self.y==(len(self.map[self.x])-1) and halt.isLocked==True: #занято  
                self.score=-5000
                self.isDone=True
                return self.encode(self.x,self.y),self.score, self.isDone
            
            if self.y==(len(self.map[self.x])-1) and halt.isLocked==False:
                halt.isLocked=True
                self.score=halt.passengers
                halt.passengers=0
                for h in halt.X:
                    self.map[h[0]][h[1]]=9

        

            #self.map[self.x][self.y]=1           
        
        if  command==1:   
            if self.y<(len(self.map[self.x])-1):
                if self.map[self.x][self.y+1]==1:#если впереди есть автобус, то штраф
                    self.score=-5000
                    #self.map[self.x][self.y]=0
                    self.isDone=True
                    return self.encode(self.x,self.y),self.score, self.isDone


                if (self.y+2)>(len(self.map[self.x])-1):
                    self.score=-5000
                    #self.map[self.x][self.y]=0
                    self.isDone=True
                    return self.encode(self.x,self.y),self.score, self.isDone

                if self.map[self.x][self.y+2]==1:#если впереди есть автобус, то штраф
                    self.score=-5000
                    #self.map[self.x][self.y]=0
                    self.isDone=True
                    return self.encode(self.x,self.y),self.score, self.isDone  

                self.map[self.x][self.y]=0    
                self.y=self.y+2
                self.score=-1.5
                self.map[self.x][self.y]=1
            else:
                self.score=-5000
                self.isDone=True
                return self.encode(self.x,self.y),self.score, self.isDone

            halt=self.getHalt(self.x)

            if  self.y==(len(self.map[self.x])-1) and halt.isLocked==True: #занято  
                self.score=-5000
                self.isDone=True
                return self.encode(self.x,self.y),self.score, self.isDone

            if self.y==(len(self.map[self.x])-1) and halt.isLocked==False:
                halt.isLocked=True
                self.score=halt.passengers
                halt.passengers=0
                for h in halt.X:
                    self.map[h[0]][h[1]]=9
            
            
            
            #self.map[self.x][self.y]=1
        
        if  command==2:
            #print(len(self.map[self.x])-1)   
            if self.y==(len(self.map[self.x])-1):
                halt=self.getHalt(self.x)
                self.map[self.x][self.y]=halt.simbol
                for coord in halt.X:
                    if coord[1]==0:
                        self.x=coord[0]
                        self.y=coord[1]+1

                        if self.map[self.x][self.y]==1:#если впереди есть автобус, то штраф
                            self.score=-5000
                            #self.map[self.x][self.y]=0
                            self.isDone=True
                            return self.encode(self.x,self.y),self.score, self.isDone 
                        else:
                            self.map[self.x][self.y]=1
                            self.score=-1
                            break

                halt.isLocked=False
                for h in halt.X:
                    self.map[h[0]][h[1]]=halt.simbol
            else:
                self.score=-10000
                #self.map[self.x][self.y]=0
                self.isDone=True
                return self.encode(self.x,self.y),self.score, self.isDone 

        if  command==3:   
            if self.y==(len(self.map[self.x])-1):
                halt=self.getHalt(self.x)
                self.map[self.x][self.y]=halt.simbol
                for coord in reversed(halt.X):
                    if coord[1]==0:
                        self.x=coord[0]
                        self.y=coord[1]+1
                        if self.map[self.x][self.y]==1:#если впереди есть автобус, то штраф
                            self.score=-5000
                            #self.map[self.x][self.y]=0
                            self.isDone=True
                            return self.encode(self.x,self.y),self.score, self.isDone 
                        else:
                            self.map[self.x][self.y]=1
                            self.score=-1
                            break
                halt.isLocked=False
                for h in halt.X:
                    self.map[h[0]][h[1]]=halt.simbol
            else:
                self.score=-10000
                #self.map[self.x][self.y]=0
                self.isDone=True
                return self.encode(self.x,self.y),self.score, self.isDone

        if self.time>100:           
           self.isDone=True
           self.score=1000
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