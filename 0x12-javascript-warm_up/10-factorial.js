#!/usr/bin/node

import { argv } from 'node:process'

let a, n;

a = process.argv[1];
n = parseInt(a);i

function facto(n) {
	if ( n === 0 || ( n === 1 ) ) { 
		console.log(1); 
	} else { 
		console.log(n * facto(n - 1)); 
	}
}

if ( a !== null && n ) { 
	facto(n); 
}
