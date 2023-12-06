import run from 'aocrunner';

const parseInput = (rawInput: string) => rawInput;

const part1 = (rawInput: string) => {
  const input = parseInput(rawInput);
  const [times, records] = input.split('\n').map((line) =>
    line
      .split(/\ +/)
      .map((n) => Number.parseInt(n))
      .filter((i) => !Number.isNaN(i)),
  );
  const possibilities = (time: number, i: number): number =>
    time - (beatRecord(time, records[i]) * 2 - 1);

  return times.map(possibilities).reduce((sum, c) => sum * c);
};

const raceDistance = (availableTime: number, holdTime: number) =>
  holdTime * (availableTime - holdTime);

// Minimum hold time to beat the record
const beatRecord = (available: number, record: number) => {
  for (let t = 1; t < available; t++)
    if (raceDistance(available, t) > record) return t;
  return 0;
};

const part2 = (rawInput: string) => {
  const input = parseInput(rawInput);

  return;
};

const testInput = `
Time:      7  15   30
Distance:  9  40  200
`;
run({
  part1: {
    tests: [
      {
        input: testInput,
        expected: 288,
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
