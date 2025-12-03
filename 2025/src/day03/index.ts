import run from "aocrunner";

const parseInput = (rawInput: string) =>
  rawInput.split("\n").map((s) => Array.from(s));

const part1 = (rawInput: string) => {
  const joltages = parseInput(rawInput);
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

const part2 = (rawInput: string) => {
  return;
};

run({
  part1: {
    tests: [
      {
        input: `
        987654321111111
        811111111111119
        234234234234278
        818181911112111
        `,
        expected: 357,
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
