// Mozzarella Ramen - Tiffany Cao, Kiran Vuksanaj
// SoftDev1 pd1
// K29 -- Sequential Progression III: Season of the Witch
// 2019-12-12


var changeHeading = function(e) {
  console.log(e);
  var h = document.getElementById("h");
  if (e.type == 'mouseover'){
    h.innerHTML = e.srcElement.innerHTML
  }else{
    h.innerHTML = "Hello World!";
  };
};


var removeItem = function(e) {
  console.log(e);
  e.srcElement.remove();
};

var lis = document.getElementsByTagName("li");
// console.log(lis);

for (var i = 0; i < lis.length; i++){
  lis[i].addEventListener('mouseover', changeHeading);
  lis[i].addEventListener('mouseout', changeHeading);
  lis[i].addEventListener('click', removeItem);
};

var addItem = function(e) {
  console.log(e);
  var list = document.getElementById("thelist");
  var li = document.createElement("li");
  var node = document.createTextNode("WORD");
  li.appendChild(node);
  li.addEventListener('mouseover', changeHeading);
  li.addEventListener('mouseout', changeHeading);
  li.addEventListener('click', removeItem);
  list.appendChild(li);
};


var add = document.getElementById("b").addEventListener('click', addItem);

var fib = function(n) {
    return ( n < 2 ) ? 1 : fib(n-1) + fib(n-2);
}

var addFib = function(e) {
    console.log(e);
    // get list where elements should be appended
    var fiblist = document.getElementById('fiblist');
    console.log(fiblist.children);
    console.log(fiblist.children.length);
    // generate the nth fibonacci number, where n is the existing length of generated numbers
    var newFibVal = fib(fiblist.children.length);
    // create element and text node to append onto the list, inserting generated number
    var newli = document.createElement('li');
    var node = document.createTextNode(newFibVal);
    // attach node and child to the rest of the DOM
    newli.appendChild(node);
    fiblist.appendChild(newli);
}

var addFib2 = function(e) {
    console.log(e);
    var fiblist = document.getElementById('fiblist');
    var newFibVal;
    if( fiblist.children.length < 2 ) {
	newFibVal = 1;
    }else {
	var children = fiblist.children;
	var ultFib = parseInt(children[children.length-1].innerHTML);
	var penultFib = parseInt(children[children.length-2].innerHTML);
	newFibVal = ultFib + penultFib;
    }
    var newli = document.createElement('li');
    var node = document.createTextNode(newFibVal);
    newli.appendChild(node);
    fiblist.appendChild(newli);
}

var fb = document.getElementById('fb');
fb.addEventListener('click',addFib2);
