'''
Print Consecutive Numbers Assignment
Created By: David Wukelic
Utilizing tab spacing


Read an integer n

Without using any string methods, try to print the following:

Note that "" represents the values in between.

Example:

Input Format
3 

Output Format
123 

'''

n = 133
counter = 0
number = 1
sum = 0 

while n > 0:
    if counter < 9:
        sum = (sum * 10) + number
    elif counter >= 9 and counter < 99:
        sum = (sum * 100) + number
    else:
        sum = (sum * 1000) + number
    counter += 1
    number += 1
    n -= 1

print (sum)