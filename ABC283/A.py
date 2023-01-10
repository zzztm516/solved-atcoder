def main():

    A, B = map(int, input().split())

    ans = A
    for i in range(B - 1):
        ans *= A

    print(ans)

if __name__ == '__main__':
    main()