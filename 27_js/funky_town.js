// console.log("this is a test");

//function for factorial
var fact = function(n) {
  if (n < 2) return 1;
  return fact(n - 1) * n;
};

//function for fibonacci
var fib = function(n) {
  if (n <= 0) return 0;
  if (n == 1) return 1;
  return fib(n - 1) + fib(n - 2);
};

//function for GCD
var gcd = function(a, b){
  if (b > a) return gcd(b, a);
  if (a % b == 0) return b;
  return gcd(b, a % b);
};

var test = ["Tiffany", "Jackie", "Tina", "Wooooo"]

//function for selecting random student from a given list
var randomStudent = function(list) {
  var index = parseInt(Math.random() * list.length);
  return list[index];
};
