#終わってない

def main():

    S_list = list(input())
    start = 0
    finish = 0
    count = 0
    check_list = []
    if S_list[0] != '(' or S_list[len(S_list) - 1] != ')' or S_list.count('(') != S_list.count(')'):
        return print('No')
    
    for i in range(len(S_list)):
        #position = i - finish
        #print(position)
        if S_list[i] == '(':
            check_list.append(S_list[i])

        elif S_list[i] == ')':
            check_list.append(S_list[i])
            finish = len(check_list)
            index_num = [n for n, v in enumerate(check_list) if v == '(']
            start = index_num[len(index_num) - 1]
            #print(start, finish)
            #print('before', check_list)
            del check_list[start:finish]
            #print('after', check_list)
            #print(S_list)


        else:
            if S_list[i] in check_list :
                #print(S_list[position])
                return print('No')
            else:
                check_list.append(S_list[i])


    print("Yes")

    
if __name__ == '__main__':
    main()