import random
from typing import List

class Halt:
    
    def __init__(self,X:List,simbol,name) -> None:
        self.X=X
        self.simbol=simbol
        self.passengers=0
        self.name=name
        self.isLocked=False
        

    def generate(self):
        self.passengers=self.passengers+random.randint(1,10)

    