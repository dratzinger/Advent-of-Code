import run from "aocrunner";

type Matrix<T> = T[][];
const parseInput = (rawInput: string): Matrix<string> =>
  rawInput.split("\n").map((l) => l.trim().split(/\s+/));

const part1 = (rawInput: string) => {
  const input = parseInput(rawInput);
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

  return;
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
    tests: [{ input, expected: "" }],
    solution: part2,
  },
  trimTestInputs: true,
  onlyTests: true,
});
