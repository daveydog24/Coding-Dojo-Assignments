import math
if __name__ == '__main__':
    n = int(input())
    sum = 0
    counter = 0
    while n > 0:
        if counter == 0:
            sum += 1
        elif counter == 1:
            sum += math.floor(1.1 * (10**counter))
        elif counter == 2:
            sum += math.floor(1.1 * (10**counter)) + 1
        elif counter == 3:
            sum += math.floor(1.1 * (10**counter)) + 11
        elif counter == 4:
            sum += math.floor(1.1 * (10**counter)) + 111
        elif counter == 5:
            sum += math.floor(1.1 * (10**counter)) + 1111
        elif counter == 6:
            sum += math.floor(1.1 * (10**counter)) + 11111
        elif counter == 7:
            sum += math.floor(1.1 * (10**counter)) + 111111
        elif counter == 8:
            sum += math.floor(1.1 * (10**counter)) + 1111111
        elif counter == 9:
            sum += math.floor(1.1 * (10**counter)) + 11111111
        elif counter == 10:
            sum += math.floor(1.1 * (10**counter)) + 111111111
        elif counter == 11:
            sum += math.floor(1.1 * (10**counter)) + 1111111111
        else:
            sum += math.floor(1.1 * (10**counter)) + 11111111111
        counter += 1
        n -= 1                
    print (sum)