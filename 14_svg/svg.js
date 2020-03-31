// Team Confetti
// Tiffany Cao && Peihua Huang
// SoftDev1 pd1
// K#14: Ask Circles [Change || Die] While Moving
// 2020-03-31

var pic = document.getElementById("vimage");
var id = 0;
var btn_move = document.getElementById("move");
var btn_xtra = document.getElementById("xtra");

//Function for drawing new circles
pic.addEventListener("click", function(e){
  if(e.target == pic){ //if mouse is on svg blank canvas
    var c = document.createElementNS("http://www.w3.org/2000/svg", "circle"); //creating a new circle

    c.setAttribute("r", "15");
    c.setAttribute("fill", "blue");
    // c.setAttribute("stroke", "blue");

    c.setAttribute("cx", e.offsetX); //setting circle's position
    c.setAttribute("cy", e.offsetY);

    c.setAttribute("inc_x", 1); //setting up initial moving increments
    c.setAttribute("inc_y", 1);

    c.addEventListener("click", change); //add change color functionality

    pic.appendChild(c);
  };
});

//Function to change color from blue to cyan and removing/creating circles
var change = function(e){
  if(e.target != pic && e.target.getAttribute("fill") != "cyan"){ //if mouse is on a blue circle
    e.target.setAttribute("fill", "cyan");
  }
  else{
    var newX = Math.floor(Math.random() * 501);
    var newY = Math.floor(Math.random() * 501);
    e.target.remove(); //remove old circle
    var c = document.createElementNS("http://www.w3.org/2000/svg", "circle"); //creating a new circle

    c.setAttribute("r", "15");
    c.setAttribute("fill", "blue");
    // c.setAttribute("stroke", "blue");

    c.setAttribute("cx", newX); //setting circle's position
    c.setAttribute("cy", newY);

    c.setAttribute("inc_x", 1); //setting up initial moving increments
    c.setAttribute("inc_y", 1);

    c.addEventListener("click", change); //add change color functionality

    pic.appendChild(c);
  };
};

//Function to move circles in DVD fashion
var move = function(e){
  var d = document.getElementsByTagNameNS("http://www.w3.org/2000/svg", "circle"); //get all the circles
  for (var i = 0; i < d.length; i++){
    console.log(d[i]);
    var dot = d[i];
    var x = parseInt(dot.getAttribute("cx")); //retrieve and parse x and y values to int
    var y = parseInt(dot.getAttribute("cy"));
    var inc_x = parseInt(dot.getAttribute("inc_x")); //retrieve parse increment values to int
    var inc_y = parseInt(dot.getAttribute("inc_y"));
    if (x > pic.getAttribute("width") - 15){ //change increment values according to direction
      dot.setAttribute("inc_x", -1);
    }
    else if (x < 15){
      dot.setAttribute("inc_x", 1);
    }
    if (y > pic.getAttribute("height") - 15){
      dot.setAttribute("inc_y", -1);
    }
    else if (y < 15){
      dot.setAttribute("inc_y", 1);
    }
    x += inc_x; //add new increment
    y += inc_y;
    dot.setAttribute("cx", x); //move to new positio
    dot.setAttribute("cy", y);
  }
  if (id != 0){ //animation
    id = window.requestAnimationFrame(move);
  }
};

//Extra function for changing circle color
var xtra = function(e){
  console.log("here");
  var d = document.getElementsByTagNameNS("http://www.w3.org/2000/svg", "circle"); //get all the circles
  for (var i = 0; i < d.length; i++){
    var dot = d[i];
    console.log(dot);
    dot.setAttribute("fill", '#'+Math.floor(Math.random()*16777215).toString(16)); //change their color
  }
};



//Event listener for movement animation
btn_move.addEventListener("click", function(e){
    window.cancelAnimationFrame(id);
    id = window.requestAnimationFrame(move);
  }
);

//Event listener for xtra
btn_xtra.addEventListener("click", xtra);

//Event listener for clear button
document.getElementById("clear").addEventListener("click", function(e){
  console.log("clear");
  window.cancelAnimationFrame(id); //stop animation
  id = 0;

  var fc = pic.firstChild; //remove all circles
  while(fc) {
    console.log("removing " + fc + "...");
    pic.removeChild(fc);
    fc = pic.firstChild;
  }
});
