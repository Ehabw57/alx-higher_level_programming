#!/usr/bin/node
let number = Number(process.argv[2]);
if (isNaN(number)) {
  console.log('Missing number of occurrences');
} else {
  for (; number > 0; number--) {
    console.log('C is fun');
  }
}
