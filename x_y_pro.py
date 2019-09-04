# -*- coding: utf-8 -*-
"""
Created on Fri May  3 10:08:01 2019

@author: hp
"""

import matplotlib
import matplotlib.pyplot as hp

x = [2,4,6,8,10,12,14,16]
y1 = [3,6,9,12,15,18,21,24]

hp.plot(x,y1,label="x1 & y1 value")


y2 = [5,10,15,20,25,30,35,40]

hp.plot(x,y2,label="x1 & y2 value")


y3 = [7,14,21,28,35,42,49,56]

hp.plot(x,y3,label="x1 & y3 value")


y4 = [9,18,27,36,45,54,63,72]

hp.plot(x,y4,label="x1 & y4 value")


y5 = [11,22,33,44,5,66,77,88]

hp.plot(x,y5,label="x1 & y5 value")



hp.xlabel("x-asis")
hp.ylabel("y-asis")
hp.title("Five line Graph")

hp.legend()

hp.show()
