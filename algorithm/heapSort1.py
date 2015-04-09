#!/usr/bin/env python
# coding=utf-8
 
import sys 

def left_child(node): 
    return node * 2 + 1 

def right_child(node): 
    return node * 2 + 2 

def parent(node): 
    if (node % 2): 
        return (i - 1) / 2 
    else: 
        return (i - 2) / 2 

def max_heapify(array, i, heap_size): 
    l = left_child(i) 
    r = right_child(i) 

    largest = i 
    if l < heap_size and array[l] > array[i]: 
        largest = l 

    if r < heap_size and array[r] > array[largest]: 
        largest = r 

    if largest != i: 
        array[i], array[largest] = array[largest], array[i] 
        max_heapify(array, largest, heap_size) 

def build_max_heap(array): 
    for i in range(len(array) / 2, -1, -1): 
        max_heapify(array, i, len(array)) 


def heap_sort(array): 
     build_max_heap(array) 
     for i in range(len(array) - 1, 0, -1): 
         array[0], array[i] = array[i], array[0] 
         max_heapify(array, 0, i) 


if __name__ == "__main__": 
    array = [0, 2, 6, 98, 34, -5, 23, 11, 89, 100, 7] 
    heap_sort(array) 

    for a in array: 
        sys.stdout.write("%d " % a) 

