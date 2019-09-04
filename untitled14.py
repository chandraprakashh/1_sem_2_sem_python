# -*- coding: utf-8 -*-
"""
Created on Tue May  7 12:18:27 2019

@author: hp
"""

import matplotlib
import matplotlib.pyplot as abhi

grid = abhi.GridSpec(2,2 , wspace = 0.4 , hspace = 0.9)


label1 = ["USA" , "INDIA" , "UK"]

value1 = [60,80,90]

color1 = ["r" ,"g" ,"b"]


abhi.pie(value1,labels=label1,colors = color1 , explode =(0,0,0) , radius =2.1 , autopct ="%1.1f%%")
abhi.legend()
abhi.show()