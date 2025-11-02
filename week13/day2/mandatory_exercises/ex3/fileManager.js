const fs = require('fs');
const path = require('path');

function resolveSafe(baseDir, userPath) {
  const resolved = path.resolve(baseDir, userPath);
  if (!resolved.startsWith(path.resolve(baseDir))) {
    throw new Error('Invalid path');
  }
  return resolved;
}

function readFile(filePath) {
  try {
    const resolved = path.resolve(filePath);
    return fs.readFileSync(resolved, 'utf8');
  } catch (err) {
    throw new Error(`readFile failed: ${err.message}`);
  }
}

function writeFile(filePath, content) {
  try {
    const resolved = path.resolve(filePath);
    fs.writeFileSync(resolved, content, 'utf8');
  } catch (err) {
    throw new Error(`writeFile failed: ${err.message}`);
  }
}

// Async versions
async function readFileAsync(baseDir, userPath) {
  try {
    const resolved = resolveSafe(baseDir, userPath);
    return await fs.promises.readFile(resolved, 'utf8');
  } catch (err) {
    throw new Error(`readFileAsync failed: ${err.message}`);
  }
}

async function writeFileAsync(baseDir, userPath, content) {
  try {
    const resolved = resolveSafe(baseDir, userPath);
    await fs.promises.writeFile(resolved, content, 'utf8');
  } catch (err) {
    throw new Error(`writeFileAsync failed: ${err.message}`);
  }
}

module.exports = { readFile, writeFile, readFileAsync, writeFileAsync };
