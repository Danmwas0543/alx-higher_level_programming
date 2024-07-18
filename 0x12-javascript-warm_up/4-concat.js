#!/usr/bin/node
/*
 * This script prints two arguments passed to it in the format: "arg1 is arg2".
 */

const firstArg = process.argv[2];
const secondArg = process.argv[3];

console.log(firstArg + ' is ' + secondArg);
