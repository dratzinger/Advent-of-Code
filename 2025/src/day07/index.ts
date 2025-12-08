import run from "aocrunner";
import { Matrix } from "../utils";

const start = "S";
const empty = ".";
const beam = "|";
const splitter = "^";

const parseInput = (rawInput: string): Matrix<string> =>
  rawInput.split("\n").map((s) => Array.from(s));

const simulateTachyonManifold = (input: Matrix<string>) => {
  let splits = 0;
  let paths = 0;
  input.forEach((current, index, array) => {
    const setBeamIfEmpty = (pos: number) => {
      if (current[pos] === empty) current[pos] = beam;
    };

    const continueOrSplitBeam = (p: string, i: number) => {
      if (p === start || p === beam) {
        setBeamIfEmpty(i);
        if (current[i] === splitter) {
          setBeamIfEmpty(i - 1);
          setBeamIfEmpty(i + 1);
          splits++;
        }
      }
    };

    const previous = array[index - 1];
    previous?.forEach(continueOrSplitBeam);

    if (current.includes(splitter)) {
      const beams = current.reduce(
        (count, p) => (p === beam ? count + 1 : count),
        0,
      );
      paths += beams;
    }
  });
  return { splits, paths };
};

const part1 = (rawInput: string) => {
  const input = parseInput(rawInput);
  const { splits } = simulateTachyonManifold(input);
  return splits;
};

const part2 = (rawInput: string) => {
  const input = parseInput(rawInput);
  const { paths } = simulateTachyonManifold(input);
  return paths;
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
    tests: [{ input, expected: 40 }],
    solution: part2,
  },
  trimTestInputs: true,
  onlyTests: true,
});
