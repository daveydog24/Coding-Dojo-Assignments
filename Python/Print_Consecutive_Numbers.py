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
    n = 3
    sum = 1
    counter = 1

    while counter < n:
        multiplier = counter
        temp_sum = 0

        while multiplier >= 0:
            temp_sum += (10**multiplier)
            multiplier -= 1

        sum += temp_sum
        counter += 1   
    print (sum)