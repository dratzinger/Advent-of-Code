import run from 'aocrunner';

const parseInput = (rawInput: string) => rawInput;

const part1 = (rawInput: string) => {
  const input = parseInput(rawInput);
  const [times, records] = sheet(input);
  return times.map(possibilities(records)).reduce((sum, c) => sum * c);
};

const part2 = (rawInput: string) => {
  const input = parseInput(rawInput);
  const [times, records] = sheet(input, true);
  return times.map(possibilities(records))[0];
};

const sheet = (input: string, badKerning = false) =>
  input.split('\n').map((line) => {
    const nums = line.replace(/.*: */, '').split(/\ +/);
    const k = badKerning ? [nums.reduce((n, i) => n + i)] : nums;
    return k.map((n) => Number.parseInt(n));
  });

const raceDistance = (availableTime: number, holdTime: number) =>
  holdTime * (availableTime - holdTime);

// Minimum hold time to beat the record
const beatRecord = (available: number, record: number) => {
  for (let time = 1; time < available; time++)
    if (raceDistance(available, time) > record) return time;
  return 0;
};

const possibilities =
  (records: number[]) =>
  (time: number, i: number): number =>
    time - (beatRecord(time, records[i]) * 2 - 1);

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
      {
        input: testInput,
        expected: 71503,
      },
    ],
    solution: part2,
  },
  trimTestInputs: true,
  onlyTests: false,
});
