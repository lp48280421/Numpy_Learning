#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May  6 15:46:43 2018

@author: pengli
"""
#JuZhen De FuZhi

import numpy as np

a = np.arange(4)

b = a

b[1]=10

print a


a = np.arange(4)
c = a.copy()  #deep copy

c[1]=20

print a