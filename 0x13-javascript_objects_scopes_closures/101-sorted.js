#!/usr/bin/node

const { dict } = require('./101-data');
const newDict = {};

for (const userId in dict) {
  const idOccurrences = dict[userId];

  if (!newDict[idOccurrences]) {
    newDict[idOccurrences] = [];
  }
  newDict[idOccurrences].push(userId);
}

console.log(newDict);
