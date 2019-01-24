# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 09:13:50 2019

@author: Quito
"""

def simpson(f,a,b,m):
    h=(b-a)/m
    s=0
    x=a
    for i in range(1,m):
        if i%2==1:
            s=s+4*f(x+i*h)
        else:
            s=s+2*f(x+i*h)
    s=h/3*(f(a)+s+f(b))
    return s