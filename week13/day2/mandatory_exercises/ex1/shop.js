let products = [];
try {
  // Attempt to load products and validate
  // eslint-disable-next-line global-require
  const loaded = require('./products');
  if (Array.isArray(loaded)) products = loaded;
  else console.warn('Warning: ./products did not export an array. Using empty list.');
} catch (err) {
  console.warn('Warning: could not load ./products:', err.message);
}

function findProductByName(name) {
  if (!name) return null;
  return products.find(p => p && p.name && p.name.toLowerCase() === name.toLowerCase()) || null;
}

// Example usage (safe)
try {
  console.log('Laptop ->', findProductByName('Laptop'));
  console.log('Coffee Mug ->', findProductByName('Coffee Mug'));
  console.log('Non Existing ->', findProductByName('Non Existing'));
} catch (err) {
  console.error('Error during example run:', err.message);
}

module.exports = { findProductByName };
