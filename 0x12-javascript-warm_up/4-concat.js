#!/usr/bin/node

import { argv } from 'node:process'

if ( process.argv[2] !== null ) { 
	if ( process.argv[3] !== null ) {
	console.log(process.argv[2] + ' is ' + process.argv[3]); 
	} else {
		console.log(process.argv[2] + ' is undefined'); 
	}
} else {
	console.log('undefined is ' + process.arg[3]); 
}
if (process.argv[2] === null && process.argv[3] === null) {
	console.log('undefined is undefined');
