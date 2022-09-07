#!/usr/bin/node
import node;
//import { } from 'node:process';
const concat = require('concat-files');

concat([
  'process.argv[2]',
  'process.argv[3]'
], 'process.argv[4]', function (err) {
  if (err) throw err;
  console.log('done');
});
