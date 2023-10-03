function clearDisplay() {
    document.getElementById("result").value = ""; // Clear the input field
}
var cont=document.querySelector(".container");
var c=document.querySelector("#cursor");

cont.addEventListener("mousemove",function(dets){
    c.style.left=dets.x+"px";
    c.style.top=dets.y+"px";
})