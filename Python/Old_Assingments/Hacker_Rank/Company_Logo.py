'''
Runner Up Assignment
Created By: David Wukelic
Utilizing tab spacing
'''

s = "aabbbccde"
s = list(s)
s.sort()
dictionary = {}
first = ('', 0)
second = ('', 0)
third = ('', 0)

# trying to reverse or sort the list
# sorted(s)
# s.reverse()

# working with a list instead of dictionary....
# new_list = []

# for value in s:
#     if value not in new_list:
#         new_list.append([value, 0])
#     else:
#         new_list[value][1] += 1
# print new_list

for value in s:
    if value not in dictionary:
        dictionary[value] = 1
        # dictionary.update({'value': 1}).format(value)
    else:
        dictionary[value] += 1

for value in dictionary.items():
    if value[1] > first[1]:
        third = second
        second = first
        first = value
    elif value[1] == first[1] and second[1] < 1:
        third = second
        second = value
    elif value[1] > second[1] and second[1] == 0:
        third = second
        second = value
    elif value[1] == second[1] and third[1] == 0:
        third = value
    elif value[1] > third[1] and third[1] == 0:
        third = value

print first[0],first[1]
print second[0],second[1]
print third[0],third[1]
