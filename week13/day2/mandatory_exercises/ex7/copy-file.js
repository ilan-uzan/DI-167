const fs = require('fs');
const path = require('path');

const source = path.resolve(__dirname, '../file-explorer/source.txt');
const dest = path.resolve(__dirname, 'destination.txt');

fs.copyFileSync(source, dest);
console.log('File copied to', dest);
