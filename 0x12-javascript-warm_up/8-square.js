#!/usr/bin/node
const size = Number(process.argv[2]);
let i, j, square;
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (i = 0; i < size; i++) {
    for (j = 0, square = ''; j < size; j++) {
      square += 'X';
    }
    console.log(square);
  }
}
