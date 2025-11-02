const path = require("path");
const fm = require("./fileManager");

const helloPath = path.join(__dirname, "Hello World.txt");
const byePath = path.join(__dirname, "Bye World.txt");

const content = fm.readFile(helloPath);
console.log(content);

fm.writeFile(byePath, "Writing to the file");
console.log("Wrote to Bye World.txt");
