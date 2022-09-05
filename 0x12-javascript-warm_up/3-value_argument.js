#!/usr/bin/node
import { argv } from 'node:process'

if ( process.argv[2] !== null ) {
	console.log (process.argv[2]); 
} else {
	console.log ('No argument'); 
}
