let facts = [
	"Boston College (also referred to as BC) is a private Jesuit research university in Chestnut Hill, Massachusetts.",
	"Boston College was founded in 1863 by the Society of Jesus (the Jesuits) to educate Boston's predominantly Irish, Catholic immigrant community.",
	"When it outgrew the limitations of the space, then-president Rev. Thomas I. Gasson, S.J., bought 31 acres of the former Lawrence Farm in Chestnut Hill, Massachusetts, and broke ground in 1909 on a new campus, today fondly known as “the Heights.”",
	"BC began as an undergraduate liberal arts college, but as its aspirations grew, it added graduate programs and professional schools fulfilling its charter as a university.",
	"The university has more than 9,300 full-time undergraduates and nearly 5,000 graduate students.",
	"Boston College athletic teams are known as the Eagles, their colors are maroon and gold, and mascot is Baldwin the Eagle.",
	"In 2017-18, 4,192 degrees were awarded in more than 50 fields of study, through eight schools and colleges.",
	"In 1927, Boston College conferred one earned bachelor’s degree and fifteen Master’s degrees on women through the Extension Division.",
	"The two most popular undergraduate majors are economics (A&S) and finance (CSOM).",
	"The computer science major has seen an increase of nearly 800 percent, growing from just 53 students in 2008 to 420 in 2019",
	"Boston College tied in 38th among national universities and 421st among global universities in U.S. News & World Report's America's Best Colleges 2018 rankings.",
	"In 2014, the undergraduate school of business, the Carroll School of Management, placed 4th in an annual ranking of US undergraduate business schools by Bloomberg Businessweek.",
	"AHANA is the term Boston College uses to refer to persons of African-American, Hispanic, Asian, and Native American descent. The term was coined at Boston College in 1979 by two students, Alfred Feliciano and Valerie Lewis, who objected to the name Office of Minority Programs used by Boston College at the time.",
	"'The Heights' is a nickname given to Boston College. It recalls both BC's lofty aspirations—the college motto is 'Ever to Excel'—and its hilltop location, an area initially designated as 'University Heights'.",
	"On October 18, 2017, hundreds of students walked out of class in a protest against racism and to demand the college officials pay more attention to the school's racial climate.",
	"For the Class of 2023, Boston College received 35,500 applications, of which it admitted 9,500 (27%).",
	"There are over 179,000 alumni in over 120 countries around the world.",
	"BC has the largest alumni association among Catholic universities in the world, consisting of 168,651 members.",
	"Boston College was named one of the 100 most beautiful college campuses by Best College Reviews.",
	"Bapst library was named one of the 25 most beautiful college libraries in the world by Campus Grotto.",
	"Boston College has over 7,000 alumni couples, but if you want to get married at the campus church, St. Ignatius, you should probably put yourself on the waiting list now.",
	"At BC, you can take classes on Disney films in the English Department. Professor Bonnie Rudner also teaches classes on young adult fiction and fairytales.",
	"One of BC’s dining halls, which is currently known for its delicious mac and cheese, was a bar years ago. Vanilla Ice performed there once in the 90’s and the stage collapsed.",
	"During exam weeks, Boston College brings in petting zoos and puppies for students to play with. There is also free coffee in the dining halls and libraries during exams.",
	"BC’s Red Bandana 5K Run and the Red Bandana football game held every October are two traditions that honor BC alum Welles Crowther who passed away in the 9/11 attacks.",
	"Boston College is the most popular college on Instagram. BC’s Gasson Hall, is the third most Instagrammed college building in the country."
];



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