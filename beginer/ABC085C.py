# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 12:05:55 2022

@author: ともき
"""


N,Y = map(int, input().split())
a,b,c = 0,0,0
flg = 0
while a <= N:
    while b <= N - a:
        c = N - a - b
        if 10000 * c + 5000 * b + 1000 *a == Y:
            print("{} {} {}".format(c,b,a))
            flg = 1
            break
        if flg == 1:
            break
        b += 1
    if flg == 1:
        break
    a += 1
    b = 0
    
if flg == 0:
     print("{} {} {}".format(-1,-1,-1))
     
"""
解答

N, Y = map(int, input().split())
for n_10k in range(N+1):
  for n_5k in range(N-n_10k+1):
    n_1k = N - n_10k - n_5k
    if n_10k*10000 + n_5k*5000 + n_1k*1000 == Y:
        print(n_10k, n_5k, n_1k)
        exit()
print(-1, -1, -1)
"""