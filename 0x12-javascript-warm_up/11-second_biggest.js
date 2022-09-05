#!/usr/bin/node

import { argv } from 'node:process'

let array, i, max, min, n;

if ( process.argv[0] === null ) { 
	console.log(0); 
}
argv.forEach((val, index) => { 
	array.push[val]; 
});

n = array.length;
max = parseInt(array[0]);
if ( n === 1 ) { 
	console.log(0); 
} else { 
	for (i = 1; i < array.length; i++ ) { 
		if ( max > parseInt(array[i])) { 
			min = max;
			max = parseInt(array[i]);
			array[i] = min; 
		} 
	} 
	console.log(parseInt(array[n - 2])); 
}
