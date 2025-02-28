#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  list.forEach((item) => {
    if (searchElement === item) {
      count++;
    }
  });
  return count;
};
