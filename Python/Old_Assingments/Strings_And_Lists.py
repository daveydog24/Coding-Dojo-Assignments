# Strings and Lists 
# Created By: David Wukelic
# Utilizing tab spacing


################################ find and replace ################################
my_string = "If monkeys like bananas, then I must be a monkey!"

# output: If monkeys like bananas, then I must be a monkey!
print my_string

# output: 3
print my_string.find("monkey")

my_string = my_string.replace("monkey", "alligator")

# output: If alligators like bananas, then I must be a alligator!
print my_string

################################ min and max ################################
x = [2,54,-2,7,12,98]

# output: [2, 54, -2, 7, 12, 98]
print x

# output: -2
print min(x)

# output: 98
print max(x)

################################ first and last ################################
x = ["hello",2,54,-2,7,12,98,"world"]

# output: hello world
print x[0], x[len(x) - 1]

################################ new list ################################
x = [19,2,54,-2,7,12,98,32,10,-3,6]

# output: [19, 2, 54, -2, 7, 12, 98, 32, 10, -3, 6]
print x

x.sort()

# output: [-3, -2, 2, 6, 7, 10, 12, 19, 32, 54, 98]
print x

first_list = x[:len(x)/2] # optional first parameter of slice defaults to zero
second_list = x[len(x)/2:] # optional second parameter of slice defaults to the list's length

#output: first list [19, 2, 54, -2, 7]
print "first list", first_list

#output: second_list [12, 98, 32, 10, -3, 6]
print "second_list", second_list

second_list.insert(0,first_list)

#output: [[19, 2, 54, -2, 7], 12, 98, 32, 10, -3, 6]
print second_list
