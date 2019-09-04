# -*- coding: utf-8 -*-
"""
Created on Thu May  2 10:13:27 2019

@author: hp
"""
#useing for loop
user_input = int(input("enter the rows::"))
print("useing for loop")

for i in range(1 , user_input+1):
    for j in range(1 , i+1):
        print("# ",end="")
    print()
    
    		
# useing while loop
rows = int(input("Please Enter the total Number of Rows  : "))
print("Nesting loop useing while loop")

i = 1
while(i <= rows):
    j = 1
    while(j <= i):        
       print("* ",end="")
       j = j + 1
    i = i + 1
    print()
    