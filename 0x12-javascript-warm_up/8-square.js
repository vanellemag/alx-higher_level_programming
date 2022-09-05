#!/usr/bin/node

import { argv } from 'node:process'

let n = process.argv[1];
let m, i;

m = 'X';
if ( n !== null ) { 
	if ( parseInt(n) ) { 
		i = parseInt(n);
		n = i;
		while ( n > 0 ) { 
			while ( i > 0 ) { 
				console.log(m);
				i--; 
			}
			n--; 
		} 
	} else { 
		console.log('Missing number of occurrences'); 
	} 
}
