def main():

    N = int(input())
    A_list = list(map(int, input().split()))
    Q = int(input())
    for i in range(Q):
        query = list(map(int, input().split()))

        if query[0] == 1:
            A_list[query[1] - 1] = query[2]

        if query[0] == 2:
            print(A_list[query[1] - 1])

if __name__ == '__main__':
    main()