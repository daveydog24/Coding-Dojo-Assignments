def bubble_sort(arr):
    length = len(arr) - 1

    for x in range(0, length):
        for i in range (0, length - x):
            if arr[i + 1] < arr[i]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

    return arr
    
x = [0, 9, 2, 15, 4, 1, 0, 11, 99, 3, 13, 25, 7, 9, 5, 1]
sort = bubble_sort(x)
print sort 