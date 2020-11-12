# def selectionSort(arr):



#     for i in range(0, len(arr)-1):
        
#         for j in range(0, i):
#             m = arr[j]
            
#             if m > arr[j + 1]:
#                 m = arr[j + 1]
                
                
                
#            # if arr[j] > arr[j + 1]:
#             #    temp = arr[j]
#              #   arr[j] = arr[j + 1]
#               #  arr[j + 1] = temp
#             if j == i:
#                 temp = arr[j]
#                 arr[j] = arr[i]
#                 arr[i] = temp
#     return arr
# print(selectionSort([3, 6, 4, 9, 5, 7]))




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