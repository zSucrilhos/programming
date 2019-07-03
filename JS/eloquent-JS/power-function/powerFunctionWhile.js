((number, power) => {
    number = 1000, power = 2;
    let i = 0, result = 0, array = [];
    while (result <= number) {
        i++;
        result = i ** power;
        array.push(result);
    } 
    console.log(array)
}) ();

