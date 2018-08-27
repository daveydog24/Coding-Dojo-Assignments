# Multiplies, Sum, Average Assignment  
# Created By: David Wukelic
# Utilizing tab spacing

# Multiples Part I
# Print odd numbers between 1 - 1,000
for count in range (1, 1001, 2):
    print count

# Multiples Part II
# Print the multiples of 5 between 5 - 1,000,000
for count in range (5, 1000001, 5):
    print count

# Sum List
# Create a program that prints the sum of all the values in the list: a = [1, 2, 5, 10, 255, 3]
Sum_list = [1, 2, 5, 10, 255, 3]
sum = 0
for i in Sum_list:
    sum += i
print sum

# Average List
# Create a program that prints the average of the values in the list: a = [1, 2, 5, 10, 255, 3]
Average_list = [1, 2, 5, 10, 255, 3]
sum = 0
length = len(Average_list)
for i in Average_list:
    sum += i
print (sum/length)