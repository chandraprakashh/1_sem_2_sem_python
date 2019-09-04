# -*- coding: utf-8 -*-
"""
Created on Wed May  8 09:36:41 2019

@author: hp
"""

from matplotlib import pyplot as plt
import style
x = [5,2,7]
y = [2,16,4]
plt.plot(x,y)
plt.title('Info')
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.grid(True , color="g")
plt.show()

