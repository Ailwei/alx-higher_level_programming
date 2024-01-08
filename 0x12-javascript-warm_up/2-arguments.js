#!/usr/bin/node

const number_args = process.argv.length;

if (number_args > 2)
{
	console.log('Arguments found');
}
else if (number_args === 1)
{
	console.log('Argument found');
}
else
{
	if (number_args === 0)
	{
		console.log('No argument');
	}

