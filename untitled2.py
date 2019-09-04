# -*- coding: utf-8 -*-
"""
Created on Sat May  4 14:13:03 2019

@author: BSDU
"""

import matplotlib

import matplotlib.pyplot as hp

fig, axes = hp.subplots(1, 3, figsize=(8,4))

x = [1,2,8]

y=[4,6,9]

hp.subplot(131)
hp.plot(x,y)


hp.subplot(132)
hp.plot(x,y)



hp.subplot(133)
hp.plot(x,y)


