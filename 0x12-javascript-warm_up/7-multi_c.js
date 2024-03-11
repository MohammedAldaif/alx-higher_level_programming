#!/usr/bin/node

const input = process.argv[2];
const number = parseInt(input, 10);

if (!isNaN(number)) {
  let i = 0;
  while (i < number) {
    console.log('C is fun');
    i++;
  }
} else {
  console.log('Missing number of occurrences');
}
