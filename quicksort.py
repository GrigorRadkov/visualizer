import random
import numpy as np

def partition(arr, start, end):
    
    pivotVal = arr[end]

    pind = start

    for i in range(start, end):
        if arr[i] < pivotVal:
            arr[i], arr[pind] = arr[pind], arr[i]
            pind = pind + 1

    arr[pind], arr[end] = arr[end], arr[pind]
    
    return pind

def quicksort(arr, start, end):
    
    if start < end:

        pi = partition(arr, start, end)

        quicksort(arr, start, (pi - 1))
        quicksort(arr, pi + 1, end)

    yield arr

