#!/usr/bin/node

const dan = {
  faith: 'object',
  mugo: 12
};

console.log(dan);

dan.incr = function () {
  dan.mugo += 1;
};

dan.incr();
console.log(dan);

dan.incr();
console.log(dan);

dan.incr();
console.log(dan);
