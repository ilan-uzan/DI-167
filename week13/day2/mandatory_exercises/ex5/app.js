const { add, multiply } = require('./math');
const _ = require('lodash');

console.log('Sum using add:', add(2,3));
console.log('Product using multiply:', multiply(4,5));
console.log('Chunk example with lodash:', _.chunk([1,2,3,4], 2));
