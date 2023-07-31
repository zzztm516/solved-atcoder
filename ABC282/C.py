def main():

    N = int(input())
    S = list(input())
    flg = 1

    for i in range(N):
        if S[i] == '"' and flg == 0:
            flg = 1

        elif S[i] == '"' and flg == 1:
            flg = 0

        elif S[i] == ',' and flg == 1:
            S[i] = '.'

    print(''.join(S))
    
if __name__ == '__main__':
    main()