import sys

def main():

    N,K = map(int, input().split())

    num_list = []

    for i in range(N):
        array = list(map(int, input().split()))
        num_list.append(array)

    num_list.sort()

    for i in range(len(num_list)):
        K -= num_list[i][1]
        if K <= 0:
            print(num_list[i][0])
            break

if __name__ == "__main__":
    main()