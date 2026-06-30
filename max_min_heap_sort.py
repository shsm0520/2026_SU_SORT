#max and min share implemantaion only differ is comparator 
from utility import read_default_list

def fix_up():
    pass
    
def fix_down(heap, index, heap_size, mode):
    target = index
    left = 2 * index + 1
    right = 2 * index + 2

    # Switch condition based on the mode
    if mode == "max":
        if left < heap_size and heap[left] > heap[target]:
            target = left
        if right < heap_size and heap[right] > heap[target]:
            target = right
    elif mode == "min":
        if left < heap_size and heap[left] < heap[target]:
            target = left
        if right < heap_size and heap[right] < heap[target]:
            target = right

    if target != index:
        heap[index], heap[target] = heap[target], heap[index]
        fix_down(heap, target, heap_size, mode)

def movingaround(heap, mode):
    n = len(heap)
    for i in range(n - 1, 0, -1):
        heap[0], heap[i] = heap[i], heap[0]
        fix_down(heap, 0, i, mode)
    return heap

def maxheap_sort(arra=None):
    def build_max_heap(arr):
        heap = arr[:]
        n = len(heap)
        for i in range(n // 2 - 1, -1, -1):
            fix_down(heap, i, n, "max")
        return heap

    arra = build_max_heap(arra)
    arra = movingaround(arra, "max")
    return arra

def minheap_sort(arra=None):
    def build_min_heap(arr):
        heap = arr[:]
        n = len(heap)
        for i in range(n // 2 - 1, -1, -1):
            fix_down(heap, i, n, "min")
        return heap

    arra = build_min_heap(arra)
    arra = movingaround(arra, "min")
    return arra


if __name__ == "__main__":

    sort_list = read_default_list()  # None을 전달하여 read_default_list()를 호출하도록 함
    print("Original List:")
    print(sort_list)
    
    print("\nSorted using Max Heap (Ascending):")
    print(maxheap_sort(sort_list))
    
    print("\nSorted using Min Heap (Descending):")
    print(minheap_sort(sort_list))