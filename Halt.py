import random
from typing import List

class Halt:
    
    def __init__(self,X:List,simbol,name,passengers) -> None:
        self.X=X
        self.simbol=simbol
        self.passengers=passengers
        self.name=name
        self.isLocked=False
        self.generator=self.passengers
        

    def generate(self):
        self.passengers=self.generator#self.passengers+random.randint(1,10)

    