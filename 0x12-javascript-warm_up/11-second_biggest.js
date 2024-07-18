#!/usr/bin/node
/*
 * This script finds the second largest integer in the list of command-line arguments.
 * If there are fewer than 3 arguments, it prints '0'.
 */

const mugo = process.argv;

if (mugo.length <= 3) {
  console.log('0');
} else {
  let dan = parseInt(mugo[2]);
  let faith = parseInt(mugo[3]);
  for (let i = 2; i < mugo.length; i++) {
    const current = parseInt(mugo[i]);
    if (current > faith) {
      dan = faith;
      faith = current;
    } else if (current > dan && current < faith) {
      dan = current;
    }
  }
  console.log(dan);
}
