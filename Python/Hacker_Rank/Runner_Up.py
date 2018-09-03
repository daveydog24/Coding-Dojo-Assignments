'''
Runner Up Assignment
Created By: David Wukelic
Utilizing tab spacing


'''
# n = 5
# arr = map(int, input().split())
arr = [6, 6, 6, 6, 6, 5]
first = None
second = None

for value in arr:
    if not first:
        first = value
    if value > first:
        first = value
    elif not second:
        if value != first:
            second = value
    if value < 0:
        if value <= second and value != first:
            second = value
    else:
        if value >= second and value != first:
            second = value
    
print (second)