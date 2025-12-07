import run from "aocrunner";

type Range = [start: number, end: number];
const parseInput = (rawInput: string) => {
  const data = rawInput.split("\n\n").map((s) => s.split("\n"));
  const ranges = data[0].map((r) => r.split("-", 2).map(Number) as Range);
  const ids = data[1].map(Number);
  return { ranges, ids };
};

const part1 = (rawInput: string) => {
  const { ranges, ids } = parseInput(rawInput);
  const fresh = ids.filter((id) =>
    ranges.some(([start, end]) => id >= start && id <= end),
  );
  return fresh.length;
};

const part2 = (rawInput: string) => {
  const input = parseInput(rawInput);

  return;
};

const input = `
3-5
10-14
16-20
12-18

1
5
8
11
17
32
`;

run({
  part1: {
    tests: [{ input, expected: 3 }],
    solution: part1,
  },
  part2: {
    tests: [{ input, expected: "" }],
    solution: part2,
  },
  trimTestInputs: true,
  onlyTests: false,
});
