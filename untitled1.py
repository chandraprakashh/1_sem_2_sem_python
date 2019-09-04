# -*- coding: utf-8 -*-
"""
Created on Sat May  4 14:09:37 2019

@author: BSDU
"""

import matplotlib

import matplotlib.pyplot as hp

fig, axes = hp.subplots(2, 3, figsize=(8,4))

x = [1,2,8]

y=[4,6,9]

hp.subplot(212)
hp.plot(x,y)