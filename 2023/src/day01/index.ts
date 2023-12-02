import run from 'aocrunner';

const parseInput = (rawInput: string) => rawInput;

const part1 = (rawInput: string) => {
  const input = parseInput(rawInput);

  const lines = input.split('\n');
  const numDigit = /\d/g;
  const values = lines
    .map((line) => {
      const digits = Array.of(...line.matchAll(numDigit));
      const first = digits[0] ?? '';
      const last = digits[digits.length - 1] ?? first;
      return Number.parseInt(`${first}${last}`);
    })
    .filter(Number.isInteger);

  const sum = values.reduce((acc, val) => (acc += val), 0);

  return sum;
};

const part2 = (rawInput: string) => {
  const input = parseInput(rawInput);

  return;
};

run({
  part1: {
    tests: [
      {
        input: `
        1abc2
        pqr3stu8vwx
        a1b2c3d4e5f
        treb7uchet
        `,
        expected: 142,
      },
    ],
    solution: part1,
  },
  part2: {
    tests: [
      // {
      //   input: ``,
      //   expected: "",
      // },
    ],
    solution: part2,
  },
  trimTestInputs: true,
  onlyTests: false,
});
