(function isEven(number = -1) {
		if (Math.sign(number) == 1) {
			return (number % 2 == 0) ? console.log("Number is even") : console.log("Number is odd")
		} else {
			console.log("Number is negative");
			return 1;
		}
})();
