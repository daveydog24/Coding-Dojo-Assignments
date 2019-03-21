# Javascript:
# var arr = [1,3,5,7]
# var temp = arr[0]
# arr[0] = arr[1]
# arr[1] = temp

# Python
# arr = [1,3,5,7]
# arr[0], arr[1] = arr[1], arr[0]

def push_front(arr, val):
    arr.append(val)
    length = len(arr)
    for i in range (1, length):
        arr[-i] = arr[-i - 1]
    
    arr[0] = val

    return arr

x = [0, 2, 3, 7 , 10]

z = push_front(x, 12)
print z