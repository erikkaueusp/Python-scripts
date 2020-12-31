# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 17:32:22 2020

@author: crash
"""

def f(x):
    return 2**x

a = list(range(0,10))
b = map(f(a),a)