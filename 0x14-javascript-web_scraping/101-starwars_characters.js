#!/usr/bin/node
const request = require('request');
const URL = 'https://swapi-api.alx-tools.com/api/films/';
const id = process.argv[2];
request(`${URL}${id}`, (err, response, body) => {
  if (err) console.log(err);
  const characters = JSON.parse(body).characters;
  function fetchCharacter (index) {
    if (index >= characters.length) return;
    request(characters[index], (err, response, body) => {
      if (err) console.log(err);
      console.log(JSON.parse(body).name);
      fetchCharacter(index + 1);
    });
  }
  fetchCharacter(0);
});
