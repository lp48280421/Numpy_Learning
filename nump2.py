#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri May  4 20:39:35 2018

@author: pengli
"""

#JuZhen de JiBen YunSuan

import numpy as np

a = np.array([[1,2],
              [8,10]])
b = np.eye(2)

c = a + b
d = a **2
e = a * b
f = np.dot(a,b)
g = (a==2)
h = (a>3)
i = np.sin(a)
j= np.random.random((2,3))
k = np.max(a)
l = np.max(a,axis=0)

m = np.sum(a)
n = np.sum(a,axis=1)

print(n)

