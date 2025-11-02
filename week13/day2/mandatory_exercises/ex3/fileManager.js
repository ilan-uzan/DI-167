const fs = require("fs");
const path = require("path");

function readFile(filePath) {
  const resolved = path.resolve(filePath);
  return fs.readFileSync(resolved, "utf8");
}

function writeFile(filePath, content) {
  const resolved = path.resolve(filePath);
  fs.writeFileSync(resolved, content, "utf8");
}

module.exports = { readFile, writeFile };
