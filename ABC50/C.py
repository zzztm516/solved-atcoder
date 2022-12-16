# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 07:58:17 2022

@author: ともき
"""


N = int(input())
lis = list(map(int, input().split()))
su = 0
MOD = 10**9 + 7
if N == 0:
    print(0)
elif N == 1:
    print(1)
elif N % 2 == 1:  
    temp = (N - 1) / 2
    while temp > 0:
        su += temp*2*2
        temp -= 1
    if su != sum(lis):
        print(0)
    else:
        print(int((2**((N - 1) // 2))%MOD))
else:
    temp = N / 2
    while temp > 0:
        su += (temp*2-1)*2
        temp -= 1
    if su != sum(lis):
        print(0)
    else:
        print(int((2**(N // 2))%MOD))

