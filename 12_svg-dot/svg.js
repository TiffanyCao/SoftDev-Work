// Team Club Penguinners
// Yaru && Tiff
// SoftDev1 pd1
// K#12: Connect the Dots
// 2020-03-30

var pic = document.getElementById("vimage");
//initalized variables
var oldX = null;
var oldY = null;
var firstClick = true;

//Event listener for svg
pic.addEventListener("click", function(e){
  var c = document.createElementNS("http://www.w3.org/2000/svg", "circle"); //creating a new circle

  c.setAttribute("r", "5");
  c.setAttribute("fill", "orange");
  c.setAttribute("stroke", "black");

  console.log("click");
  console.log(e.offsetX);
  console.log(e.offsetY);
  c.setAttribute("cx", e.offsetX); //setting circle's position
  c.setAttribute("cy", e.offsetY);

  pic.appendChild(c);

  var l = document.createElementNS("http://www.w3.org/2000/svg", "line");
  if(firstClick){ //checking if this is the first circle
	   firstClick = false;
	   console.log(firstClick);
  }
  else{ //if not the first circle, draw a line from oldX and oldY to current position
  	l.setAttribute("x1", oldX);
  	l.setAttribute("y1", oldY);
  	l.setAttribute("x2", e.offsetX);
  	l.setAttribute("y2", e.offsetY);
  	l.setAttribute("stroke", "black");
  	pic.appendChild(l);
  }

  oldX = e.offsetX; //sets current circle's position to become the oldX and oldY values
  oldY = e.offsetY;

});

//Event listener for clear button
document.getElementById('clear').addEventListener("click", function(e){
  firstClick = true; //resets firstClick to true
  console.log("clear");

  var r = document.createElementNS("http://www.w3.org/2000/svg", "rect"); //clear svg by drawing a rectangle over it
  r.setAttribute("x", 0);
  r.setAttribute("y", 0);
  r.setAttribute("width", 500);
  r.setAttribute("height", 500);
  r.setAttribute("fill", "white"); //set color to white for clearing

  pic.appendChild(r);

});
