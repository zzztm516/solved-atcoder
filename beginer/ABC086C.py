# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 15:26:54 2022

@author: ともき
"""


t0, x0, y0 = 0, 0, 0
for _ in range(int(input())):
    t, x, y = map(int, input().split())
    if t >= abs(x)+abs(y):
        
    else:
        print("NO")
        break