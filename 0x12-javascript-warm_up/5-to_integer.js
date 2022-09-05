#!/usr/bin/node

import { argv } from 'node:process'

if ( process.argv[1] !== null ) {
	if ( parseInt(process.argv[1]) ) { 
		console.log('My number: ' +  parseInt(process.argv[1]); 
	} else { 
		console.log('Not a number'); 
	}
} else { 
	console.log('Not a number'); 
}
