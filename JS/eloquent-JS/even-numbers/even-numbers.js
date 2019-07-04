function logNumbers(number, interval) {
    `This takes every number that is less than the number set and logs it out`
    let counter = 0;
    
    while (counter <= number) {
        console.log(counter);
        counter += interval;
    }
}

logNumbers(30, 5);

