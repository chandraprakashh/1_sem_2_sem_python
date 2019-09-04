# -*- coding: utf-8 -*-
"""
Created on Thu May  2 11:12:34 2019

@author: hp
"""

rows = int(input("Please Enter the total Number of Rows  : "))
print("Nesting loop useing while loop")

i = 1
while(i <= rows):
    j = 1
    while(j <= i):        
       print("* ",end="")
       j = j + 1
    i = i + 1
    print();