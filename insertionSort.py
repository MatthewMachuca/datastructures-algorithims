def insertionSort(arr):
    for i in range(1,len(arr)):
        temp = arr[i]
        for j in range(i-1,-1,-1):
            if arr[j] > temp:
                arr[i] = arr[j]
                arr[j] = temp
    return arr



print(insertionSort([2,5,6,3,9]))