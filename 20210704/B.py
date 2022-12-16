# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 21:35:54 2021

@author: ともき
"""


p = int(input())
count = 0
while p != 0:
    n = 1
    i = 1
    while n<=p and i<=10:
        i += 1
        n = n*i
    p -= n/i
    count += 1
    
print(count)
    