from numpy import*
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import mlab
fig, ax = plt.subplots()
def f(x):
    return 5*sin(10*x)*sin(3*x)

x = linspace(0,4)
y = f(x)
plt.plot(x,y,'g--',)
plt.savefig('number 6.png',dpi=200)
plt.show()



