import run from "aocrunner";

const parseInput = (rawInput: string) => rawInput;

const part1 = (rawInput: string) => {
  const input = parseInput(rawInput);
  return input
    .split(",")
    .map((i) => i.split("-").map(Number))
    .flatMap(([start, end]) => Array.from(generateIDs(start, end)))
    .reduce((acc, id) => {
      const t = String(id);
      const len = t.length;
      const invalid =
        len % 2 === 0 && t.slice(0, len / 2) === t.slice(Math.round(len / 2));
      return invalid ? acc + id : acc;
    }, 0);
};

function* generateIDs(start: number, end: number) {
  while (start <= end) yield start++;
}

const part2 = (rawInput: string) => {
  const input = parseInput(rawInput);

  return;
};

run({
  part1: {
    tests: [
      {
        input: `11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124`,
        expected: 1227775554,
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
