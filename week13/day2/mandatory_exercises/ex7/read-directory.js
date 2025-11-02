const fs = require('fs');
const path = require('path');

const dir = path.resolve(__dirname);
const files = fs.readdirSync(dir);
console.log('Files in folder:', files);
