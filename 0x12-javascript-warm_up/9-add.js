#!/usr/bin/node
/*
 * This script computes the addition of 2 integers provided as command-line arguments.
 */

const mugo = process.argv[2];
const faith = process.argv[3];

function add(dan, a) {
  return dan + a;
}

const x = parseInt(mugo);
const y = parseInt(faith);

console.log(add(x, y));
