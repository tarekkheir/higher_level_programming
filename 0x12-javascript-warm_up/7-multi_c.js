#!/usr/bin/node
const n = process.argv.length;

if (n === 3 && isNaN(parseInt(process.argv[2], 10))) {
  for (let i = 0; i < process.argv[2]; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurences');
}
