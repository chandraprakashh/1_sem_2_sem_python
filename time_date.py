# -*- coding: utf-8 -*-
"""
Created on Mon May 13 13:56:04 2019

@author: hp
"""
###
import time


print(time.ctime())


####second mathod

hp = time.localtime(time.time())

print(time.asctime(hp))

print(time.strftime("%Y-%m-%d %H:%M:%S %Z" , hp))


################

print(time.tzname)

import datetime

print(datetime.date.today())
##Out[17]: datetime.date(2019, 5, 13)


###
from datetime import date

hp=date.today

hp=date.today()

print(hp.day)