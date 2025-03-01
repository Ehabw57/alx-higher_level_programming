#!/usr/bin/node
const fs = require('fs');
const fileName = process.argv[2];
const writeText = process.argv[3];
fs.writeFile(fileName, writeText, 'utf-8', (error) => {
  if (error) {
    console.log('somthing went worng');
  }
});
