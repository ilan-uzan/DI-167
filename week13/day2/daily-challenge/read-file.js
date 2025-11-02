const fs = require('fs');
const path = require('path');

function readData() {
  const p = path.resolve(__dirname, 'files', 'file-data.txt');
  return fs.readFileSync(p, 'utf8');
}

module.exports = { readData };
