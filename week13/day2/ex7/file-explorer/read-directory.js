const fs = require("fs");
const path = require("path");

const dir = __dirname;
const files = fs.readdirSync(dir);
files.forEach(f => console.log(f));
