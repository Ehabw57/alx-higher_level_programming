#!/usr/bin/node

function bubblesort (arr) {
  let i, j, tmp;

  for (j = (arr.length - 1); j >= 0; j--) {
    for (i = 0; i < j; i++) {
      if (arr[i] > arr[i + 1]) {
        tmp = arr[i];
        arr[i] = arr[i + 1];
        arr[i + 1] = tmp;
      }
    }
  }
  return (arr[(arr.length) - 2]);
}

const args = process.argv.slice(2);
let i;

if (args.length < 2 || isNaN(Number(args[0]))) {
  console.log(0);
} else {
  for (i = 0; i < args.length; i++) {
    args[i] = Number(args[i]);
  }
  console.log(bubblesort(args));
}
