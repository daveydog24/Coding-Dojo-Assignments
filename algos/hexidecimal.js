/* Write for me a function that does the following:

Input: 3 separate Integer values
Output:  a 7-character length string representing the hexadecimal value of the input integers in the format of “#xxxxxx”

Example Input:
(9,208,194)
#09D0C2

Notes: 
09 / 16 = 0 R 9
208 / 16 = 13 R 0
194 / 16 = 12 R 2 

0=0, 1=1, 10-a, 11-b, 12-c, 13-d, 14-e, 15-f

*/

function createHexadecimal(int1, int2, int3) {
	return '#' + getValue(int1) + getValue(int2) + getValue (int3);
}

function getValue(int) {
	return changeToHex(Math.floor(int / 16)) + changeToHex(int % 16);
}  

function changeToHex(int){
    let letters = {
        '0': '0', 
        '1': '1', 
        '2': '2', 
        '3': '3', 
        '4': '4', 
        '5': '5', 
        '6': '6', 
        '7': '7', 
        '8': '8', 
        '9': '9',
        '10': 'A', 
        '11': 'B', 
        '12': 'C', 
        '13': 'D', 
        '14': 'E', 
        '15':'F'
    };
    let hexidecimal = letters[int];
	return hexidecimal;
}

console.log(createHexadecimal(09,208,194))
console.log(createHexadecimal(132,83,83))