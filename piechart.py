# -*- coding: utf-8 -*-
"""
Created on Thu May  9 11:36:22 2019

@author: Administrator
"""
import matplotlib.pyplot as abhi

x1 =["Abhi","Nishu","Chandu"]
y1 =[40,20,40]
z1 = ["r" , "g" , "c"]
abhi.pie(y1,labels=x1, explode =(0.0,0.0,0.0) ,colors=z1 ,radius=1.0 ,autopct ="%1.1f%%")
abhi.legend()
abhi.show() 