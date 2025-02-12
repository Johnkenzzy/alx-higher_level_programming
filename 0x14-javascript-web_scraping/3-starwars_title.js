#!/usr/bin/node
// Prints the title of Star Wars movie of a given episode

const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request.get({ url, json: true }, (err, resp, body) => {
  if (err) {
    console.log(err);
  } else {
    if (body && body.title) {
      console.log(body.title);
    }
  }
});
