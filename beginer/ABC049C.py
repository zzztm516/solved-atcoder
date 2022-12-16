# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 15:06:28 2022

@author: ともき
"""


S = input()
words_lis = ["dream","dreamer","erase","eraser"]
flg = 0
while S != "":
    for x in words_lis:
        if S.endswith(x):
            S = S[:-len(x)]
            break
    else:
        print("NO")
        flg = 1
        break

if flg == 0:
    print("YES")
    
"""
解答

S = input()
while S:
  for x in ["dream","dreamer","erase","eraser"]:
    if S.endswith(x):
      S = S[:-len(x)]
      break
  else:
    print("NO")
    break
else:
  print("YES")
  
  
接頭語がどれであるかは一意に定まらないけれど、接尾語がどれであるかなら一意に定まる
for ... else ...やwhile ... else ...のelseは、forやwhileが正常終了した場合に作動し、breakで異常終了した場合には作動しない
"""