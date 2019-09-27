let yourName;
do {
	yourName = prompt("What is your name?");
} while (!yourName) {
	console.log(yourName);
}
console.log("Your name is " + yourName)