// Team Club Penguinners
// Yaru && Tiff
// SoftDev1 pd1
// K#13: Ask Circles [Change || Die]
// 2020-03-30

var pic = document.getElementById("vimage");
//initalized variables
var currentX = null;
var currentY = null;
var changed = false;

//Event listener for svg, drawing new circle
pic.addEventListener("click", function(e){
  // console.log(e.target);

  // var d = document.getElementsByTagNameNS("http://www.w3.org/2000/svg", "circle");
  // var count = 0;
  // for (i = 0; i < d.length; i++){
  //   var s = d[i];
  //   if(e.offsetX == s.getAttribute("cx") && e.offsetY == s.getAttribute("cy")){
  //     console.log("stop");
  //     count++;
  //     break;
  //   }
  // };
  //
  // if (count == 0) {

  if(e.target == pic){ //if mouse is on svg blank canvas
    var c = document.createElementNS("http://www.w3.org/2000/svg", "circle"); //creating a new circle

    c.setAttribute("r", "10");
    c.setAttribute("fill", "blue");
    c.setAttribute("stroke", "blue");

    c.setAttribute("cx", e.offsetX); //setting circle's position
    c.setAttribute("cy", e.offsetY);

    pic.appendChild(c);
  };
});

// pic.addEventListener("click", function(e){
//   if(e.target != pic && e.target.getAttribute("fill") == "turquoise"){
//     var newX = Math.floor(Math.random() * 501);
//     var newY = Math.floor(Math.random() * 501);
//     e.target.setAttribute("cx", newX);
//     e.target.setAttribute("cy", newY);
//     e.target.setAttribute("fill", "blue");
//     e.target.setAttribute("stroke", "blue");
//   };
// });


// Event listener for changing circle color and removing circle
pic.addEventListener("click", function(e){
  var d = document.getElementsByTagNameNS("http://www.w3.org/2000/svg", "circle");
  // console.log("1");
  // console.log(d);
  if(e.target != pic && e.target.getAttribute("fill") == "blue"){ //if mouse is on a blue circle
    e.target.setAttribute("fill", "turquoise");
    e.target.setAttribute("stroke", "turquoise");
  }else if(e.target != pic && e.target.getAttribute("fill") == "turquoise"){ //if mouse is on a turquoise circle
    var newX = Math.floor(Math.random() * 501);
    var newY = Math.floor(Math.random() * 501);
    e.target.remove(); //remove old circle
    var c = document.createElementNS("http://www.w3.org/2000/svg", "circle"); //creating a new circle

    c.setAttribute("r", "10");
    c.setAttribute("fill", "blue");
    c.setAttribute("stroke", "blue");

    c.setAttribute("cx", newX); //setting circle's position to random coordinates
    c.setAttribute("cy", newY);

    pic.appendChild(c);
    // console.log("2");
    // console.log(d);
  };
});


//Event listener for clear button
document.getElementById('clear').addEventListener("click", function(e){
  firstClick = true; //resets firstClick to true
  console.log("clear");

  var fc = pic.firstChild;
  while(fc) {
    console.log("removing " + fc + "...");
    pic.removeChild(fc);
    fc = pic.firstChild;
  }

});
