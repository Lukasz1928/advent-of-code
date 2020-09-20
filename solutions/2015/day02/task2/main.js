const fs = require('fs');


function readInput() {
    const input = fs.readFileSync("input")
                    .toString()
                    .split("\n")
                    .map(line => line.split("x").map(x => parseInt(x)));
    return input;   
}

function calculateLength(d) {
    return d.map(p => 2 * (p.reduce((a, b) => a + b, 0) - Math.max(...p)) + p.reduce((a, b) => a * b, 1))
            .reduce((a, b) => a + b, 0);
}

const data = readInput();
const length = calculateLength(data);
console.log(length);