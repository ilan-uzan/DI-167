const fs = require("fs");
const path = require("path");

const src = path.join(__dirname, "source.txt");
const dest = path.join(__dirname, "destination.txt");

const content = fs.readFileSync(src, "utf8");
fs.writeFileSync(dest, content, "utf8");
console.log("Copied source.txt to destination.txt");
