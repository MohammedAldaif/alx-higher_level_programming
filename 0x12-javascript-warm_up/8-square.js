#!/usr/bin/node

const arg = process.argv[2];
if (!isNaN(arg)) {
  const length = parseInt(arg, 10);
  if (length < 0) { process.exit(); }
  const myArray = Array(length).fill('X');
  const arrayAsString = myArray.join('');
  for (let i = 0; i < length; i++) {
    console.log(arrayAsString);
  }
} else {
  console.log('Missing size');
}
