#!/usr/bin/node
exports.callMeMoby = function (times, func) {
  let i;
  for (i = 0; i < times; i++) {
    func();
  }
};
