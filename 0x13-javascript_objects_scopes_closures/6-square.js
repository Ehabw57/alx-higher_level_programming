#!/usr/bin/node
const Squaree = require('./5-square.js');
class Square extends Squaree {
  charPrint (c = 'X') {
    for (let i = 0; i < this.width; i++) {
      console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;
