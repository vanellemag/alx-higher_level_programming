#!/usr/bin/node

import { } from 'node:process';

let n = parseInt(process.argv[2]);
const m = 'C is fun';

if (n) {
  if (parseInt(n)) {
    while (n > 0) {
      console.log(m);
      n--;
    }
  }
} else {
  console.log('Missing number of occurrences');
}
