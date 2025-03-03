#!/usr/bin/node
const request = require('request');
const filmURL = process.argv[2];
request(filmURL, (err, resopnd, body) => {
  if (err) return console.log(err);
  const films = JSON.parse(body).results;
  let count = 0;
  const id = 16;
  const charcterURL = `https://swapi-api.alx-tools.com/api/people/${id}/`;
  for (const film of films) if (film.characters.includes(charcterURL)) count++;
  console.log(count);
});
