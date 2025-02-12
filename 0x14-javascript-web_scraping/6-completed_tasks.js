#!/usr/bin/node
// Computes the number of tasks completed by user id.
const request = require('request');
const url = process.argv[2];

request(url, { json: true }, (err, resp, body) => {
  if (err) {
    console.error(err);
    return;
  }

  if (!Array.isArray(body)) {
    console.error('Invalid data format');
    return;
  }

  const completedTasks = {};

  body.forEach((task) => {
    if (task.completed) {
      completedTasks[task.userId] = (completedTasks[task.userId] || 0) + 1;
    }
  });

  console.log(completedTasks);
});
