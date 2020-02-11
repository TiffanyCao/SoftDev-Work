// Trashy Artists -- Tiffany Cao and Yifan Wang
// SoftDev1 pd1
// K06 -- Dot Dot Dot
// 2020-02-11

var c = document.getElementById("slate");
var ctx = c.getContext("2d");
drawingPath = []; //stores previous position

document.getElementById("clear").addEventListener("click", () => {
  ctx.fillStyle = "#fff";
  ctx.fillRect(0, 0, c.width, c.height);
});


c.addEventListener("click", (e) => {
  var x = e.offsetX;
  var y = e.offsetY;
  if (drawingPath.length == 0){ //store the first point
    drawingPath.push([x,y]);
  }
  ctx.beginPath();
  // drawing the dot first
  ctx.arc(x, y, 5, 0, 2 * Math.PI);
  ctx.fillStyle = "blue";
  ctx.fill();
  ctx.moveTo(drawingPath[0][0],drawingPath[0][1]); // moving to the dot position before the current position
  ctx.lineTo(x,y); // drawing a line from previous dot to current dot
  ctx.stroke();
  drawingPath = []; // clears the array
  drawingPath.push([x,y]); //stores current position as the "old" position in preparation for the next dot
})


document.getElementById("clear").addEventListener("click", () => {
  drawingPath = []; //clears the array for a fresh start
  ctx.fillStyle = "#fff";
  ctx.fillRect(0, 0, c.width, c.height);
});
