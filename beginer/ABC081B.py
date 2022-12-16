# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 15:49:48 2022

@author: ともき
"""


N = int(input())
l = []
l = list(map(int, input().split()))
flag = 0
count = 0
num = 0
while flag != 1:
    for num in range(N):
        if l[num]%2 == 0:
            l[num] /= 2
            if num == N - 1:
                count += 1               
        else:
            flag = 1
            break
print(count)
        

"""
解答

_ = input()
A = [*map(int, input().split())]

count = 0
while not any(a%2 for a in A):
    A = [a/2 for a in A]
    count += 1
print(count)
"""