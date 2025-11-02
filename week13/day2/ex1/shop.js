const products = require("./products");

function findProductByName(name) {
  return products.find(p => p.name.toLowerCase() === name.toLowerCase()) || null;
}

console.log(findProductByName("Laptop"));
console.log(findProductByName("Coffee Mug"));
console.log(findProductByName("Non Existing"));
