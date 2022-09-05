#!/usr/bin/node

import { argv } from 'node:process'

let n = process.argv[1];
let m = 'C is fun';

if ( n !== null ) { 
	if ( parseInt(n) ) { 
		n = parseInt(n);
		while ( n > 0 ) { 
			console.log(m);
			n--; 
		} 
	} else { 
		console.log('Missing number of occurrences'); 
	}
}
