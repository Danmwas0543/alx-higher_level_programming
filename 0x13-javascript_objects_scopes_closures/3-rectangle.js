#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let o = 0; o < this.height; o++) {
      let z = '';
      for (let k = 0; k < this.width; k++) {
        z += 'X';
      }
      console.log(z);
    }
  }
}

module.exports = Rectangle;
