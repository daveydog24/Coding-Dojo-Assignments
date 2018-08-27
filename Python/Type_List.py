'''
Created By: David Wukelic
Utilizing tab spacing
Assignment: Type List

Write a program that takes a list and prints a message for each element 
in the list, based on that element's data type.

Your program input will always be a list. For each item in 
the list, test its data type. If the item is a string, concatenate 
it onto a new string. If it is a number, add it to a running sum. 
At the end of your program print the string, the number and an analysis 
of what the list contains. If it contains only one type, print 
that type, otherwise, print 'mixed'.

Here are a couple of test cases. Think of some of your 
own, too. What kind of unexpected input could you get?

# Examples

# 1 
# input
l = ['magical unicorns',19,'hello',98.98,'world']
# output
"The list you entered is of mixed type"
"String: magical unicorns hello world"
"Sum: 117.98"

# 2 
# input
l = [2,3,1,7,4,12]
# output
"The list you entered is of integer type"
"Sum: 29"

# 3
# input
l = ['magical','unicorns']
#output
"The list you entered is of string type"
"String: magical unicorns"
'''

def Type_List(test_list): 
    list_type = ''
    final_sum = 0
    final_string = ''
    int_test = False
    string_test = False 

    # turns the correct switches on to identify the type of list  
    # loops through the list and adds up all the integers and/or concatenates the strings in the list 
    for value in test_list:
        if isinstance(value, int) or isinstance(value, float):
            final_sum += value
            int_test = True
        elif isinstance(value, str):
            final_string += (value + " ")
            string_test = True

    # identifies which string to print based on the list type
    if int_test and string_test:
        list_type = "The list you entered is of mixed type"
    elif not int_test and string_test:
        list_type = "The list you entered is of string type"
    else:
        list_type = "The list you entered is of int type"

    print list_type
    if final_sum:
        print "Sum:", final_sum
    if final_string:
        print "String: " + final_string


mixed_list = ['magical unicorns',19,'hello',98.98,'world']
integer_list = [1,2,3,4,5]
string_list = ["Spiff", "Moon", "Robot"]

Type_List(mixed_list)
Type_List(integer_list)
Type_List(string_list)