def binarySearch(arr, num):
    p1 = 0
    p2 = len(arr) - 1
    p3 = int(p2 / 2)
    while p3 != num and p1 <= p2:
        if num < p3:
            p2 = p3 - 1
        else:
            p1 = p3 + 1
        p3 = int((p2 + p1) / 2)
    if arr[p3] == num:
        return num
    else:
        return -1
print('test')
print(binarySearch([1,2,3,4,5,6,7], 7))