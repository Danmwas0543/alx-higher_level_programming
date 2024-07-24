#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let nOccurrences = 0;
  for (let o = 0; o < list.length; o++) {
    if (searchElement === list[o]) {
      nOccurrences++;
    }
  }
  return nOccurrences;
};
