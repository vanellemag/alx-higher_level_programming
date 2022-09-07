#!/usr/bin/node
exports.esrever = function (list) {
  const array = [];
  let i;
  const n = list.length;
  for (i = (n - 1); i >= 0; i--) {
    array[n - i - 1] = list[i];
  }
  return (array);
};
