const chalk = require('chalk');

function colorful(msg) {
  return chalk.cyan(msg);
}

module.exports = { colorful };
