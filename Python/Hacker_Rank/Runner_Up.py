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
highest = None
second_highest = None

for value in arr:
    if not highest:
        print "in non highest loop", value
        highest = value
    else:
        if value > highest:
            second_highest = highest
            highest = value
        else:
            if not second_highest:
                second_highest = value
            if value > second_highest and value != highest:
                second_highest = value

print (second_highest)