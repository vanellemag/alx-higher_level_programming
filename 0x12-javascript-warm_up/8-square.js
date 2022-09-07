#!/usr/bin/node

import { } from 'node:process';

let n = parseInt(process.argv[2]);
let i, j;
let m = '';

if (n) {
  for (j = n; j > 0; j--) {
    for (i = n; i > 0; i--) {
      m = 'X' + m;
    }
    console.log(m);
    m = '';
  }
} else {
  console.log('Missing size');
}
