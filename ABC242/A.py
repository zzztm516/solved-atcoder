# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 14:38:53 2022

@author: ともき
"""


A,B,C,X = map(int, input().split())
if A >= X:
    print(1.000000000000)
elif A+1 <= X <= B:
    print(C/(B-A))
else :
    print(0.000000000000)