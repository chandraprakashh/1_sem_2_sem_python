# -*- coding: utf-8 -*-
"""
Created on Fri May  3 09:11:10 2019

@author: hp
"""

import matplotlib
import matplotlib.pyplot as hp

x1 = [8,5,9,3,7]
y1 = [9,6,3,5,2]

hp.plot(x1,y1,label="Line1")

x2 = [7,6,3,5,2]
y2 = [8,2,6,9.3,2]

hp.plot(x2,y2,label="Line2")

hp.xlabel("x-asis")
hp.ylabel("y-asis")
hp.title("two line graph")

hp.legend()

hp.show()
