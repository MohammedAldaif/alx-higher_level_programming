#!/usr/bin/node

function factorial (n) {
  if (isNaN(n) || n < 0) {
    return 1; // Factorial of NaN or negative numbers is 1
  }

  if (n === 0 || n === 1) {
    return 1; // Base case: 0! and 1! are both 1
  } else {
    return n * factorial(n - 1); // Recursive case
  }
}

const input = process.argv[2];
const result = factorial(parseInt(input, 10));

console.log(result);
