const fs = require('fs').promises;
const path = require('path');

async function readData() {
  try {
    const p = path.resolve(__dirname, 'files', 'file-data.txt');
    return await fs.readFile(p, 'utf8');
  } catch (err) {
    throw new Error(`Failed to read data file: ${err.message}`);
  }
}

module.exports = { readData };
