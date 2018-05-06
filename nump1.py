#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 22:00:58 2018

@author: pengli
"""
# JuZhen de ChuangJian
import numpy as np

a = np.array([12,3,4])

print(a)
print(a.dtype)

b = np.array([[4,5,9],
              [6,11,87]])
print(b)
print "b shape:",b.shape
print "b size:",b.size
print "b ndim:",b.ndim

c = np.zeros((3,4))
print(c)

d = np.ones((4,5),dtype=float)
print(d)
print(d.dtype)

e = np.empty((3,3))
print(e)

k = np.arange(1,10,2)
print(k)

i = np.linspace(1,12,12).reshape((3,4))
print(i)
print(i.shape)

#print("Hello World")
