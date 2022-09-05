#!/usr/bin/node

import { argv } from 'node:process'

if ( process.argv[1] !== null ) { 
	if ( process.argv[2] !== null ) {
	console.log(process.argv[1] + ' is ' + process.argv[2]); 
	} else {
		console.log(process.argv[1] + ' is undefined'); 
	}
} else {
	console.log('undefined is ' + process.arg[2]); 
}
if (process.argv[1] === null && process.argv[2] === null) {
	console.log('undefined is undefined');
