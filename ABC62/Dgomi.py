import heapq

def main():
    N = int(input())
    num_list = list(map(int, input().split()))
    
    left_heap = num_list[:N]
    right_heap = num_list[(3 * N - 1 - (N - 1)):]
    print(left_heap, right_heap)
    print(num_list)

    right_heap = [-1 * i for i in right_heap]#最大値を取り出したいため、符号を逆にしたheapをつくる

    heapq.heapify(left_heap)
    heapq.heapify(right_heap)

    count = 0
    factor_right = 0
    factor_left = 0

    while count != N:
        
        if num_list[N + factor_left] - left_heap[0] >= -1 * right_heap[0] - num_list[(3 * N - 1 - N) - factor_right]:
            heapq.heappushpop(left_heap, num_list[N + factor_left])
            factor_left += 1

        else:
            heapq.heappushpop(right_heap, -1 * num_list[(3 * N - 1 - N) - factor_right])
            factor_right += 1
        
        count += 1

    print(sum(left_heap) + sum(right_heap))

if __name__ == '__main__':
    main()