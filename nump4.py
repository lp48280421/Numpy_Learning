#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat May  5 22:58:01 2018

@author: pengli
"""
# JuZhen De Suo Yin

import numpy as np

A = np.array([3,9,0])
B = np.array([[2,8,5],
              [9,4,2],
              [5,0,3]])
a = A[1]

b = B[0]
c = B[0][1]
d = B[0,1]

e = B[0:3,1]
f = B[0:3][1]

#for row in B:
#    print(row)
#
#print('\n')
#
#for row in B.T:
#    print(row)

#JuZhen AnHang  or AnLie ZhanKai Wei ShuZu

g = B.flatten(order='c')
h = B.flatten(order='F')

for row in B.flat:
    print(row)
    
#print(h)