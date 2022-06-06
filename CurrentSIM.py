# Current Simulation Utilities
import numpy as np
from itertools import product

def staircase(delta=5, Nsp=5, Ns=5, Nb=4, Imag=[-40, -80, -120, -160]):
    """
    delta = milliseconds between each step
    Nsp = number of staircase pulses/groups (repeat modifier)
    Ns = samples per block in staircase
    Nb = number of blocks per stairway
    Imag = list of current magnitudes for each step in mA, same number of elements as Nb

    returns:
    (time, current) as lists of floats in mS and mA
    """

    T = np.arange(0, Nsp * Ns * delta * Nb, delta)
    T = T * 10 ** (-3) # convert to milliseconds
    I = np.zeros(Nsp * Ns * Nb)

    for k in range(Nb * Nsp):
        I[k * Ns: (k+1) * Ns] = Imag[k % Nb] * np.ones(Ns)

    I = I * 10 ** (-3) # convert to mA
    return T, I


def deepdischarge(delta=5, Ns=5, Nb=2, Imag=[0, -1000]):
    """
    delta = milliseconds time of each step
    Ns = number of steps per block
    Nb = number of blocks
    Imag = list of current magnitudes for each step in mA, same number of elements as Nb

    returns:
    (time, current) as lists of floats in mS and mA
    """
    T = np.arange(0, delta * Ns * Nb, delta)
    T = T * 10 ** (-3) # convert to milliseconds

    I = np.zeros(Ns * Nb)

    for k in range(Nb):
        I[k * Ns: (k+1) * Ns] = Imag[k] * np.ones(Ns)
    I = I * 10 ** (-3) # convert to mA
    return T, I

# for some reason this is identical to the deepdischarge function???
def rectangular(delta=1000, Ns=500, Nb=2, Imag=[-1000, 0]):
    """
    delta = milliseconds time of each step
    Ns = number of steps per wave
    Nb = number of waves
    Imag = list of current magnitudes for each step in mA, same number of elements as Nb

    returns:
    (time, current) as lists of floats in mS and mA
    """

    T = np.arange(0, delta * Ns * Nb, delta)
    T = T * 10 ** (-3) # convert to milliseconds
    I = np.zeros(Ns * Nb)
    for k in range(Nb):
        I[k * Ns: (k+1) * Ns] = Imag[k] * np.ones(Ns)

    I = I * 10 ** (-3) # convert to mA
    return T, I


def rectangularnew(I1=-0.5, I2=0.5, delta=100*10**(-3), Tc=10, D=100):
    """
    delta =  Sampling delta time in seconds
    Tc = Pulse-Width in seconds
    D = Total time in seconds
    I1,I2 = current values for wave halves

    returns:
    (I, T) as lists of floats in mA and ms
    """

    Ns_pulse = int(Tc / delta) # Number of samples in one on-off pulse
    Np = int(D / Tc) # Number of on-off pulses
    Nsp2 = int(Ns_pulse / 2) # Number of samples in each half of apulse
    Nb = 2 # Number of blocks = on + off pulse
    Nt = int(D / delta) # Total number of samples
    Imag = [I1, I2] # Current vector
    T = np.arange(0, D, delta) # Time vector
    I = Imag[0] * np.ones(Nt) # Current vector
    for k in range(Nb * Np):
        I[k*Nsp2 : (k+1)*Nsp2] = Imag[k % Nb] * np.ones(Nsp2)

    # if (Np * Ns_pulse != Nt):
    #     print("Warning: Np * Ns_pulse ~= Nt")
    #     Q = Nt - Np * Ns_pulse
    #     I[k * Nsp2:k * Nsp2 + Q] = I[:Q]

    I = I * 10 ** (-3) # convert to mA

    return I, T



# My own function that I made earlier

from math import log10

# generate a square wave +- 0.5V, at 0.01s intervals, for 10s
def squareWave(amplitude, period, duration, sampleRate=10, offset=0):
    """
    Generate a square wave with the given amplitude, period, duration, and sample rate.
    amplitude = upper and lower limit in Amps
    period = period of a full wave in seconds
    duration = duration of the sample in seconds
    sampleRate = number of samples per second in Hz
    offset = offset of the wave in volts

    returns:
    (amps, time) as lists of floats
    """
    a = []
    t = [round(i, round(log10(sampleRate)))
         for i in np.arange(0, duration, 1/sampleRate)]
    for i in t:
        if i % period < period / 2:
            a.append(amplitude + offset)
        else:
            a.append(-amplitude + offset)
    return (a, t)