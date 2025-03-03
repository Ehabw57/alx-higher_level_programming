#!/usr/bin/node
const request = require('request');
const URL = process.argv[2] || process.exit(1);
request(URL, (err, response, body) => {
  if (err) return console.log(err);
  const tasks = JSON.parse(body);
  const completedCount = {};

  for (const task of tasks) {
    if (task.completed) {
      if (completedCount[task.userId]) completedCount[task.userId]++;
      else completedCount[task.userId] = 1;
    }
  }
  console.log(completedCount);
});
