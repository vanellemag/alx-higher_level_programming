#!/usr/bin/node

import { } from 'node:process';

if (process.argv[2]) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
