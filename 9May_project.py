# -*- coding: utf-8 -*-
"""
Created on Thu May  9 10:11:30 2019

@author: Administrator
"""

import matplotlib
import matplotlib.pyplot as abhi 
from matplotlib import style


fig, axes =abhi.subplots(3,3, figsize=(5,4))

x=[2,5,2]
y=[2,3,1]

abhi.subplot(337)
abhi.plot(x,y , label="Demo1", color="r")
abhi.xlabel("x")
abhi.ylabel("y")


######Scetter#######
abhi.subplot(332)
abhi.scatter(x,y , label="Demo1", color="c")
abhi.legend()


########Bar############
abhi.subplot(336)
abhi.bar(x,y,label="Demo1", color="g")
abhi.xlabel("x")
abhi.ylabel("y")

###pie###########
abhi.subplot(334)
x1 =["Abhi","Nishu","Chandu"]
y1 =[40,20,40]
z1 = ["r" , "g" , "c"]
abhi.pie(y1,labels=x1, explode =(0.1,0.1,0.1) ,colors=z1 ,radius=1.0 ,autopct ="%1.1f%%")
abhi.xlabel("x")
abhi.ylabel("y")


######style#########
abhi.subplot(339)
abhi.plot(x,y , label="Demo1", color="c")
abhi.xlabel("x")
abhi.ylabel("y")
abhi.grid(True)
abhi.legend()
abhi.show()