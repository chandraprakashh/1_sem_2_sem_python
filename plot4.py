# -*- coding: utf-8 -*-
"""
Created on Fri May  3 09:12:10 2019

@author: hp
"""

import matplotlib
import matplotlib.pyplot as dell

year = [1991,1996,2001,2006,2011,2016]
pop_India = [10,15,20,25,30,80]
pop_USA = [15,30,45,60,90,105]

dell.plot(year,pop_India , color="r")
dell.plot(year , pop_USA , color ="g")
dell.xlabel("year")
dell.ylabel("population")
dell.title("population of INDIA & USA")
dell.show()