#!/usr/bin/node

exports.converter = function (base) {
  return (n) => { return n.toString(base); };
};
