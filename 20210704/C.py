# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 21:39:38 2021

@author: ともき
"""


list1 = input().split()
list2 = input().split()

n1 = int(list1[0])
n2 = int(list1[1])

answer = [n2//n1] * n1
n2 = n2 % n1

class C():
    list_a = list2
    def __init__(self, i):
    self.id = i
        
order = [C(i) for i in range(n1)]
order.list_a.sort()

    
for i in range (n2):
  answer[order.list_a[i].id] += 1        
    
for ans in answer:
    print(ans)