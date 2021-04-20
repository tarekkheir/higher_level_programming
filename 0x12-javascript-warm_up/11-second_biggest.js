#!/usr/bin/node
const arr = process.argv.slice(2).map(Number);

if (arr.length <= 1) {
  console.log(0);
} else {
  arr.splice(arr.indexOf(Math.max.apply(null, arr)), 1);
  console.log(Math.max.apply(null, arr));
}
