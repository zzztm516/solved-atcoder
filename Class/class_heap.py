# 優先度付きキュー(ヒープ)と呼ばれるデータ構造を用いて簡単に行うことができます．優先度付きキュー
# は，「要素の push」「最小要素の pop」がともに O(log N) 時間で行えるキューです．
# 優先度付きキュー用pythonライブラリ -> heapq

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
    return arr

class heap():

    def __init__(self, arr):
        self.list = []
        for num in arr:
            self.insertheap(num)

    def node_up(self):
        #1次元ヒープでは親ノードのindexは子ノードを"index"としたとき、(index - 1) // 2になる
        index = len(self.list) - 1
        while index !=0 and self.list[index] < self.list[(index -1) // 2]:
            swap(self.list, index, (index -1) // 2)
            index = (index -1) // 2

    def insertheap(self, num):
        self.list.append(num)
        self.node_up()

    def node_down(self):
        if len(self.list) == 2 and self.list[0] > self.list[1]:
            swap(self.list, 0, 1)
    
        index = 0
        while 2 * index + 2 <= len(self.list) - 1: #右の子ノードのindex番号がリストの全体の要素数より大きいなら終了
            index_child_left = 2 * index + 1
            index_child_right = 2 * index + 2
            child_left = self.list[index_child_left]
            child_right = self.list[index_child_right]
            if self.list[index] > min(child_left, child_right):
                if child_left <= child_right:
                    swap(self.list, index, index_child_left)
                    index = index_child_left
                else:
                    swap(self.list, index, index_child_right)
                    index = index_child_right

    def get_num_pop_min(self):
        if len(self.list) == 1:
            ans = self.list[0]
            self.list.pop(0)
            return ans

        else:
            ans = self.list[0]
            self.list[0] = self.list.pop(-1)
            self.node_down()
            return ans

    def pop_min(self):
        if len(self.list) == 1:
            self.list.pop(0)

        else:
            self.list[0] = self.list.pop(-1)
            self.node_down()

def main():
    my_list = [3, 1, 88, 15, 2, 61, 17, 2, 2, 18, 21]
    my_heap = heap(my_list)


    my_heap.insertheap(100)



    my_my_heap = my_heap
    print(my_heap.list)
    print(my_my_heap.list)
    my_my_heap.pop_min()

    print(my_heap.list)
    print(my_my_heap.list)

if __name__ == '__main__':
    main()