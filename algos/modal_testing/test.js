// function reverseArray(arr){ 
//     for(var i=0; i<arr.length/2; i++) { 
//         temp = arr[arr.length-i-1]; 
//         arr[arr.length-i-1] = arr[i]; 
//         arr[i] = temp; 
//     } 
//     return arr; 
// } 
// b = reverseArray([1,2,3]); 
// console.log('b is', b); 
    
// describe("reverseArray", function() { 
//     it("should return [5,3,1] when [1,3,5] is passed", function() { 
//         expect(reverseArray([1,3,5])).toEqual([5,3,1]); 
//     }); 
//     it("should return [2,4,8,1] when [1,8,4,2] is passed", function() { 
//         expect(reverseArray([2,4,8,1])).toEqual([1,8,4,2]); 
//     }); 
// });

var dojo = {};                                 // creates an empty object
dojo = {
  name: 'Coding Dojo',                         // property can store a string
  number_of_students: 25,                      // property can store a number
  instructors: ['Andrew', 'Michael', 'Jay'],   // property can store arrays
  location: {                                  // property can even store another object!
    city: 'San Jose',
    state: 'CA',
    zipcode: 95112
  }
}                                              // access object properties with dot (.) notation
// console.log(dojo.name, dojo.number_of_students, dojo.instructors, dojo.location);
// console.log(dojo["name"]);                     // or bracket [] notation (note: specify key in quotes)

// for (key,value of dojo.location){
//     console.log(key, value);
// }

let test = {a: 1, b: 2, c: 3};

for (let [key, value] of Object.entries(test)) {
    console.log(key, value);
}
