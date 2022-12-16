# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 15:56:07 2022

@author: ともき
"""


K,S= map(int, input().split())
cou = 0
for i in range(K + 1):
    for j in range(K + 1):
        k = S - i - j
        if k > K or k < 0:
            continue
        else:
            cou += 1
print(cou)
    