import run from "aocrunner";
import { Matrix } from "../utils";

const start = "S";
const empty = ".";
const beam = "|";
const splitter = "^";

const parseInput = (rawInput: string): Matrix<string> =>
  rawInput.split("\n").map((s) => Array.from(s));

const part1 = (rawInput: string) => {
  const input = parseInput(rawInput);
  let count = 0;
  input.forEach((current, index, array) => {
    const updated = [...current];

    const setBeamIfEmpty = (pos: number) => {
      if (current[pos] === empty) current[pos] = beam;
    };

    const continueOrSplitBeam = (p: string, i: number) => {
      if (p === start || p === beam) {
        setBeamIfEmpty(i);
        if (current[i] === splitter) {
          setBeamIfEmpty(i - 1);
          setBeamIfEmpty(i + 1);
          count++;
        }
      }
    };

    const previous = array[index - 1];
    previous?.forEach(continueOrSplitBeam);
  });
  return count;
};

const part2 = (rawInput: string) => {
  const input = parseInput(rawInput);

  return;
};

const input = `
.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
`;

run({
  part1: {
    tests: [{ input, expected: 21 }],
    solution: part1,
  },
  part2: {
    tests: [{ input, expected: "" }],
    solution: part2,
  },
  trimTestInputs: true,
  onlyTests: true,
});
