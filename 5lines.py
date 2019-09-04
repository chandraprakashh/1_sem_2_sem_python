# -*- coding: utf-8 -*-
"""
Created on Fri May  3 09:51:21 2019

@author: hp
"""

import matplotlib
import matplotlib.pyplot as hp

x1 = [2,4,6,8,10,12,14,16]
y1 = [3,6,9,12,15,18,21,24]

hp.plot(x1,y1,label="x1 & y1 value")

x2 = [4,8,12,16,20,24,28,32]
y2 = [5,10,15,20,25,30,35,40]

hp.plot(x2,y2,label="x2 & y2 value")

x3 = [6,12,18,24,30,36,42,48]
y3 = [7,14,21,28,35,42,49,56]

hp.plot(x3,y3,label="x3 & y3 value")

x4 = [8,16,24,32,40,48,56,64]
y4 = [9,18,27,36,45,54,63,72]

hp.plot(x4,y4,label="x4 & y4 value")

x5 = [10,20,30,40,50,60,70,80]
y5 = [11,22,33,44,5,66,77,88]

hp.plot(x5,y5,label="x5 & y5 value")



hp.xlabel("x-asis")
hp.ylabel("y-asis")
hp.title("Five line Graph")

hp.legend()

hp.show()
