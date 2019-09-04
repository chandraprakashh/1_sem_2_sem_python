# -*- coding: utf-8 -*-
"""
Created on Fri May  3 13:02:19 2019

@author: hp
"""




 

x = range(0,5)

y = [i**2 for i in x]

plt.plot(x,y, lable  = 'x vs x**2)

plt.savefig('xsquare')

