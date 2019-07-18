((string, char) => {
	let counter = 0;
	let array  = string.split('');
	for (let i = 0; i < array.length; i++) {
		if (array[i] == char) {
			counter += 1;
			console.log("Found " + counter + " " + char);
			continue;
		} else if (counter == 0) {
			console.log("There is no such character on the string");
			break;
		} 
	}
})("asd", "d");