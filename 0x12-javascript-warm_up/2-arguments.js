#!/usr/bin/node

import {argv} from 'node:process';

if ( process.argv[2] !== null ) 
{ 
	console.log('Argument found'); 
} 
else 
{ 
	console.log('No argument'); 
}
