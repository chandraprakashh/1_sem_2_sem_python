# -*- coding: utf-8 -*-
"""
Created on Wed May  8 13:58:05 2019

@author: hp
"""

import socket

hostname = socket.gethostname()

IP = socket.gethostbyname(hostname)

print(hostname)
print(IP)