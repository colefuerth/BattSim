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

    # delta    = 5; % milliseconds
    # Nsp     = iter; % #of staircase pulses
    # Ns      = 5; % #of samples for each pulse
    # Nb      = 4; % #of blocks
    # Imag    = [-40 -80 -120 -160]; % same as the #of blocks

    # T        = 0:delta:delta*Nsp*Ns*Nb-1 ;
    T = np.arange(0, Nsp * Ns * delta * Nb, delta)
    #  T        = T*10^-3;
    T = T * 10 ** (-3) # convert to milliseconds
    # T        = T';
    # T = np.transpose(T) # unnecessary

    # I = zeros(Nsp*Ns*Nb,1);
    I = np.zeros(Nsp * Ns * Nb)

    # l = 1;
    # for k = 1:Nb*Nsp
    for k in range(Nb * Nsp):
        #     I((k-1)*Ns+1:k*Ns) = Imag(l)*ones(Ns,1);
        I[k * Ns: (k+1) * Ns] = Imag[k % Nb] * np.ones(Ns)
    #     l = l+1;
    #     if(l == Nb+1)
    #         l = 1;
    #     end
    # end

    # I = I*10^-3;
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
    # delta = 5; % milliseconds
    # Ns = 10; % #of samples for each pulse
    # Nb = 2;
    # Imag = [0 -1000]; % same as the #of blocks

    # T = 0:delta:delta * Ns * Nb - 1;
    T = np.arange(0, delta * Ns * Nb, delta)
    # T = T * 10^ - 3;
    T = T * 10 ** (-3) # convert to milliseconds
    # T = T';
    # l = 1;

    I = np.zeros(Ns * Nb)

    # for k = 1:Nb
    for k in range(Nb):
        I[k * Ns: (k+1) * Ns] = Imag[k] * np.ones(Ns)
    #     I((k - 1) * Ns + 1:k * Ns) = Imag(l) * ones(Ns, 1);
    #     l = l + 1;
    #     if (l == Nb + 1)
    #         l = 1;
    #     end
    # end
    # I = I * 10^ - 3;
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

    # %          delt = delta;
    # %          pulsewidth = T;
    # %          pulsetotal = D;
    # delta = 1000; % milliseconds
    # Ns = 500; % #of samples for each pulse
    # Nb = 2;
    # Imag = [-1000 0]; % same as the #of blocks


    # T = 0:delta:delta * Ns * Nb - 1;
    T = np.arange(0, delta * Ns * Nb, delta)
    # T = T * 10^ - 3;
    T = T * 10 ** (-3) # convert to milliseconds
    # T = T';
    # l = 1;
    # for k = 1:Nb
    I = np.zeros(Ns * Nb)
    for k in range(Nb):
        I[k * Ns: (k+1) * Ns] = Imag[k] * np.ones(Ns)
    #     I((k - 1) * Ns + 1:k * Ns) = Imag(l) * ones(Ns, 1);
    #     l = l + 1;
    #     if (l == Nb + 1)
    #         l = 1;
    #     end
    # end

    # I = I * 10^ - 3;
    I = I * 10 ** (-3) # convert to mA
    # I = I';
    return T, I


def rectangularnew(I1=-0.5, I2=0.5, delta=100*10**(-3), Tc=10, D=100):
    """
    delta =  Sampling delta time in seconds
    Tc = Pulse-Width in seconds
    D = Total time in seconds
    I1,I2 = current values for wave halves
    """

    # Ns_pulse = T / delta; % Number of samples in one on-off pulse
    Ns_pulse = int(Tc / delta)
    # Np = floor(D / T); % Number of on-off pulses
    Np = int(D / Tc)
    # Nsp2 = Ns_pulse / 2; % Number of samples in each half of apulse
    Nsp2 = int(Ns_pulse / 2)
    # Nb = 2; % Number of blocks = on + off pulse
    Nb = 2
    # Nt = D / delta; % Total number of samples
    Nt = int(D / delta)
    # Imag = [I1 I2]; % Current vector
    Imag = [I1, I2]
    # T = 0:delta:D; % Time vector
    T = np.arange(0, D, delta)
    # T = T(2:end)';
    # T = T[1:]
    # I = Imag(1) * ones(length(T), 1);
    I = Imag[0] * np.ones(Nt)
    # l = 1;
    # for k = 1:Nb * Np
    for k in range(Nb * Np):
        I[k*Nsp2 : (k+1)*Nsp2] = Imag[k % Nb] * np.ones(Nsp2)
    #     I((k - 1) * Nsp2 + 1:k * Nsp2) = Imag(l) * ones(Nsp2, 1);
    #     l = l + 1;

    #     if (l == Nb + 1)
    #         l = 1;
    #     end

    # end

    # # if (Np * Ns_pulse ~= Nt)
    # if (Np * Ns_pulse != Nt):
    #     print("Warning: Np * Ns_pulse ~= Nt")
    # #     Q = Nt - Np * Ns_pulse;
    #     Q = Nt - Np * Ns_pulse
    # #     I(k * Nsp2 + 1:k * Nsp2 + Q) = I(1:Q);
    #     I[k * Nsp2:k * Nsp2 + Q] = I[:Q]
    # # end

    # I = I * 10^ - 3;
    I = I * 10 ** (-3) # convert to mA

    return T, I



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