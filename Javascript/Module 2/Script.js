var myImage = document.getElementsByClassName("intro");
console.log(myImage);

var para = document.getElementsByClassName("intro");
var content = para.innerHTML;
console.log(content);

var myLinks = document.getElementsByTagName("a");

var firstLink = myLinks[0].getAttfibute("href");
console.log(firstLink);

//console.log(myLinks.length);
//document.getElementById("mainTitle").innerHTML  = "This is why you should travel with us!"

//var align = mainTitle.getAttribute("align")
//console.log(align);

document.getElementById("Customer1").setAttribute("align", "left");
document.getElementById("China").setAttribute("src", "images/japan.jpg");
document.getElementById("China").setAttribute("alt", "picture of china");