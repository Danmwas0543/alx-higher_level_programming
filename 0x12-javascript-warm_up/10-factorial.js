#!/usr/bin/node
/*
 * This script computes and prints the factorial of a number provided as a command-line argument.
 * If no valid number is provided, it computes the factorial of 1.
 */

let dan = parseInt(process.argv[2]);
if (isNaN(dan)) {
  dan = 1;
}

function faith(n) {
  if (n === 1) {
    return 1;
  }
  return n * faith(n - 1);
}

console.log(faith(dan));
