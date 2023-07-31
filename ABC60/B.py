import sys

def main():
    A,B,C = map(int, input().split())

    for i in range(B):
        if (A * i) % B == C:
            print("YES")
            break
        elif i == B - 1:
            print("NO")

if __name__ == "__main__":
  main()

""" good answer
import math
a,b,c=map(int,input().split())
print('YNEOS'[c%math.gcd(a,b)>0::2])

math.gcd(a,b) a,bでの最大条約数を求める
::すべての配列の要素
::2すべての配列の要素を2つ飛ばし

print('YNEOS'[False]) Yが出力
print('YNEOS'[True]) Nが出力

最大公約数について : https://qiita.com/drken/items/0c88a37eec520f82b788

なんで最大公約数で行けるかわからん

"""