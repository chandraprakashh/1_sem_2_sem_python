# -*- coding: utf-8 -*-
"""
Created on Tue May  7 11:45:15 2019

@author: hp
"""

import matplotlib
import matplotlib.pyplot as abhi


grid = abhi.GridSpec(4,4 , wspace = 0.5 , hspace = 0.6)
x = [1980,1985,1990,1995,2000,2005,2010,2015]
y1 = [10,20,30,25,50,60,70,80]

y2 = [5,10,17,20,15,30,35,40]

y3 = [8,16,24,2,40,48,56,64]

abhi.subplot(grid[0,0])

abhi.subplot(grid[0,1])

abhi.subplot(grid[0,2])

abhi.subplot(grid[0,3])

abhi.subplot(grid[1,0])

abhi.subplot(grid[1,1])
abhi.subplot(grid[1,2])
abhi.plot(x,y1)
abhi.subplot(grid[1,3])
abhi.plot(x,y2)
abhi.subplot(grid[2,0])
abhi.subplot(grid[2,1])
abhi.subplot(grid[2,2])
abhi.plot(x,y3 ,label = "INDIA" , color="r")
abhi.subplot(grid[2,3])
abhi.subplot(grid[3,0])
abhi.subplot(grid[3,1])
abhi.subplot(grid[3,2])
abhi.subplot(grid[3,3])

abhi.plot(x,y)

abhi.show()
