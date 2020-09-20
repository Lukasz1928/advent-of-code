const fs = require('fs');


function readInput() {
    const input = fs.readFileSync("input")
                    .toString()
                    .split("\n")
                    .map(line => line.split("x").map(x => parseInt(x)));
    return input;   
}

function calculateArea(d) {
    return d.map(p => [p[0] * p[1], p[0] * p[2], p[1] * p[2]])
            .map(p => 2 * p.reduce((a, b) => a + b, 0) + Math.min(...p))
            .reduce((a, b) => a + b, 0);
}

const data = readInput();
const area = calculateArea(data);
console.log(area);