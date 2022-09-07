#!/usr/bin/node
class  Rectangle {
  width;
  height;
  constructor(w, h){
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
  rotate () {
    let h1;
    
    h1 = this.width;
    this.width = this.height;
    this.height = h1;
  }
  doublee () {
    let a, b;
    
    a = this.width;
    b = this.height;
    this.width = a * 2;
    this.height = b * 2;
  }
}
module.exports = Rectangle;
