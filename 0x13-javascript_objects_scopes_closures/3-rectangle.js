#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i, j;
    let m = '';

    for (i = 0; i < this.height; i++) {
      for (j = 0; j < this.width; j++) {
        m = 'X' + m;
      }
      console.log(m);
      m = '';
    }
  }
}
module.exports = Rectangle;
