'''
Runner Up Assignment
Created By: David Wukelic
Utilizing tab spacing


'''
n = 5
arr = map(int, input().split())
first = None
second = None

for value in arr:
    print value
    if not first:
        first = value
    if value >= first:
        first = value
    else:
        if not second:
            second = value
        if value <= first and value >= second:
            second = value
        
    # if value == first and value != second:
    #     second = value
    
print (second)