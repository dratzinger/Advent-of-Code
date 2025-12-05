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
  const joltages = parseInput(rawInput);
  const sums = joltages.map((j) =>
    Array.from(j)
      .map((val, idx) => ({ val, idx }))
      .sort((a, b) => a.val.localeCompare(b.val))
      .slice(-12)
      .sort((a, b) => a.idx - b.idx)
      .map((el) => el.val)
      .reduce((sum, char) => sum + char),
  );
  const converted = sums.map(Number);
  const len = sums.map((s) => s.length);
  console.log({ sums, len, converted });
  return converted.reduce((acc: number, j: number) => acc + j);
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
