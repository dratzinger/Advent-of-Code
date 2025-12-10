import run from "aocrunner";

const parseInput = (rawInput: string) =>
  rawInput.split("\n").map((s) => s.split(",").map(Number));

const part1 = (rawInput: string) => {
  const input = parseInput(rawInput);
  let maxArea = 0;
  let current = input.pop();
  while (current) {
    maxArea = input.reduce((max, next) => {
      const [x0, y0] = current;
      const [x1, y1] = next;
      const length = Math.max(x0, x1) - Math.min(x0, x1) + 1;
      const height = Math.max(y0, y1) - Math.min(y0, y1) + 1;
      const area = length * height;
      return Math.max(max, area);
    }, maxArea);
    current = input.pop();
  }
  return maxArea;
};

const part2 = (rawInput: string) => {
  const input = parseInput(rawInput);

  return;
};

const input = `
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
`;

run({
  part1: {
    tests: [{ input, expected: 50 }],
    solution: part1,
  },
  part2: {
    tests: [{ input, expected: "" }],
    solution: part2,
  },
  trimTestInputs: true,
  onlyTests: false,
});
