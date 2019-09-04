# -*- coding: utf-8 -*-
"""
Created on Wed May  1 14:21:38 2019

@author: hp
"""

user_input =int(input("enter the number:"))

if(user_input>=60):
    print("first")
    
elif(user_input<60 and user_input>=50):
    print("second");
    
elif(user_input<50 and user_input>=45):
    print("Third");
    
elif(user_input<45):
    print("fail");

else:
    print("invaild input");
