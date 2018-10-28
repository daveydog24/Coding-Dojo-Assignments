'''
Checkerboard Assignment
Created By: David Wukelic
Utilizing tab spacing
'''


def Print_Symbol(rows, stars_in_row, symbol):
    while rows > 0:
        printed = ''
        stars = stars_in_row
        if rows % 2 == 0:
            while stars > 0:
                printed += "{} ".format(symbol)
                stars -= 1
        else:
            while stars > 0:
                printed += " {}".format(symbol)
                stars -= 1
        rows -= 1
        print printed

# define how many rows and stars you want 
Print_Symbol(1000, 8, 'I love Kim <3')