import subprocess as sp
from utils import *

octave = sp.Popen(["octave", "octave/batterySimulator.m"],
                       stdin=sp.PIPE,
                       stdout=sp.PIPE,
                       stderr=sp.PIPE,
                       universal_newlines=True,
                       bufsize=0)

# Send octave commands to stdin
# assert(octave.stdout.read()  == 'coefficients: ')

battery = [
    -9.082, 103.087, -18.185, 2.062, -0.102, -76.604, 141.199, -1.117
]

# if octave.stdout.read() != 'coefficients':
#     raise Exception('coefficients request not received')
octave.stdin.write(f'{" ".join(map(str,battery))}\n')
octave.stdin.close()

# Fetch output
for line in octave.stdout:
    print('py:', line.strip())

# generate a square wave like in demoBatterySimulator.m
for v, t in zip(*squareWave(0.5, 10, 100)):
    print(t, v)
