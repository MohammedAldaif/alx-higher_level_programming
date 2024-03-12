#!/usr/bin/node
let a = parseInt(process.argv[2],10);
let b = parseInt(process.argv[3],10);
function add(a,b){
	return a + b;
}
console.log(add(a,b));
