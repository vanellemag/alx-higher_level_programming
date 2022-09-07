#!/usr/bin/node

import { } from 'node:process';

let a, n;

a = process.argv[2];
n = parseInt(a);

function facto(n) {
  if (n === 0 || (n === 1)) {
    return(1);
  } else {
    return(n * facto(n - 1));
  }
}

if (a && n ) {
  console.log(facto(n));
}
if (!a) {
  console.log(1);
}
