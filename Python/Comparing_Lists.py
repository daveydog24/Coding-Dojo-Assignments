# Compare List Assignment  
# Created By: David Wukelic
# Utilizing tab spacing

'''
Write a program that compares two lists and prints a message depending on if the 
inputs are identical or not.

Your program should be able to accept and compare two lists: list_one and list_two. 
If both lists are identical print "The lists are the same". If they are not identical
print "The lists are not the same." Try the following test cases for lists one and two:

'''

def Compare_Lists(first_list, second_list):
    compared_list_equal = True;
    if len(first_list) == len(second_list):
        for count, x in enumerate(first_list):
            if x != second_list[count]:
                compared_list_equal = False;
    else:
        compared_list_equal = False;
        
    if compared_list_equal:
        print "The lists are the same."
        return True;
    else:
        print "The lists are not the same."
        return False

# list_one = [1,2,5,6,2]
# list_two = [1,2,5,6,2]

list_one = [1,2,5,6,5]
list_two = [1,2,5,6,5,3]

# list_one = [1,2,5,6,5,16]
# list_two = [1,2,5,6,5]

# list_one = ['celery','carrots','bread','milk']
# list_two = ['celery','carrots','bread','cream']

Compare_Lists(list_one, list_two)
