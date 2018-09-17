'''
Runner Up Assignment
Created By: David Wukelic
Utilizing tab spacing

n = 5
arr = [-10, 0, 10]
highest = None
second_highest = None

# loops through each value in the array
for value in arr:

    # if its the first time through it stores the first variable as the highest number
    if not highest:
        highest = value

    # checks value and if they are higher than the stored highest variable it stores the new value
    if value > highest:
        second_highest = highest
        highest = value

print (second_highest)
print (highest)

'''

# multiplier = 3
# def multiplying(num):
#     return num * multiplier

# arr = [-10, 0, 10]
# x = map(multiplying, arr)
# print x

# for i in range(len(arr)):
#     print arr[i]














def Kim(*args):
    test_string = ''
    test_int = 0
    for i in args:
        if type(i) is str:
            test_string += str(i) + " "
        if type(i) is int:
            test_int += i
        if type(i) is list:
            for value in i:
                test
                Kim(value)
    print ("string: {}, sum: {}".format(test_string, test_int))
    

Kim(1)
Kim(1,2,3)
Kim(1,2,3,"i love kim", "hey babe", 5)
Kim(1,2,3,"i love kim", "hey babe", 5, [1,2,3,4,5])
