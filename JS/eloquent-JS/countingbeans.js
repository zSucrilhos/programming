((string, char) => {
	let counter = 0;
	let array  = string.split('');
	for (let i = 0; i < array.length; i++) {
		if (array[i] == char) {
			counter += 1;
		}
	}
	(counter > 1) ? console.log("Found " + counter + " " + char + "'s") : console.log("Found " + counter + " " + char);
	(counter === 0) ? console.log("There is no such character on the string") : null;
	return counter;

})("In other words, as we start the program, we start in the global execution context.\
Some variables are declared within the global execution context. We call these global\
variables. When the program calls a function, what happens? A few steps:JavaScript\
creates a new execution context, a local execution context\
That local execution context will have its own set of variables, these variables\
will be local to that execution context.\
The new execution context is thrown onto the execution stack. T", "t");