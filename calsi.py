# -*- coding: utf-8 -*-
"""
Created on Mon May 13 21:21:24 2019

@author: hp
"""

while True:
    a= int (input("Enter the first number): "))
    b= int (input("Enter the second number): "))
    operator= str (input("Do you want to add, subtract, multiply, or divide? "))
    
    if operator==("divide"):
        print ("Your answer is", a / b)
        
    

    if operator==("multiply"):
        print ("Your answer is", a * b)
        
    
    if operator==("add"):
        print ("Your answer is", a + b)
        
    
    if operator==("subtract"):
        print ("Your answer is", a - b) 
     
    repeat=str (input("Do you want to perform another calculation(yes or no)? "))
    if repeat == "no":
        break
        




    
    
    
    
    
    
    
