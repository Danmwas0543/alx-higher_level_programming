#!/usr/bin/node
/*
 * This script outputs the first argument passed to it.
 * If no argument is provided, it prints "No argument".
 */

const dan = process.argv;

if (dan[2] === undefined) {
  console.log('No argument');
} else {
  console.log(dan[2]);
}
