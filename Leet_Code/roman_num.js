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
  const numOfNums = strArr.length - 1;
  // strArr.forEach((letter, index) => {
  //   for (const key in romanObj) {
  //     if(letter === 'I' && strArr[index + 1] === 'V') {
        
  //     }
  //     else if (key === letter) {
  //       result += romanObj[key]
  //     }
  //   }
  // })

  for (let i = 0; i < strArr.length; i++) {
    if (strArr[i] === 'I' &&  strArr[i + 1] === 'V') {
      result += 4;
      strArr.splice(i, 2)
      console.log('strarray', strArr)
    } else { 
      for (const key in romanObj) {
        if (key === str[i]) {
          result += romanObj[key]
        }
      }
    }

  }
  

  return result

}

console.log(romanToInt("XIV"))