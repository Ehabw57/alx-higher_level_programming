#!/usr/bin/node
const fetch = require('node-fetch');
const URL = process.argv[2];
async function main () {
  const response = await fetch(URL);
  console.log(response.status);
}
main();
