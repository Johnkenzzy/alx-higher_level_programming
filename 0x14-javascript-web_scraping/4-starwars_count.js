#!/usr/bin/node
// Prints the number of movies where the character "Wedge Antilles" is present

const request = require('request');
const url = process.argv[2];

request({ url, json: true }, (err, resp, body) => {
  if (err) {
    console.error(err);
    return;
  }

  let count = 0;
  const characterId = '18';

  for (const movie of body.results) {
    if (movie.characters.some((charUrl) => charUrl.includes(`/people/${characterId}/`))) {
      count++;
    }
  }

  console.log(count);
});
