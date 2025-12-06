import run from "aocrunner";

type Matrix<T> = T[][];
const parseInput = (rawInput: string): Matrix<string> =>
  rawInput.split("\n").map((line) => Array.from(line));

const getNeighbors = (input: Matrix<string>, y: number, x: number) => [
  input[y - 1]?.[x - 1],
  input[y - 1]?.[x],
  input[y - 1]?.[x + 1],
  input[y]?.[x - 1],
  "self",
  input[y]?.[x + 1],
  input[y + 1]?.[x - 1],
  input[y + 1]?.[x],
  input[y + 1]?.[x + 1],
];

const mapAccessible = (input: Matrix<string>, threshold = 4, roll = "@") => {
  const rows = input.length;
  const cols = input[0].length;
  const rollcount: Matrix<number> = Array(rows)
    .fill(null)
    .map((_) => Array(cols).fill(null));

  for (let y = 0; y < rows; y++) {
    for (let x = 0; x < cols; x++) {
      rollcount[y][x] =
        input[y][x] !== roll
          ? threshold
          : getNeighbors(input, y, x).filter((n) => n === roll).length;
    }
  }
  return rollcount.map((l) => l.map((c) => c < threshold));
};

const part1 = (rawInput: string) => {
  const input = parseInput(rawInput);
  const accessible = mapAccessible(input);
  return accessible.flat().filter(Boolean).length;
};

const part2 = (rawInput: string) => {
  let plan = parseInput(rawInput);
  let accessible = mapAccessible(plan);
  let total = 0,
    newlyAccessible = accessible.flat().filter(Boolean).length;
  while (newlyAccessible > 0) {
    total += newlyAccessible;
    plan = plan.map((r, y) => r.map((c, x) => (accessible[y][x] ? "." : c)));
    accessible = mapAccessible(plan);
    newlyAccessible = accessible.flat().filter(Boolean).length;
  }
  return total;
};

const input = `
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
`;

run({
  part1: {
    tests: [{ input, expected: 13 }],
    solution: part1,
  },
  part2: {
    tests: [{ input, expected: 43 }],
    solution: part2,
  },
  trimTestInputs: true,
  onlyTests: false,
});
