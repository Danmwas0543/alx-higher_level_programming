#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let o = 0; o < this.height; o++) {
      let z = '';
      for (let k = 0; k < this.width; k++) {
        z += c;
      }
      console.log(z);
    }
  }
}

module.exports = Square;
