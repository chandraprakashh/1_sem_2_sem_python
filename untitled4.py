# -*- coding: utf-8 -*-
"""
Created on Sat May  4 14:22:39 2019

@author: BSDU
"""


import matplotlib

import matplotlib.pyplot as hp

fig, axes = hp.subplots(3, 4, figsize=(8,4))

x = [1,2,8]

y=[4,6,9]

hp.subplot(341)
hp.plot(x,y)

x1= [4,6,9]

y1=[2,6,3]

hp.subplot(344)
hp.plot(x1,y1)

x2 = [6,2,9]

y2 =[2,6,9]

hp.subplot(347)
hp.plot(x2,y2)

x3 = [1,2,8]

y3=[5,6,3]

hp.subplot(349)
hp.plot(x3,y3)


