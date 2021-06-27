function rot13(str) {
  //input and output as mapping refrences
  var input  = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz';
  var output = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm';

  var index = x => input.indexOf(x);
  var translate = x => index(x) > - 1 ? output[index(x)] : x;

  return str.split('').map(translate).join('');
}

rot13("SERR PBQR PNZC");
