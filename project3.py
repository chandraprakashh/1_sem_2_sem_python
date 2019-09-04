# -*- coding: utf-8 -*-
"""
Created on Wed May  8 09:17:04 2019

@author: hp
"""

import numpy as np
import pylab as pl
x = np.linspace(0, 2*np.pi, 100)
pl.plot(x, np.sin(x), "-x", label=u"sin")
pl.plot(x, np.random.standard_normal(len(x)), 'o', label=u"rand")
leg = pl.legend(numpoints=3)
l = leg.legendHandles[1]
l._legmarker.set_xdata(l._legmarker.get_xdata()[1:2])
l._legmarker.set_ydata(l._legmarker.get_ydata()[1:2])
pl.xlabel("x-Assis")
pl.ylabel("y-Assis")
pl.title("graph")
##or
#l._legmarker.set_markevery(3)
pl.show()