const { greet } = require('./greeting');
const { colorful } = require('./colorful-message');
const { readData } = require('./read-file');

console.log(greet('Ilan'));
console.log(colorful('This is colorful!'));
console.log('File contents:\n', readData());
