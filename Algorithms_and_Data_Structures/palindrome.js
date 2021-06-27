function palindrome(str) {
  //clean up input
  var regExp = /[\W_]/gi;
  var cleanStr = str.toLowerCase().replace(regExp, "");

  //build reverse String
  var reverseStr = cleanStr.split("").reverse().join("");

  //String compare
  return reverseStr === cleanStr;
}

palindrome("eye");
