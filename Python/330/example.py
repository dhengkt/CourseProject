import matplotlib.pyplot as plt
import numpy as np

radians = np.arange(30)/30*2.0*np.pi

plt.plot(radians, np.sin)
plt.tiltle("Sine Graph")