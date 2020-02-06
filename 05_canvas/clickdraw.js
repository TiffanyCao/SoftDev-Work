// Trashy Artists -- Tiffany Cao and Yifan Wang
// SoftDev1 pd1
// K05 -- ...and I want to Paint It Better
// 2020-02-06

var c = document.getElementById("slate");
var ctx = c.getContext("2d");
var mode = "rectangle"; // "rectangle" or "dot"
var modeDisplay = document.getElementById("modeDisplay");
var drawingInstructions = [];

document.getElementById("clear").addEventListener("click", () => {
  // e.preventDefault();
  // this method is used to cancel the default action related to an event;
  // for example, if you use this method on a "submit" button, the form will not be submitted.
  // here, clearing the canvas will be prevented if this method is used
  ctx.fillStyle = "#fff";
  ctx.fillRect(0, 0, c.width, c.height);
});

document.getElementById("switch").addEventListener("click", () => {
  if(mode === "rectangle"){
    mode = "dot";
  }else{
    mode = "rectangle";
  }
  modeDisplay.innerHTML = mode;
});

c.addEventListener("click", (e) => {
  var x = e.offsetX;
  var y = e.offsetY;
  // returns coordinates of the mouse pointer relative to the target element, which in this case is the canvas;
  // this lets the user zoom in and out and still be able to draw on the canvas exactly where they clicked the pointer because their coordinates
  // are relative to the canvas and not the page.
  if(mode === "rectangle"){
    ctx.fillStyle = "red";
    ctx.fillRect(x, y, 50, 100);
  }else{
    ctx.beginPath();
    // this method begins a new path by emptying the list of previous paths;
    // it is called every time you want to draw something new that you don't want on the same line or path
    ctx.arc(x, y, 5, 0, 2 * Math.PI);
    ctx.stroke();
    ctx.fillStyle = "blue";
    ctx.fill();
  }
})
