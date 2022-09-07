#!/usr/bin/node

import { argv } from 'node:process';

let i, n;
const array = [];

if (!process.argv[2]) {
  console.log(0);
} else {
  for (i = 2; i < argv.length; i++) {
    array[i - 2] = parseInt(process.argv[i]);
  }
  n = array.length;
  if (n === 1) {
    console.log(0);
  } else {
    console.log(parseInt(array[n - 2]));
  }
}
