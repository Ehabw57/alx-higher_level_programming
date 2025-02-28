#!/usr/bin/node
exports.converter = function (base) {
  return function (int) {
    return int.toString(base);
  };
};
