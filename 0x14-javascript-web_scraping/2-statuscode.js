#!/usr/bin/node
const fetch = require('node-fetch');
const URL = process.argv[2];
async function main () {
  const request = new Request(URL);
  const response = await fetch(request);
  console.log(response.status);
}
main();
