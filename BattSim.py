import subprocess as sp
from utils import *


class BattSim:

    def __init__(self):
        self.octave = sp.Popen(["octave", "-W", "batterySimulator.m"],
                               stdin=sp.PIPE,
                               stdout=sp.PIPE,
                               stderr=sp.PIPE,
                               universal_newlines=True,
                               bufsize=0)
        self.Kbatt = [
            -9.082, 103.087, -18.185, 2.062, -0.102, -76.604, 141.199, -1.117
        ]

    def __resp(self):
        # confirm 'done' response from child
        line = octave.stdout.readline().strip()
        assert(line == 'done')

    # if octave.stdout.read() != 'coefficients':
    #     raise Exception('coefficients request not received')
    def setCoefficients(self, Kbatt):
        self.octave.stdin.write(f'k\n')
        self.octave.stdin.write(f'{" ".join(map(str,battery))}\n')
        self.__resp()


    def setCurrentDraw(self, I: list, T: list) -> None:
        # I and T are both lists containing the same number of elements for simulation. These can be developed however you choose
        self.octave.stdin.write(f'i\n')
        self.octave.stdin.write(f"{' '.join(map(str, I))}\n")
        self.octave.stdin.write(f"{' '.join(map(str, T))}\n")
        self.__resp()
                

    # for line in octave.stderr:
    #     print(line)

    # Fetch output
    def __fetchResponse(self):
        response = []
        while True:
            line = self.octave.stdout.readline().strip()
            if line == 'done':
                break
            response.append(list(map(float, line.split())))
        return response if len(response) > 1 else response[0]

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
