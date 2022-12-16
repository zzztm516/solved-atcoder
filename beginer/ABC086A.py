# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 11:57:56 2022

@author: ともき
"""


a,b = map(int, input().split())
if a*b%2 == 0:
    print("Even")
else:
    print("Odd")
    

"""
解答

a, b = map(int, input().split())
print("Odd" if a%2 and b%2 else "Even")
"""
