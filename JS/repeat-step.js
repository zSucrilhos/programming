((steps, func) => {
	'use strict'
	for (let i = 0; i < steps; i++) {
		func;
	}
}) (3, console.log('erick\n'));