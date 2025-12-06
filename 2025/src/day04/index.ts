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

const part1 = (rawInput: string) => {
  const input = parseInput(rawInput);
  const rows = input.length;
  const cols = input[0].length;
  const rollcount: Matrix<number> = Array(rows)
    .fill(null)
    .map((_) => Array(cols).fill(null));

  const roll = "@";
  const threshold = 4;
  for (let y = 0; y < rows; y++) {
    for (let x = 0; x < cols; x++) {
      rollcount[y][x] =
        input[y][x] !== roll
          ? threshold
          : getNeighbors(input, y, x).filter((n) => n === roll).length;
    }
  }

  const accessible = rollcount
    .flatMap((l) => l.map((c) => c < threshold))
    .filter(Boolean);
  return accessible.length;
};

const part2 = (rawInput: string) => {
  const input = parseInput(rawInput);

  return;
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
    tests: [{ input, expected: "" }],
    solution: part2,
  },
  trimTestInputs: true,
  onlyTests: false,
});
