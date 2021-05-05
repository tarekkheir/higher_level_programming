#!/usr/bin/node
// script that prints all characters of a Star Wars movie

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/'.concat(process.argv[2]);

request.get(url, function (error, response, body) {
  if (error) return console.log(error);
  const characters = JSON.parse(body).characters;
  for (const character of characters) {
    request.get(character, function (error, response, body) {
      if (error) return console.log(error);
      const c = JSON.parse(body);
      console.log(c.name);
    });
  }
});
