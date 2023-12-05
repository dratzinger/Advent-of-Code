import run from 'aocrunner';
import path from 'path';

const parseInput = (rawInput: string) => rawInput;

type AlmanacMap = {
  source: string;
  destination: string;
  mappings: Map<number, number>;
};

const part1 = (rawInput: string) => {
  const input = parseInput(rawInput);
  const [s, ...blocks] = input.split('\n\n');
  const seeds = s.split(' ')
  const mapMap = new Map<string, AlmanacMap>();
  const maps =blocks.map(b=>b.split('\n')).map(([first, ...rest])=>{
    const [source,destination] = first.split(' ')[0].split('-to-');
    const instructions = rest.map(l=>l.split(' '))
    const mappings = new Map<number, number>()
    instructions.forEach(i => {
      let [destNum, sourceNum, range] = i.map(Number.parseInt)
      for(let c=range; c>0; c--) {
        mappings.set(sourceNum, destNum)
        destNum++
        sourceNum++
      }
    })
    const result = {source, destination, mappings}
    mapMap.set(source, result)
    return 
  })
  console.log({mapMap})

  return;
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
