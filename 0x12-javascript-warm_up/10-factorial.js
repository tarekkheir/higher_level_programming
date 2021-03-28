#!/usr/bin/node
function factorial (n) {
  if (!isNaN(parseInt(process.argv[2], 10)) && n >= 2) {
    return factorial(n - 1) * n;
  } else {
    return 1;
  }
}
console.log(factorial(parseInt(process.argv[2])));
