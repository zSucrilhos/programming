function range(start=0, end=10, step=1) {
	/* This function gets an interval and returns an array of numbers */
	// Checking if the arguments are integers
	if (typeof start != "number" && typeof end != "number") {
		throw "You must pass only integers as arguments.";
	} else {
		// Doing the real stuff
		let array = [];
		if (start < end) { // Incrementing
			for (let i = start; i < end+step; i += step) {
				array.push(i);
			}
			return array; // We need something to work with

		} else if (start > end) { // Decrementing
			for (let i = start; i >= end-1; i -= step) {
				array.push(i);
			}
			return array; // We need something to work with²
		}
	}
}

function sum(array) {
	/* This function gets an array as argument and returns the sum of all 
	of its items */
	let actualSum = 0;
	for (let i = 0; i < array.length; i++) {
		actualSum += array[i];
	}
	return console.log(actualSum);
}

sum(range(0,1450,9));