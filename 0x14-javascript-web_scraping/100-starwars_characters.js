#!/usr/bin/node
// Prints all characters of a Star Wars movie
const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, { json: true }, (err, resp, body) => {
  if (err) {
    console.error(err);
    return;
  }

  if (resp.statusCode !== 200) {
    console.error('Error: Movie not found');
    return;
  }

  const characters = body.characters;
  if (!characters || characters.length === 0) {
    console.log('No characters found');
    return;
  }

  characters.forEach((url) => {
    request(url, { json: true }, (err, resp, charBody) => {
      if (err) {
        console.error(err);
        return;
      }
      console.log(charBody.name);
    });
  });
});
