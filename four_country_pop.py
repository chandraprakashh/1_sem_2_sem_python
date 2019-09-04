# -*- coding: utf-8 -*-
"""
Created on Fri May  3 09:48:58 2019

@author: hp
"""


import matplotlib

import matplotlib.pyplot as Core

year = [1980,1985,1990,1995,2000,2005,2010,2015]

India_pop = [10,20,30,40,50,60,70,80]

AUS_pop = [5,10,15,20,25,30,35,40]

UK_pop = [8,16,24,32,40,48,56,64]

Chaina_pop = [11,22,33,44,55,66,77,88]


Core.plot(year, India_pop, label = "INDIA" , color="r")

Core.plot(year , AUS_pop , label ="AUS" , color ="g")

Core.plot(year , UK_pop , label="UK" , color ="Y")

Core.plot(year , Chaina_pop , label="Chaina" , color ="b")

Core.xlabel("year")

Core.ylabel("population")

Core.title("population of INDIA , AUS ,UK & Chaina")

Core.legend()

Core.show()
