#!/usr/bin/node
const firstInt = process.argv[2];
const secondInt = process.argv[3];

function add (a, b) {
  const c = a + b;
  console.log(c);
}

add(+firstInt, +secondInt);
