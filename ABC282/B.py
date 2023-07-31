def main():

    N, M = map(int, input().split())
    S = []
    count = 0
    
    for i in range(N):
        S.append(input())


    for i in range(N - 1):
        j = i + 1
        while j != N:
            for k in range(M):
                if S[i][k] == "o" or S[j][k] == "o" :
                    if k == M - 1:
                        count += 1
                else:
                    break
                k += 1

            j += 1
    print(count)
    

if __name__ == '__main__':
    main()