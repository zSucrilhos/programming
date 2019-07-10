'use strict'
((number, power) => {
    number = 1000, power = 2;
    let result = 0; array = [];
    for (let i = 0; result <= number; i++) {
        result = i ** power;
        array.push(result);
    }
    console.log(array);
}) ();

