def main():

    S = input()
    count_doublezero = S.count('00')
    print(len(S) - count_doublezero)
    
if __name__ == '__main__':
    main()