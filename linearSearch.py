def linearSearcg(arr, num):
    for i in range(0, len(arr)):
        if arr[i] == num:
            return i
    return - 1

print(linearSearcg([1,2,3,4,5] , 4))