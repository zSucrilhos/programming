function calculatePower(number, power) {
    `This function calculates all the powers of the numbers until >number is
    reached`
    let k = 0, j = 0;
    while (k <= number) {
        console.log(j);
        j = k ** power;
        k++;
    }
}

calculatePower(1000, 2);
