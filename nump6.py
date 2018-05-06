#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May  6 15:25:21 2018

@author: pengli
"""
#JuZhen De FenGe

import numpy as np

A = np.arange(12).reshape(3,4)


print "A:", A
print "v_split:", np.split(A,2,axis=1)
print "h_split:", np.split(A,3,axis=0)
#print "h_split:", np.split(A,2,axis=0)

print "h_split:", np.array_split(A,2,axis=0)

print "vsplit:", np.vsplit(A,3)
print "hsplit:", np.hsplit(A,2)