'''
Compare List Assignment  
Created By: David Wukelic
Utilizing tab spacing

Assignment Info
    You have a record of students. Each record contains the student's name, 
    and their percent marks in Maths, Physics and Chemistry. The marks can be 
    floating values. The user enters some integer followed by the names and marks 
    for students. You are required to save the record in a dictionary data type. 
    The user then enters a student's name. Output the average percentage marks 
    obtained by that student, correct to two decimal places.

Input Format
    The first line contains the integer , the number of students. 
    The next lines contains the name and marks obtained by that student 
    separated by a space. The final line contains the name of a particular
    student previously listed.

Output Format  
    Print one line: The average of the marks obtained by the particular 
    student correct to 2 decimal places.

Sample Input 0
    3
    Krishna 67 68 69
    Arjun 70 98 63
    Malika 52 56 60
    Malika

Sample Output 0
    56.00

Explanation 0
    Marks for Malika are whose average is

Sample Input 1
    2
    Harsh 25 26.5 28
    Anurag 26 28 30
    Harsh

Sample Output 1
    26.50

'''
a = ['Krishna 67 68 69','Arjun 70 98 63','Malika 52 56 60', 'Malika']
b = ['Harsh 25 26.5 28', 'Anurag 26 28 30', 'Harsh']

def find_percentage(test_list):
    
    for x in enumerate(test_list):
        line = x[1].split()
        name = line[0]

    # makes sure that the last entry doesnt actually run numbers it just stuff only on the line we want. AKA minimal data
        if name == test_list[-1] and (x[0] != (len(test_list)-1)):
            scores = line[1:]
            scores = list(map(float, scores))
            total = 0
            count = 0
            for i in scores:
                total += i
                count += 1
            average = (total / count)
            
    return average

