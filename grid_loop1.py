# -*- coding: utf-8 -*-
"""
Created on Tue May  7 16:22:33 2019

@author: hp
"""

import matplotlib
import matplotlib.pyplot as abhi

grid = abhi.GridSpec(3,3 , wspace = 1.2 , hspace = 1.1)


label1 = ["USA" , "INDIA" , "UK"]

value1 = [60,80,90]

color1 = ["r" ,"g" ,"b"]

abhi.subplot(grid[0,0])
year = [1980,1985,1990,1995,2000,2005,2010,2015]
USA = [5,10,17,20,15,30,35,40]

abhi.subplot(grid[0,1])

abhi.plot(year,USA , label ="USA" , color ="g")
abhi.legend()
abhi.title("Poplation of USA ")
abhi.xlabel("Year")
abhi.ylabel("Poplation")

abhi.subplot(grid[0,2])

nishu1 = ["USA" , "INDIA" , "UK"]

nishu2 = [60,80,90]

abhi.subplot(grid[1,0])
abhi.pie(nishu2,labels=nishu1, explode =(0,0.1,0) , radius =1.9 , autopct ="%1.1f%%")
abhi.legend()
abhi.subplot(grid[1,1])
abhi.subplot(grid[1,2])
abhi.pie(value1,labels=label1,colors = color1 , explode =(0,0,0) , radius =2.1 , autopct ="%1.1f%%")
abhi.legend()
abhi.subplot(grid[2,0])
year = [1980,1985,1990,1995,2000,2005,2010,2015]

INDIA = [10,0,30,25,50,60,70,80]

abhi.plot(year,INDIA , label ="INDIA" , color="r")
abhi.legend()
abhi.title("Poplation of INDIA ")
abhi.xlabel("Year")
abhi.ylabel("Poplation")

abhi.subplot(grid[2,1])

x= [5,9,1,7]
y= [4,3,7,10]
abhi.subplot(grid[2,2])
abhi.plot(x,y , label ="line" , color="r")
abhi.legend()
abhi.title("Graph")
abhi.xlabel("x-assis")
abhi.ylabel("y-assis")


abhi.show()
