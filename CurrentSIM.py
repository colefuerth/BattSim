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
