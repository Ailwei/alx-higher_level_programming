#!/usr/bin/node

const sizeofsquare = parseInt(process.argv[2]);

if (!isNaN(sizeofsquare)) {
  for (let i = 0; i < sizeofsquare; i++) {
    console.log('X'.repeat(sizeofsquare));
  }
} else {
  console.log('Missing size');
}
