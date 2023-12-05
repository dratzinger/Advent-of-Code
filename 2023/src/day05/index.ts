import run from 'aocrunner';

const parseInput = (rawInput: string) => rawInput;

type AlmanacMap = {
  source: string;
  destination: string;
  mappings: Range[];
};

type Range = {
  sourceNum: number;
  destNum: number;
  length: number;
};

const part1 = (rawInput: string) => {
  const input = parseInput(rawInput);
  const [s, ...blocks] = input.split('\n\n');
  const seeds = s
    .split(' ')
    .map((n) => Number.parseInt(n))
    .filter((n) => !Number.isNaN(n));
  const maps = blocks
    .map((b) => b.split('\n'))
    .map(([first, ...rest]) => {
      const [source, destination] = first.split(' ')[0].split('-to-');
      const instructions = rest.map((l) => l.split(' '));
      const mappings = instructions
        .map((i): Range => {
          let [destNum, sourceNum, length] = i.map((n) => Number.parseInt(n));
          return { sourceNum, destNum, length };
        })
        .sort((a, b) => a.sourceNum - b.sourceNum);
      return { source, destination, mappings };
    });

  const locations = seeds.map((s) => trackSeed(s, maps));

  return Math.min(...locations);
};

const trackSeed = (seed: number, maps: AlmanacMap[]): number => {
  // the map path in the input is sequential, so I won't bother with pathing
  let result = seed;
  for (const map of maps) {
    result = findMapping(result, map?.mappings);
  }
  return result;
};

const findMapping = (target: number, ranges?: Range[]) => {
  const range = ranges?.find((r) => {
    return r.sourceNum <= target && r.sourceNum + r.length > target;
  });
  if (range) {
    const diff = target - range.sourceNum;
    return range.destNum + diff;
  }
  return target;
};

const part2 = (rawInput: string) => {
  const input = parseInput(rawInput);

  return;
};

const testInput = `
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
`;

run({
  part1: {
    tests: [
      {
        input: testInput,
        expected: 35,
      },
    ],
    solution: part1,
  },
  part2: {
    tests: [
      {
        input: testInput,
        expected: 46,
      },
    ],
    solution: part2,
  },
  trimTestInputs: true,
  onlyTests: false,
});
