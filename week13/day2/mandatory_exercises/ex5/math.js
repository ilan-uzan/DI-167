function ensureNumber(x) {
  const n = Number(x);
  if (Number.isNaN(n)) throw new TypeError('Expected a number');
  return n;
}

function add(a, b) {
  const x = ensureNumber(a);
  const y = ensureNumber(b);
  return x + y;
}

function multiply(a, b) {
  const x = ensureNumber(a);
  const y = ensureNumber(b);
  return x * y;
}

module.exports = { add, multiply };
