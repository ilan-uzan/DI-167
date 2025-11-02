const chalk = require('chalk');

function greet(name) {
  if (!name) throw new Error('Name is required');
  return `Hello, ${name}!`;
}

if (require.main === module) {
  const name = process.argv[2] || 'World';
  try {
    console.log(chalk.green(greet(name)));
  } catch (err) {
    console.error(chalk.red(err.message));
    process.exit(1);
  }
}

module.exports = { greet };

