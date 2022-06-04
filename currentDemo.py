# currentsim py demo

from CurrentSIM import *
import matplotlib.pyplot as plt

# T, I = staircase()
# T, I = deepdischarge()
# T, I = rectangular()
T, I = rectangularnew()

# plot the the current (I) vs time (T)
plt.plot(T, I)
plt.xlabel('Time (s)')
plt.ylabel('Current (A)')
plt.show()
