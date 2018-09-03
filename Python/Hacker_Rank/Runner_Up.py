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

n = 5
arr = [-10, 0, 10]
