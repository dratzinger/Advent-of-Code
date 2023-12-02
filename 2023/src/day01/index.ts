import run from 'aocrunner';

const parseInput = (rawInput: string) => rawInput;

const part1 = (rawInput: string) => {
  const input = parseInput(rawInput);
  const lines = input.split('\n');
  return crunch(lines, /(\d)/g);
};

const part2 = (rawInput: string) => {
  const input = parseInput(rawInput);
  const lines = input.split('\n');
  return crunch(
    lines,
    /(?=(\d|one|two|three|four|five|six|seven|eight|nine))/g,
  );
};

const crunch = (lines: string[], pattern: RegExp) =>
  lines
    .map((line) => Array.from(line.matchAll(pattern), (match) => match[1]))
    .map((digits) => {
      console.log(digits);
      const first = String(digits[0] ?? '');
      const last = String(digits[digits.length - 1] ?? first);
      const d1 = lookup[first] ?? first;
      const d2 = lookup[last] ?? last;
      const valStr = `${d1}${d2}`;
      const val = Number.parseInt(valStr);
      return val;
    })
    .filter(Number.isInteger)
    .reduce((acc, val) => (acc += val), 0);

const lookup: { [id: string]: string } = {
  one: '1',
  two: '2',
  three: '3',
  four: '4',
  five: '5',
  six: '6',
  seven: '7',
  eight: '8',
  nine: '9',
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
      {
        input: `
        two1nine
        eightwothree
        abcone2threexyz
        xtwone3four
        4nineeightseven2
        zoneight234
        7pqrstsixteen
        `,
        expected: 281,
      },
    ],
    solution: part2,
  },
  trimTestInputs: true,
  onlyTests: false,
});
