#!/usr/bin/node
// script that computes the number of tasks completed by user id

const request = require('request');
let i = 0;
const dict = {};

request.get(process.argv[2], function (error, response, body) {
  if (error) return console.log(error);

  const json = JSON.parse(body);
  while (i < json.length) {
    if (json[i].userId === undefined && json[i].completed === true) {
      dict[json[i].userId] = 0;
    }
    if (json[i].completed === true) {
      dict[json[i].userId] += 1;
    }
    i++;
  }
  console.log(dict);
});
