#!/usr/bin/node

const firstArg = process.argv[2];

if (typeof firstArg === 'undefined') {
  console.log('No argument');
} else {
  console.log(firstArg);
}
