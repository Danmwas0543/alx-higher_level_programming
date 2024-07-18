#!/usr/bin/node
/*
 * This script prints a square of size provided as a command-line argument.
 * If size is not provided or not a number, it prints "Missing size".
 */

const faith = process.argv[2];

if (faith === undefined || isNaN(parseInt(faith))) {
  console.log('Missing size');
} else {
  for (let mugo = 0; mugo < parseInt(faith); mugo++) {
    let dan = '';
    for (let i = 0; i < parseInt(faith); i++) {
      dan += 'X';
    }
    console.log(dan);
  }
}
