# Finding Characters Assignment  
# Created By: David Wukelic
# Utilizing tab spacing

'''
Write a program that takes a list of strings and a string containing a single 
character, and prints a new list of all the strings containing that character.

example: 

# input
word_list = ['hello','world','my','name','is','Anna']
char = 'o'
# output
new_list = ['hello','world']

'''

def Find_Character(char, arr):
    new_list = []
    for x in arr:
        for c in x:
            if c == char:
                new_list.append(x)
                break
    print new_list
word_list = ['hello','world','my','name','is','Anna']
char = 'o'

Find_Character(char, word_list)