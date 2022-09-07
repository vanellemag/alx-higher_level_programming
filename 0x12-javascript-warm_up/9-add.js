#!/usr/bin/node

import { } from 'node:process';

let a, b;

function add (a, b) {
  if (a && b) {
    console.log(a + b);
  }
}
if (process.argv[2] && process.argv[3]) {
  a = parseInt(process.argv[2]);
  b = parseInt(process.argv[3]);
  if (a && b) {
    add(a, b);
  }
} else {
  console.log('NaN');
}
