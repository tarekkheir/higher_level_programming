#!/usr/bin/node
const arr = process.argv.slice(2).map(Number);

if (arr.length <= 1) {
  console.log(0);
} else {
  var max = Math.max.apply(null, arr);
  console.log(max)
}
