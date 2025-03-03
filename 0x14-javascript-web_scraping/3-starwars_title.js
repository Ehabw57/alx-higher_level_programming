#!/usr/bin/node
const request = require('request');
const URL = 'https://swapi-api.alx-tools.com/api/films/';
const id = process.argv[2];
request(`${URL}${id}`, (err, response, body) => {
  if (err) {
    console.log(err);
  }
  console.log(JSON.parse(body).title);
});
