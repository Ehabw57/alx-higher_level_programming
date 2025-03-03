#!/usr/bin/node
const request = require('request');
const URL = process.argv[2] || process.exit(1);
request(URL, (err, response, body) => {
  if (err) return console.log(err);
  const tasks = JSON.parse(body);
  const completed_count = {};

  for (const task of tasks) {
    if (task.completed) {
      if (completed_count[task.userId]) completed_count[task.userId]++;
      else completed_count[task.userId] = 1;
    }
  }
  console.log(completed_count);
});
