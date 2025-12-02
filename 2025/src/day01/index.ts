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
  return;
};

run({
  part1: {
    tests: [
      {
        input: `
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
        `,
        expected: "3",
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
