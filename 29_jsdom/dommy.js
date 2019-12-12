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

for (var i = 0; i < lis.length; i++){
  lis[i].addEventListener('mouseover', changeHeading);
  lis[i].addEventListener('mouseout', changeHeading);
  lis[i].addEventListener('click', removeItem);
};

var addItem = function(e) {
  var list = document.getElementsByID("ol")
}
