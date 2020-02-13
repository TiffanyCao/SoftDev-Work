// Greyducks Forever -- Tiffany Cao & Yaru Luo
// SoftDev1 pd1
// K07 -- They lock us in the tower whenever we get caught
// 2020-02-12

var c = document.getElementById("slate");
var ctx = c.getContext("2d");
var id = 0;
var progress = 0;
var shrink = false;

document.getElementById("start").addEventListener("click", () => {
  if(id == 0) id = window.requestAnimationFrame(step);
})

document.getElementById("stop").addEventListener("click", () => {
  window.cancelAnimationFrame(id);
  id = 0;
})

function step(){
  if(!shrink){ //expanding
    progress += 1;
    if(progress >= c.width/2) shrink = true; //if the radius exceeds the canvas screen
  }else{ //shrinking
    progress -= 1;
    if(progress <= 0){ //if the radius goes below zero
      shrink = false;
      progress = 0; //starting the cycle over again
    }
  }
  ctx.beginPath();
  ctx.clearRect(0, 0, c.width, c.height); //clearing the screen for the shrinking
  //filling the circle
  ctx.arc(c.width/2, c.height/2, progress, 0, 2 * Math.PI);
  ctx.fillStyle = "lightblue";
  ctx.fill();
  ctx.stroke();
  if(id != 0) window.requestAnimationFrame(step);
}
