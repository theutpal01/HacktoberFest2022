//  WEBSITE CRAWLER TASK

console.log("This is Tutorial 13 and Task 1");
// Exercise

// You have to create a variable which is a string containing the text which is a link you are interested in.

// You have to fetch all the links from a given page which contains this text

// codewithharry.com  not needed
// javascript needed

// z = document.links;

// let a = "string";
// let b = "javascript";

// Array.from(z).forEach(function(element){
//     if (String(element).includes(b)){
//         console.log(element); // also we can do console.log(element.href)
//     };
// });


z = document.links;
a = "String"; //Should not include
b = "javascript"; // Should include

Array.from(z).forEach(function (element)
{
	if (String(element).includes(b)) {
		console.log(element);
	}
});