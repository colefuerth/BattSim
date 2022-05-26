
import numpy as np
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