#!/usr/bin/node
/*
 * This script outputs a specific message based on the number
 * of input arguments provided.
 */

const inputArgs = process.argv;

if (inputArgs.length <= 2) {
  console.log('No argument');
} else if (inputArgs.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
