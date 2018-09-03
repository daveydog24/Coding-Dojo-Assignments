'''
Checkerboard Assignment
Created By: David Wukelic
Utilizing tab spacing
'''

rows = 15
stars_in_row = 30

while rows > 0:
    printed = ''
    stars = stars_in_row
    if rows % 2 == 0:
        while stars > 0:
            printed += "* "
            stars -= 1
    else:
        while stars > 0:
            printed += " *"
            stars -= 1
    rows -= 1
    print printed
