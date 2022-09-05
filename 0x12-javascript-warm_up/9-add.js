#!/usr/bin/node

import { argv } from 'node:process'

let a, b;

function add(a, b) {
	if ( a && b ) { 
		console.log(a + b); 
	}
}

if ( process.argv[1] !== null && process.argv[2] !== null ) { 
	a = parseInt(process.argv[1]);
	b = parseInt(process.argv[2]);
	if ( a && b ) { 
		add(a, b);
	} 
}
