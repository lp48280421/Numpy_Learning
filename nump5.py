#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May  6 15:01:06 2018

@author: pengli
"""
# JuZhen De HeBing

import numpy as np

A = np.array([1,1,1])
B = np.array([2,2,2])

A1 = A[np.newaxis,:]
B1 = B[np.newaxis,:]

A2 = A.reshape(3,1)
B2 = B.reshape(3,1)

C = np.vstack((A,B))
D = np.hstack((A,B)).reshape(2,3)

E = np.concatenate((A1,B1),axis=0)
F = np.concatenate((A1,B1),axis=1)

print(F)