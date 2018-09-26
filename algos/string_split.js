function split(str, separator, limit) {
  let results = [];
  let subStr = '';
  if (separator) {
    if (separator.length == 1){
      for(let i = 0; i < str.length; i++) {
        if(str[i] === separator[0]) {
          if (results.length != limit){
            results.push(subStr);
            subStr = '';
          }
        }
        while (str[i] == separator[0]){ 
          i++;
        }
        subStr += str[i];
      }
    } else {
      for(let i = 0; i < str.length; i++) {
        let tempStr = '';
        for(let j = 0; j < separator.length; j++) {
          tempStr += str[i+j];
        }
        if(tempStr === separator) {
          if (results.length != limit){
            results.push(subStr);
            subStr = '';
            i += separator.length-1;
          }
        }
        subStr += str[i];
      }
    }
    if (results.length != limit){
      results.push(subStr);
    }
  } else {
    results.push(str);
  }
  return results;
}




const url = 'https://www.facebook.com/hi/anotherthing/anotherotherthing';
console.log(split(url, '/hi'));
// console.log(split(url, '/', 10));
// console.log(split(url, '//', 4));


