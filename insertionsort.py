#fix insertionsort
def insertionsort(arr):

    for i in range(1, len(arr)):

        j = i
        while j >= 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1

            yield arr
