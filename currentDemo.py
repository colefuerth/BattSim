# currentsim py demo

from CurrentSIM import staircase
import matplotlib.pyplot as plt

T, I = staircase()

# plot the the current (I) vs time (T)
plt.plot(T, I)
plt.xlabel('Time (s)')
plt.ylabel('Current (A)')
plt.show()
