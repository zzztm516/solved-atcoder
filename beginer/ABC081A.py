# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 12:14:29 2022

@author: ともき
"""

"""各桁の取り出し
s = int(input())
list = []
while s > 0:
    list.append(s%10)
    s //= 10
list.reverse()
print(list)
"""

s = int(input())
list = [0,0,0]
while s > 0:
    list.append(s%10)
    s //= 10
list.reverse()
print(list[0]+list[1]+list[2])


"""
解答

print(input().count("1"))
"""