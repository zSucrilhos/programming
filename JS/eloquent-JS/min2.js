function min(nums) {
	'use strict'
	let argsArray = [];
	for (let i = 0; i < nums.length; i++) {
		argsArray.push(nums);
	}
	return console.log(Math.min(argsArray));
}

min([1,2,3,5,6,7,8,9,0]);
