#!/usr/bin/node
// script that prints the title of a Star Wars movie where the episode number matches a given integer.

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/'.concat(process.argv[2]);

request.get(url, function (error, response, body) {
  if (error) return console.log(error);
  const json = JSON.parse(body)
  console.log(json.title);
});
