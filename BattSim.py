import subprocess as sp
from utils import *
from math import exp
import numpy as np


class BattSim:

    def __init__(self, Kbatt: list, Cbatt: float, R0: float, R1: float, C1: float, R2: float, C2: float, ModelID: int):
        self.Kbatt = kBatt
        self.Cbatt = Cbatt
        self.R0 = R0
        self.R1 = R1
        self.C1 = C1
        self.R2 = R2
        self.C2 = C2
        self.ModelID = ModelID
        self.alpha1 = exp(- (delta / (R1 * C1)))
        self.alpha2 = exp(- (delta / (R2 * C2)))

        self.h = 0

        self.soc = 0.5

    def simulate(self) -> list:
        """
        Simulate the battery and return the voltage and current
        returns:
        [Vbatt, Ibatt, soc, Vo] as lists of floats
        """
        self.octave.stdin.write(f's\n')
        return self.__fetchResponse()

    def kill(self) -> int:
        self.octave.stdin.write(f'quit\n')
        return self.octave.wait(timeout=1)


if __name__ == '__main__':
    battSim = BattSim()
    Vbatt, Ibatt, soc, Vo = battSim.simulate()

    print(f'Vbatt: {Vbatt}')
    print(f'Ibatt: {Ibatt}')
    print(f'Vo: {Vo}')

    battSim.kill()
