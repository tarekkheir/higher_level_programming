#!/usr/bin/node
// script that prints the number of movies where the character “Wedge Antilles” is present.

const request = require('request');

const url = process.argv[2];
const char = 'https://swapi-api.hbtn.io/api/people/18/';
let nb = 0;

request.get(url, function (error, response, body) {
  if (error) return console.log(error);
  const json = JSON.parse(body).results;
  for (const film of json) {
    for (const character of film.characters) {
      if (character === char) {
        nb++;
      }
    }
  }
  console.log(nb);
});
