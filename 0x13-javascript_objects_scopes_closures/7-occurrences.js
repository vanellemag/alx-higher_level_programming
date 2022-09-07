#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let i;
  let compt = 0;
  for (i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      compt = compt + 1;
    }
  }
  return (compt);
};
