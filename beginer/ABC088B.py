# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 10:15:14 2022

@author: ともき
"""

N = int(input())
lis = list(map(int, input().split()))
lis.sort(reverse=True)
i = 0
sum = 0
while i < N:
    if i%2==0:
        sum += lis[i]
    else:
        sum -= lis[i]
    i += 1
print(sum)

"""
解答

_ = input()
a = sorted(map(int,input().split()), reverse=True)
print(sum(a[::2]) - sum(a[1::2]))
"""