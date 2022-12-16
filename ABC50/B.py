# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 07:48:17 2022

@author: ともき
"""


N = input()
lis = list(map(int, input().split()))
M = int(input())
ans = []
for i in range(M):
    A,B = map(int, input().split())
    temp = lis[A-1]
    lis[A-1] = B
    ans.append(sum(lis))
    lis[A-1] = temp
[print(i) for i in ans]