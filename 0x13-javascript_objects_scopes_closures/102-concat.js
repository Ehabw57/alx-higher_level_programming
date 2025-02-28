#!/usr/bin/node
const fs = require('fs');
const argv = process.argv.slice(2);
const content1 = fs.readFileSync(argv[0]);
const content2 = fs.readFileSync(argv[1]);
fs.writeFileSync(argv[2], `${content1}${content2}`);
