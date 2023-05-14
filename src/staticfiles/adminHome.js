let facts = [];



document.querySelector("#filter-button").onclick = function(){
	let randomFact = facts[Math.floor(Math.random()*facts.length)];

	// CREATE NEW PARAGRAPH-TAG
	let paragraph = document.createElement("p");
	paragraph.className = "generated-content";

	// CREATE PARAGRAPH CONTENT
	let node = document.createTextNode(randomFact);

	// ADD PARAGRAPH CONTENT TO TAG
	paragraph.appendChild(node);

	// ADD PARAGRAPH TO DIV-CONTAINER WITH ID "content"
	let element = document.querySelector("#content");
	element.appendChild(paragraph);
  
  
	this.blur(); // lose focus
  
}

function openCity(evt, cityName) {
  // Declare all variables
  var i, tabcontent, tablinks;

  // Get all elements with class="tabcontent" and hide them
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }

  // Get all elements with class="tablinks" and remove the class "active"
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }

  // Show the current tab, and add an "active" class to the button that opened the tab
  document.getElementById(cityName).style.display = "block";
  evt.currentTarget.className += " active";
}
document.getElementById("defaultOpen").click();