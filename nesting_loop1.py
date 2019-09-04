# -*- coding: utf-8 -*-
"""
Created on Thu May  2 09:26:35 2019

@author: hp
"""

#user input useing foor loop 
rows = int(input("Please Enter the total Number of Rows  : "))
print("Nesting loop useing while loop")

i = 1
while(i <= rows):
    j = 1
    while(j <= i):        
        print('%d' %i, end = '  ')
        j = j + 1
    i = i + 1
    print()
    
    # useing for loop
    
user_input = int(input("enetr the total number of rows ::"))
print("Nesting loop useing for loop")

# for loop 

for i in range(1,user_input+1):
    for j in range(1,i+1):
        print("%d" %i, end = '  ')
    print()