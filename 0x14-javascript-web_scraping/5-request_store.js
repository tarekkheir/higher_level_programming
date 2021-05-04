#!/usr/bin/node
// script that gets the contents of a webpage and stores it in a file.

const request = require('request');
const fs = require('fs');
const url = process.argv[2];

request.get(url, function (error, response, body) {
  if (error) return console.log(error);
  fs.writeFile(process.argv[3], body, 'utf8', function (err, data) {
    if (err) return console.log(err);
  });
});
