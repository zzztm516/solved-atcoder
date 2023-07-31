def main():
    H, W = map(int, input().split())

    print('#' * (W + 2))

    for i in range(H):
        print('#' + input() + '#')

    print('#' * (W + 2))

if __name__ == '__main__':
    main()