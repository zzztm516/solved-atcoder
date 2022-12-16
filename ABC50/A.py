# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 07:27:40 2022

@author: ともき
"""


A,op,B = map(str, input().split())
A = int(A)
B = int(B)
if op=="+":
    print(A+B)
else:
    print(A-B)