"""
あとでーß
import sys

def main():

    N, W= map(int, input().split())

    w_lis = []
    v_lis = []
    ratio_lis = []

    for i in range(N):
        temp_w,temp_v =map(int, input().split())
        w_lis.append(temp_w)
        v_lis.append(temp_v)
        ratio_lis.append(temp_v / temp_w)

    check_W = 0
    sum_v = 0
   
    while check_W != W:
        if check_W + w_lis[ratio_lis.index(max(ratio_lis))] <= W and max(ratio_lis) >0:
            sum_v += v_lis[ratio_lis.index(max(ratio_lis))]
            check_W += w_lis[ratio_lis.index(max(ratio_lis))]
            ratio_lis[ratio_lis.index(max(ratio_lis))] = -1

        elif check_W + w_lis[ratio_lis.index(max(ratio_lis))] > W and max(ratio_lis) >0:
            ratio_lis[ratio_lis.index(max(ratio_lis))] = -1
    
        if check_W + min(w_lis) > W or max(ratio_lis) < 0:
            break

    print(sum_v)

if __name__ == "__main__":
  main()
"""