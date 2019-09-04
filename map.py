# -*- coding: utf-8 -*-
"""
Created on Mon May 13 10:42:54 2019

@author: Administrator
"""

import requests

api_key = "_your_api_key_"

url = "https://goo.gl/maps/QGs5TLGaAjdaG6oN8"

center = "Dehradun"
zoom = 10

r = requests.get(url + "center =" + center + "&zoom =" +
                   str(zoom) + "&size = 400x400&key =" +
                             api_key + "sensor = false") 


f = open('address of the file location ', 'wb') 
f.write(r.content) 
f.close() 