



def selSort(arr):
    for i in range(0, len(arr)):
        lowest = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[lowest]:
                lowest = j
        temp = arr[lowest]
        arr[lowest] = arr[i]
        arr[i] =temp
    return arr



print(selSort([3,6,1,8,6,3,5]))