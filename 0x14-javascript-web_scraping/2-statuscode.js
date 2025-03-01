#!/usr/bin/node
const URL = process.argv[2];
async function main () {
  const response = await fetch(URL);
  console.log(response.status);
}
main();
