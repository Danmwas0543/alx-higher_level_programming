#!/usr/bin/node
exports.esrever = function (list) {
  let len = list.length - 1;
  let o = 0;
  while ((len - o) > 0) {
    const aux = list[len];
    list[len] = list[o];
    list[o] = aux;
    o++;
    len--;
  }
  return list;
};
