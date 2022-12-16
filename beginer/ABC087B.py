# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 08:48:42 2022

@author: ともき
"""


a, b, c, x = map(int, [input() for _ in range(4)])
count = 0
n_a , n_b ,n_c = 0, 0, 0
while n_a != a + 1:
    while n_b != b + 1:
        while n_c != c + 1:
            if 500*n_a + 100*n_b + 50*n_c == x:
                count += 1
            n_c += 1
        n_b += 1
        n_c = 0
    n_a += 1
    n_b = 0
    n_c = 0
print(count)

"""解説

import itertools as it

A, B, C, X = map(int, [input() for _ in range(4)])

count = 0
for a, b, c in it.product(range(A+1), range(B+1), range(C+1)):
  if 500*a + 100*b + 50*c == X:
    count += 1
print(count)
"""