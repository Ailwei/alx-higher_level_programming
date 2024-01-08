#!/usr/bin/node

const numofocur = parseInt(process.argv[2]);

if (!isNaN(numofocur)) {
  for (let i = 0; i < numofocur; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurences');
}
