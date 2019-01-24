# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 09:20:20 2019

@author: Quito
"""

from pylab import*
from simpson import*
def f(t):
    return -t**3/6+5*t**2/3-25*t/6+7
s=simpson(f,0,2,8)
s