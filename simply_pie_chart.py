# -*- coding: utf-8 -*-
"""
Created on Tue May  7 12:04:22 2019

@author: hp
"""

import matplotlib
import matplotlib.pyplot as abhi

label1 = ["USA" , "INDIA" , "UK"]

value1 = [60,80,90]

color1 = ["r" ,"g" ,"b"]

abhi.pie(value1,labels=label1,colors = color1)
abhi.legend()
abhi.show()