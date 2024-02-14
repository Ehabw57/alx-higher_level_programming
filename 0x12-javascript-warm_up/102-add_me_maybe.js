#!/usr/bin/node
exports.addMeMaybe = function (num, func) {
  let i = Number(num);
  func(++i);
};
