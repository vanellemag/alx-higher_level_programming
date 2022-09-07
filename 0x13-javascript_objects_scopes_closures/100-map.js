#!/usr/bin/node
const array = require('./100-data').list;

let i;
const res = [];
for (i = 0; i < array.length; i++) {
  res[i] = array[i] * i;
}
console.log(array);
console.log(res);
