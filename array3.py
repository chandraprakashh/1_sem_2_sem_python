# -*- coding: utf-8 -*-
"""
Created on Fri May 10 10:12:02 2019

@author: hp
"""

import numpy as np 

x = np.array([[1, 2], [3, 4], [5, 6]]) 
y = x[[0,1], [0,0]] 
print(y)