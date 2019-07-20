let i = 0;
(function consolelog(number = 100, interval = 1) {
	if (i <= number) {
		console.log(i);
		i += interval;
		consolelog();
	}
}) ();