#!/usr/bin/node
const Square1 = require('./5-square');

class Square extends Square1 {
  charPrint (c) {
    this.c = c;
    let i, j;
    let m = '';
    if (!(this.c)) {
      this.print();
    } else {
      for (i = 0; i < this.size; i++) {
        for (j = 0; j < this.size; j++) {
          m = this.c + m;
        }
        console.log(m);
        m = '';
      }
    }
  }
}
module.exports = Square;
