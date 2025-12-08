import run from "aocrunner";
import { transposeMatrix } from "../utils/matrix.js";

type Matrix<T> = T[][];
const parseInput = (rawInput: string) => rawInput.split("\n");

const part1 = (rawInput: string) => {
  const input = parseInput(rawInput).map((l) => l.trim().split(/\s+/));
  const results = [] as number[];
  for (let col = 0; col < input[0].length; col++) {
    const op = input.at(-1)?.at(col);
    let total = op === "*" ? 1 : 0;
    for (let line = input.length - 2; line >= 0; line--) {
      const element = Number(input[line][col]);
      if (op === "*") total *= element;
      else total += element;
    }
    results.push(total);
  }
  return results.reduce((sum, t) => sum + t);
};

const part2 = (rawInput: string) => {
  const input = parseInput(rawInput);
  const transposed = transposeMatrix(input) as Matrix<string>;
  const stack = [] as number[];
  let op: string;
  let total = 0;
  [...transposed, null].forEach((l) => {
    if (l?.at(-1) === "*" || l?.at(-1) === "+") op = l.pop();

    const line = l?.join("")?.trim();
    if (!line) {
      let result = op === "*" ? 1 : 0;
      while (stack.length > 0) {
        let val = stack.pop();
        if (op === "*") result *= val;
        else result += val;
      }
      total += result;
    } else {
      stack.push(Number(line));
    }
  });
  return total;
};

const input = `
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
`;

run({
  part1: {
    tests: [{ input, expected: 4277556 }],
    solution: part1,
  },
  part2: {
    tests: [{ input, expected: 3263827 }],
    solution: part2,
  },
  trimTestInputs: true,
  onlyTests: false,
});
