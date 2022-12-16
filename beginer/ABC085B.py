# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 11:24:50 2022

@author: ともき
"""

N = int(input())
lis = list(map(int, [input() for _ in range(N)]))
lis.sort()

i = 0
while i < N-1:
    if lis[i] == lis[i+1]:        
        del lis[i+1]
        N -= 1
        i -= 1
    i += 1
print(len(lis))

"""
解答

N = int(input())
print(len(set(input() for _ in range(N))))
setは重複を許さない集合
"""