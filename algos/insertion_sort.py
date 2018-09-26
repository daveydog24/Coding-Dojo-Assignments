def insertion_sort(arr):
    length = len(arr)

    for x in range(0, length):
        if x > 0: 
            while arr[x] < arr[x-1]:
                arr[x], arr[x-1] = arr[x-1], arr[x]
                x -= 1
                if x == 0:
                    break

    return arr

x = [9, 2, 15, 4, 0, 7, 9, 5, 1, 28, 2009, 2020, 5050, 69, 99, 88, 19, 67]
sort = insertion_sort(x)
print sort 
