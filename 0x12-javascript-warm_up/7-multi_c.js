#!/usr/bin/node
/*
 * This script prints "C is fun" x times, where x is provided as a command-line argument.
 * If x is not provided or not a number, it prints "Missing number of occurrences".
 */

const dan = process.argv[2];

if (dan === undefined || isNaN(parseInt(dan))) {
  console.log('Missing number of occurrences');
} else {
  for (let faith = 0; faith < parseInt(dan); faith++) {
    console.log('C is fun');
  }
}
