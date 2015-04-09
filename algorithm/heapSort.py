#!/usr/bin/env python
# coding=utf-8

def parent(i):
    '''
    父节点下标
    '''
    if (i % 2):
        return (i - 1) >> 1
    else:
        return (i - 2) >> 1 # floor((i - 1)/2)

def left(i):
    '''
    左儿子下标
    '''
    return (i << 1) + 1 # 2i + 1

def right(i):
    '''
    右儿子下标
    '''
    return (i << 1) + 2 # 2i + 2

def min_heapify(A, i, heap_size, offset=0):
    '''最小堆化A[i]为根的子树，伪码如下：
       MIN-HEAPIFY(A, i)
       1  l ← LEFT(i)
       2  r ← RIGHT(i)
       3  if l <= heap-size[A] and A[l] < A[i] // A[i]，A[LEFT[A]]中找出最小的
       4    then least ← l
       5    else least ← i
       6  if r <= heap-size[A] and A[r] < A[least] // A[i]，A[LEFT[A]]，A[RIGHT[i]]中找出最小的
       7    then least ← r
       8  if least != i // A[i]为最小时结束，否则继续递归
       9    then exchange A[i] ↔ A[least] // 交换A[i]，A[least]，使得满足最小堆性质
       10        MIN-HEAPIFY(A, least) // 递归
           
       # 注：上述下标是从1开始的，编程时都从0开始了。
       T(n) = O(lgn)
                                                           
       Args:
            A (Sequence): 序列A
            i (int): 下标i
            heap_size (int): 存放在A中的堆元素个数
            offset (int): 取值偏移量（只用在了heap_sort）
    '''
    l, r = left(i), right(i)
    if l < heap_size and A[l + offset] < A[i + offset]:
        least = 1
    else:
        least = i

    if r < heap_size and A[r + offset] < A[least + offset]:
        least = r
    
    if least != i:
        A[i + offset], A[least + offset] = A[least + offset], A[i + offset]
        print least, heap_size, offset, i
        min_heapify(A, least, heap_size, offset)

def build_min_heap(A):
    '''
    构造成最小堆，伪码如下：
    BUILD-MIN-HEAP(A)
    1  heap-size[A] ← length[A] // 堆元素个数为数组大小
    2  for i ← floor(length[A]/2) downto 1 // 自最后个父结点向上
    3    do MIN-HEAPIFY(A, i) // 最小堆化A[i]为根的子树
    
    T(n) = O(n)
    
    Args:
        A (Sequence): 序列A
    '''
    heap_size = len(A)
    parent_last = parent(heap_size - 1) # 最后一个的下标的父亲
    for i in range(parent_last, -1, -1): # parent_last downto 0
        min_heapify(A, i, heap_size)

def heap_sort_reverse(A):
    '''
    堆排序（逆序），伪码如下：
    HEAPSORT-REVERSE(A)
    1  BUILD-MIN-HEAP(A) // 构造成最小堆
    2  for i ← length[A] downto 2
    3    do exchange A[1] ↔ A[i] // 最小元素A[1]与A[n]互换
    4       heap-size[A] ← heap-size[A] - 1 // 减小heap-size[A]
    5       MIN-HEAPIFY(A, 1) // 保持最小堆性质
 
    T(n) = O(nlgn)

    Args:
        A (Sequence): 序列A
    '''
    build_min_heap(A)
    heap_size = len(A)
    for i in range(heap_size - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heap_size -= 1
        min_heapify(A, 0, heap_size)

def heap_sort(A):
    '''
    堆排序，伪码如下：
    HEAPSORT(A)
    1  for i ← 1 to length[A] - 1 // 从第一位到倒数第二位
    2    sub_heap_size = length[A] - i + 1 // i开始的子树的堆大小
    3    for j ← floor(sub_heap_size/2) downto 1 // 从子树最后个父结点向上，以将该子树构造成最小堆
    4      do MIN-HEAPIFY(A[i..length[A]], j) // 让i开始的子树的j为根的子树保持最小堆性质
    
    T(n) = O(n^2)
    
    Args:
        A (Sequence): 序列A
    '''
    heap_size = len(A)
    for i in range(0, heap_size - 1):
        sub_heap_size = heap_size - i # 子树堆大小
        sub_p_last = parent(sub_heap_size - 1) # 子树堆大小
        for j in range(sub_p_last, -1 ,-1):
            min_heapify(A, j, sub_heap_size, i) # i为子树在A中的偏移量

def heap_sort2(A):
    '''
    亦可在heap_sort_reverse时，拼接正序结果，其T(n) = O(nlgn)。
    或者，由heap_sort_reverse获得逆序结果后reversed，线性时间即可。
    这两种方式，相较于heap_sort都要好很多。
    '''
    build_min_heap(A)
    heap_size = len(A)
    R = []
    for i in range(heap_size - 1, 0, -1):
        R.append(A[0])
        A[0], A[i] = A[i], A[0]
        heap_size -= 1
        min_heapify(A, 0, heap_size)
    R.append(A[0])
    return R

if __name__ == '__main__':
    import random, timeit

    items = range(10)
    random.shuffle(items)

    def test_heap_sort():
        print(items)
        heap_sort(items)
        print(items)

    def test_heap_sort_reverse():
        print(items)
        heap_sort_reverse(items)
        print(items)

    test_methods = [test_heap_sort ]
    for test in test_methods:
        name = test.__name__
        t = timeit.Timer(name + '()', 'from __main__ import ' + name)
        print(name + ' takes time : %f' % t.timeit(1))

