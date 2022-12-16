# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 09:53:56 2022

@author: ともき
"""

N,A,B = map(int, input().split())
lis = []
lis_check = []
temp,check = 1,A

while temp != N + 1:
    temp_temp = temp
    while temp > 0:
        lis_check.append(temp%10)
        temp //= 10
    temp = temp_temp
    while check != B + 1 :
        if sum(lis_check) == check:
            lis.append(temp)
        check += 1       
    temp += 1
    check = A 
    lis_check = []
    
print(sum(lis))

"""
解答

N, A, B = map(int, input().split())
print(sum(i for i in range(N+1) if A <= sum(map(int,str(i))) <= B))
"""