#!/usr/bin/node
/*
 * This script prints "My number: <first argument converted to integer>"
 * if the first argument can be converted to an integer.
 */

const dan = process.argv[2];

if (dan === undefined || isNaN(parseInt(dan))) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(dan));
}
