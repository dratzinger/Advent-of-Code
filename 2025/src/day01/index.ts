import run from "aocrunner";

const parseInput = (rawInput: string) => rawInput;

const part1 = (rawInput: string) => {
  const input = parseInput(rawInput);
  let dial = 50;
  return input.split("\n").reduce((count, current) => {
    const left = current.slice(0, 1) === "L";
    const amt = Number(current.slice(1));
    dial = (left ? dial - amt : dial + amt) % 100;
    return count + (dial === 0 ? 1 : 0);
  }, 0);
};

const part2 = (rawInput: string) => {
  const input = parseInput(rawInput);
  let dial = 50;
  return input.split("\n").reduce((count, current) => {
    const left = current.slice(0, 1) === "L";
    const amt = Number(current.slice(1));
    for (let i = amt; i > 0; i--) {
      dial = (dial + (left ? -1 : 1)) % 100;
      if (dial === 0) count++;
    }
    return count;
  }, 0);
};

const input = `
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
`;

run({
  part1: {
    tests: [{ input, expected: 3 }],
    solution: part1,
  },
  part2: {
    tests: [{ input, expected: 6 }],
    solution: part2,
  },
  trimTestInputs: true,
  onlyTests: false,
});
