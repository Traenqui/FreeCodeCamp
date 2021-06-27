function convertToRoman(num) {
  //lookup "table"
  var lookup = {M:1000,CM:900,D:500,CD:400,C:100,XC:90,L:50,XL:40,X:10,IX:9,V:5,IV:4,I:1};
  var res = '';

  for(let i in lookup) {
    while (num >= lookup[i]) {
      res += i;
      num -= lookup[i];
    }
  }
  return res;
}

convertToRoman(36);
