#!/usr/bin/node
const request = require('request');
const filmURL = process.argv[2];
request(filmURL + '/1', (err, resopnd, body) => {
  if (err) {
    console.log(err);
  }
  const charURL = JSON.parse(body).characters[14];
  request(charURL, (err, respond, body) => {
    if (err) {
      console.log(err);
    }
    console.log(JSON.parse(body).films.length);
  });
});
