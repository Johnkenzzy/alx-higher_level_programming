#!/usr/bin/node
// Prints all characters of a Star Wars movie in order
const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, { json: true }, (err, resp, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const characters = body.characters;
  printCharactersInOrder(characters, 0);
});

function printCharactersInOrder (characters, index) {
  if (index >= characters.length) return;

  request(characters[index], { json: true }, (err, res, body) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log(body.name);
    printCharactersInOrder(characters, index + 1);
  });
}
