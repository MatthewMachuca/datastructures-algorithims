def insertionSort(arr):
    for i in range(1,len(arr)):
        temp = arr[i]
        j = i-1
        while (j >= 0) and (arr[j] > temp):
            arr[j+1] = arr[j]
            j -= 1
                
        arr[j+1]=temp
    return arr



print(insertionSort([2,2,4,55,34,19,22,5,6,3,9]))