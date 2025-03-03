#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const URL = process.argv[2];
const fileName = process.argv[3];

request(URL, (err, response, body) => {
  if (err) return console.log(err);
  fs.writeFile(fileName, body, (err) => {
    if (err) return console.log(err);
  });
});
