(function dddGenerator(start=0,end=100) {
	let array = [];
	for (let i = start; i < end; i++) {
		let number1 = (Math.round(Math.random()*9));
		let number2 = (Math.round(Math.random()*9));
		let ddd = number1.toString() + number2.toString();
		array.push(ddd);
		return console.log(array);
	}
})(10, 11);

function genTel(){
	function interval(to){
		return Math.floor(Math.random() * to + 1)
	}
	return ra
}
parseInt(10)