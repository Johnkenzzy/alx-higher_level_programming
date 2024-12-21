#!/usr/bin/node

const fs = require('fs');
const fA = process.argv[2];
const fB = process.argv[3];
const fC = process.argv[4];

try {
  const dataA = fs.readFileSync(fA, 'utf-8');
  const dataB = fs.readFileSync(fB, 'utf-8');

  fs.writeFileSync(fC, dataA + dataB, 'utf-8');
} catch (err) {
  console.error('Error:', err.message);
}
