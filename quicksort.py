import random
import numpy as np

def quicksort(arr, start, end):

    if start < end:
        # This would be the partition method, but it is embedded in the quicksort function to enable drawing with pysimplegui
        pivotVal = arr[end]
        pind = start

        for i in range(start, end):
            if arr[i] < pivotVal:
                arr[i], arr[pind] = arr[pind], arr[i]
                pind += 1
            yield arr
        arr[pind], arr[end] = arr[end], arr[pind]
        
        yield arr

        yield from quicksort(arr, start, (pind - 1))
        yield from quicksort(arr, pind + 1, end)

