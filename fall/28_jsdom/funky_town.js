//Jackie Lin and Tiffany Cao (Team Couch Potatoes)
//SoftDev1 pd1
//K#28 -- Sequential Progression II: Electric Boogaloo
//2019-12-11

// console.log("this is a test");

//function for factorial
var factorial = function(n) {
  if (n < 2) return 1;
  return factorial(n - 1) * n;
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

var test = ["Tiffany", "Jackie", "Tina", "Wooooo", "Bob", "Joe", "Esteban"]

//function for selecting random student from a given list
var randomStudent = function() {
  var index = parseInt(Math.random() * test.length);
  return test[index];
};


// https://www.w3schools.com/jsref/met_element_addeventlistener.asp
var fact = document.getElementById("fact");
fact.addEventListener("click", function(){
  console.log(factorial(5));
  document.getElementById("fact").innerHTML = factorial(5);
});


var fibo = document.getElementById("fib");
fibo.addEventListener("click", function(){
  console.log(fib(5));
  document.getElementById("fib").innerHTML = fib(5);
});


var denom = document.getElementById("gcd");
denom.addEventListener("click", function(){
  console.log(gcd(28, 84));
  document.getElementById("gcd").innerHTML = gcd(28, 84);
});


var student = document.getElementById("randomStudent");
student.addEventListener("click", function(){
  var random = randomStudent()
  console.log(random)
  document.getElementById("randomStudent").innerHTML = random;
});
