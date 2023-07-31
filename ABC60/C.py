import sys

def main():

    #N, T, *t = map(int, open(0).read().split())

    
    N, T= map(int, input().split())
    t_lis = list(map(int, input().split()))
    

    sum = 0

    for i in range(N - 1):
        if t_lis[i+1] - t_lis[i] < T:
            sum += t_lis[i+1] - t_lis[i]
        else:
            sum += T

    print(sum+T)

if __name__ == "__main__":
  main()