#!/usr/bin/node
// Gets the contents of a webpage and stores it in a file.
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filePath = process.argv[3];

request(url, (err, resp, body) => {
  if (err) {
    console.error(err);
    return;
  }

  fs.writeFile(filePath, body, 'utf-8', (err) => {
    if (err) {
      console.error(err);
    }
  });
});
