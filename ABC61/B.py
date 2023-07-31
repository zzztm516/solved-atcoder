N,M = map(int, input().split())
go_list = []
return_list = []

for i in range(M):
    a,b = map(int, input().split())
    go_list.append(a)
    return_list.append(b)

for i in range(N):
    print(go_list.count(i+1) + return_list.count(i+1))
