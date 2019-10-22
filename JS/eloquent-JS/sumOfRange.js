((array) => {
    if (typeof array != "object") {
        console.log("Argument is not an array");
        return 1;
    }

    for (let i = 0; i < array.length; i++) {
        let r1 = array[i] + array[i+1];
        let r2 = r1 + array[i];
        console.log(r2);
    }
})([1,2,4]);
