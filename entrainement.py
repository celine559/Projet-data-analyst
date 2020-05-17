# -*- coding: utf-8 -*-
"""
Created on Sat May  9 17:26:12 2020

@author: celin
"""

#faire un diagramme en bâton


import numpy as np
import pylab as pl
from random import*
#L=[1 for i in range(10)]+[2 for i in range(50)]+[3 for i in range(40)]
#bornes=np.arange(0.5,4,1)

#pl.hist(L,bins=3)
L=[randint(1,6) for i in range(1000)]

frequences=[L.count(k)/len(L) for k in range(1,7)]
print(frequences)
pl.bar(np.arange(1,7),frequences)
x=np.linspace(0,6,101)
L2=[1/6 for k in x]
pl.plot(x,L2,'-')
pl.show()
