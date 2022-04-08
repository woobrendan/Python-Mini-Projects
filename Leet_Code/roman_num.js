const romanToInt = (str) => {
  let result = 0;
  const romanObj = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
  }

  const strArr = str.split('');
  for (let i = 0; i < strArr.length; i++) {

    if (strArr[i] === 'I' &&  strArr[i + 1] === 'V') {
      result += 4;
      strArr.splice(i, 2);
    } 
    else if (strArr[i] === 'I' &&  strArr[i + 1] === 'X') {
      result += 9;
      strArr.splice(i, 2);
    } 
    else if (strArr[i] === 'X' &&  strArr[i + 1] === 'L') {
      result += 40;
      strArr.splice(i, 2);
      i--;
    }
    else if (strArr[i] === 'X' &&  strArr[i + 1] === 'C') {
      result += 90;
      strArr.splice(i, 2);
      i--;
    }
    else if (strArr[i] === 'C' &&  strArr[i + 1] === 'D') {
      result += 400;
      strArr.splice(i, 2);
      i--;
    }
    else if (strArr[i] === 'C' &&  strArr[i + 1] === 'M') {
      result += 900;
      strArr.splice(i, 2);
      i--;
    }
  
    else { 
      for (const key in romanObj) {
        if (key === str[i]) {
          result += romanObj[key];
        }
      }
    }
  }

//  strArr.forEach((letter, index) => { 

//     if (letter === 'I' &&  strArr[index + 1] === 'V') {
//       result += 4;
//       strArr.splice(index , 2);
//     } 
//     else if (letter === 'I' &&  strArr[index  + 1] === 'X') {
//       result += 9;
//       strArr.splice(index , 2);
//     } 
//     else if (letter === 'X' &&  strArr[index  + 1] === 'L') {
//       result += 40;
//       strArr.splice(index , 2);
//       index - 1;
//     }
//     else if (letter === 'X' &&  strArr[index  + 1] === 'C') {
//       result += 90;
//       strArr.splice(index , 2);
//       index - 1;
//     }
//     else if (letter === 'C' &&  strArr[index  + 1] === 'D') {
//       result += 400;
//       strArr.splice(index , 2);
//       index - 1;
//     }
//     else if (letter === 'C' &&  strArr[index  + 1] === 'M') {
//       result += 900;
//       strArr.splice(index , 2);
//       index - 1;
//     }
  
//     else { 
//       for (const key in romanObj) {
//         if (key === letter) {
//           result += romanObj[key];
//         }
//       }
//     }
//   })


  return result;
}
console.log(romanToInt("MDCCXCVII"))