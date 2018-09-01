"""filename: 1.2 Plot.py"""

import matplotlib.pyplot as pl
import numpy as np

x = np.arange(0, 1, 0.01)  
y = -1 * x * np.log(x) - (1 - x) * np.log(1 - x)
pl.figure(figsize=(10,6))  
pl.plot(x, y,label="$H(x)=-x\log(x)-(1-x)\log(1-x)$")

pl.grid()
pl.legend()
pl.show()

"""--------------------------------------"""

x = np.arange(0, 1, 0.01)  
y = -1 * x * np.log(x) - (1 - x) * np.log(1 - x)
pl.figure(figsize=(10,6))  
pl.plot(x, y,label="$\log$")

pl.grid()
pl.legend()
pl.show()

"""--------------------------------------"""
