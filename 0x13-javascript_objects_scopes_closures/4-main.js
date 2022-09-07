#!/usr/bin/node
const Rectangle = require('./4-rectangle');
//console.log(Rectangle);
const r1 = new Rectangle(2, 3);
//r1.print();
console.log('Normal: ');
r1.print();

console.log('Double: ');
r1.double();
r1.print();

console.log('Rotate:');
r1.rotate();
r1.print();
/*console.log(r1);
console.log(r1.width);
console.log(r1.height);*/

/*const r2 = new Rectangle(10, 5);
r2.print();
/*console.log(r2);
console.log(r2.width);
console.log(r2.height);*/

/*const r3 = new Rectangle(2, 0);
r3.print();*/
/*console.log(r3);
console.log(r3.width);
console.log(r3.height);*/
