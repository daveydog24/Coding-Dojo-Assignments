Write for me a function that does the following:

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

Function createHexadecimal(int1, int2, int3) {
	//validations
	Let finalString = ‘’
	
	Return getValue(int1) + getValue(int2) + getValue (int3)
}

Function getValue(int)  //9; 208; 194 
{
	Return mutate(actualInt(int)) + mutate(intRemainder(int));
}  /”09” ; D0; C2

function mutate(int){
Letters = {0: 0, 1: 1, 10: a, 11: b, 12: c, 13: d, 14: e, 15-f}
hexidecimal  = Letters[int]

	Return hexidecimal 
}

Function actualInt(int){
	Return (math.floor(int/16));
}
