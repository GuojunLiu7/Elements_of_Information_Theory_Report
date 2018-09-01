"""filename: 1.1 Plot.py"""

import matplotlib.pyplot as pl
import numpy as np

x = np.arange(0, 4*np.pi, 0.01)  
y = np.log(x)  
pl.figure(figsize=(10,6))  
pl.plot(x, y,label="$ln(x)$")

pl.grid()
pl.legend()
pl.show()

"""--------------------------------------"""

x = np.arange(0, 4*np.pi, 0.01)  
y = np.log(x) - x + 1
pl.figure(figsize=(10,6))  
pl.plot(x, y,label="$ln(x) - x + 1$")

pl.grid()
pl.legend()
pl.show()

"""--------------------------------------"""

x = np.arange(0, 4*np.pi, 0.01)  
y = x * np.log(x)
pl.figure(figsize=(10,6))  
pl.plot(x, y,label="$xlog(x)$")

pl.grid()
pl.legend()
pl.show()

"""--------------------------------------"""

x = np.arange(0, 4*np.pi, 0.01)  
y = np.log(x) / x
pl.figure(figsize=(10,6))  
pl.plot(x, y,label="$log(x)/x$")

pl.grid()
pl.legend()
pl.show()

"""--------------------------------------"""

x = np.arange(0, 4*np.pi, 0.01)  
y = np.log(x) / x
pl.figure(figsize=(10,6))  
pl.plot(x, y,label="$log(x)/x$")

pl.grid()
pl.legend()
pl.show()