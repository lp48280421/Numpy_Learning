#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat May  5 22:30:12 2018

@author: pengli
"""
# JuZhen De JiBen YunSuan2

import numpy as np

A = np.array([[2,3,4],
              [3,5,8],
              [2,7,3]])

a = np.mean(A)
b = np.average(A,axis=0)

c = np.median(A)

d = np.argmax(A)
e = np.argmin(A,axis=0)

f = np.cumsum(A,axis=0)
g = np.cumsum(A)

h = np.diff(A)
i = np.diff(A,axis=0)

j = np.nonzero(A)
k = np.sort(A,axis=0)

l = np.transpose(A)
m = A.T

n = np.clip(A[0],3,5)
print(n)