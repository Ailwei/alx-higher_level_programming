#!/usr/bin/node

const mynumb = parseInt(process.argv[2]);

if (!isNaN(mynumb))
{
	console.log('My number: ${mynumb}');
}
else
{
	console.log('Not a number');
}
