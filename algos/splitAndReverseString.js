



function reverseString(s) {
    let newString = '';
    try {
        newString = s.split('');
        console.log(newString);
        newString.reverse();
        newString = newString.join('');
        console.log(newString);
    }
    catch (error) {
        console.log(error.message);
        console.log(String(s))
    }
}

let string = 'david is about to kill this interview';
reverseString(string);