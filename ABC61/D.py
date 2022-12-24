def main():
    N, M = map(int, input().split())
    INF = -float('inf')
    score = [0] + [INF] * (N - 1)
    abc = []

    for i in range(M):
        a, b, c =map(int, input().split())
        #tupleで追加
        abc.append((a -1, b - 1, c))

    for a, b, c in abc:
        score[b] = max(score[b], score[a] + c)
        ans = score[-1]

    #もう一度計算してsocreが変わればinf
    for a, b, c in abc:
        score[b] = max(score[b], score[a] + c)
    
    if ans == score[N - 1]:
        print(ans)
    
    else:
        print('inf')


if __name__ == '__main__':
    main()