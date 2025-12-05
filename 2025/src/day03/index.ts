import run from "aocrunner";

const parseInput = (rawInput: string) => rawInput.split("\n");

const part1 = (rawInput: string) => {
  const joltages = parseInput(rawInput).map((s) => Array.from(s));
  return joltages
    .map((j) =>
      j.reduce((max, cur, idx, arr) => {
        if (idx + 1 < arr.length && cur > max[0]) return cur + "0";
        if (cur > max[1]) return max[0] + cur;
        return max;
      }, "00"),
    )
    .map(Number)
    .reduce((acc: number, j: number) => acc + j);
};

const cavemanCombinationSum = (j: string) =>
  Array.of(j)
    .flatMap((s) => Array(s.length).fill(s).map(dropCharAtIndex))
    .flatMap((s) => Array(s.length).fill(s).map(dropCharAtIndex))
    .flatMap((s) => Array(s.length).fill(s).map(dropCharAtIndex))
    .map(Number)
    .sort()
    .pop() ?? 0;

const dropCharAtIndex = (str: string, i: number) =>
  str.slice(0, i) + str.slice(i + 1);

const part2 = (rawInput: string) => {
  const joltages = parseInput(rawInput);
  const sums = joltages.map(cavemanCombinationSum);
  return sums.reduce((acc, j) => acc + j);
};

const input = `
        987654321111111
        811111111111119
        234234234234278
        818181911112111
        `;
run({
  part1: {
    tests: [{ input, expected: 357 }],
    solution: part1,
  },
  part2: {
    tests: [{ input, expected: 3121910778619 }],
    solution: part2,
  },
  trimTestInputs: true,
  onlyTests: true,
});
