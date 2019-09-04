# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib
import matplotlib.pyplot as bsdu

grid = bsdu.GridSpec(2,2 , wspace=0.4 , hspace= 0.8)

Year = [2003,2004,2005,2006]
JAIPUR = [10,20,15,40]
BHILWARA=[10,30,14,40]
AJMER =[10,20,13,30]
RALIA =[20,10,30,15]


bsdu.subplot(grid[0,0])
bsdu.plot(Year, JAIPUR , label="JAIPUR", color="g")
bsdu.legend()
bsdu.title("Poplation of JAIPUR")
bsdu.xlabel("Year")
bsdu.ylabel("Poplation")


bsdu.subplot(grid[0,1])
bsdu.plot(Year, BHILWARA , label="BHILWARA", color="r")
bsdu.legend()
bsdu.title("Poplation of BHILWARA")
bsdu.xlabel("Year")
bsdu.ylabel("Poplation")


bsdu.subplot(grid[1,0])
bsdu.plot(Year, AJMER , label="AJMER", color="b")
bsdu.legend()
bsdu.title("Poplation of AJMER")
bsdu.xlabel("Year")
bsdu.ylabel("Poplation")

bsdu.subplot(grid[1,1])
bsdu.plot(Year, RALIA , label="RALIA", color="c")
bsdu.legend()
bsdu.title("Poplation of RALIA")
bsdu.xlabel("Year")
bsdu.ylabel("Poplation")
