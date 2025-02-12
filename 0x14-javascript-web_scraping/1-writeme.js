#!/usr/bin/node
// Writes content of a file

const fs = require('fs');
const path = process.argv[2];
const content = process.argv[3];

fs.writeFile(path, content, { encoding: 'utf-8' }, (err) => {
  if (err) {
    console.log(err);
  }
});
