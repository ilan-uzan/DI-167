const _ = require("lodash");
const math = require("./math");

const numbers = [1, 2, 3, 4];
console.log("Sum using lodash:", _.sum(numbers));
console.log("Add using custom module:", math.add(10, 5));
console.log("Multiply using custom module:", math.multiply(6, 7));
