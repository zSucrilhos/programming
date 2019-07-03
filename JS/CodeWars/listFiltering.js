function filterList(array) {
    /* Get a array of items and return only the numbers */
    return array.filter( (array) => {
       return typeof array === "number";
    });
};

console.log(filterList(["abc", 1, "def", 2]))

