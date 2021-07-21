
from Halt import Halt


class Road:
    def __init__(self,start:Halt,finish:Halt,coeff) -> None:
        self.start=start
        self.finish=finish
        self.coeff=coeff
