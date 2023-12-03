import run from 'aocrunner';

const parseInput = (rawInput: string) => rawInput;

const part1 = (rawInput: string) => {
  const input = parseInput(rawInput);
  const lines = input.split('\n');
  const bag = { red: 12, green: 13, blue: 14 };
  const games = parseGames(lines);
  console.log(games);
  const valid = validateGames(games, bag);
  console.log(valid);
  return valid.reduce((sum, id) => (sum += id));
};

const part2 = (rawInput: string) => {
  const input = parseInput(rawInput);

  return;
};

type Colour = 'red' | 'blue' | 'green';
type Bag = Record<Colour, number>;
type CubeSet = Partial<Bag>;
type Games = Record<number, CubeSet[]>;

const parseGames = (lines: string[]): Games => {
  const split = lines.map((line) => line.replace('Game ', '').split(': '));
  return split
    .map((record) => {
      const [id, log] = record;
      const sets = log.split('; ').map(mapCubeSet);
      return { [id]: sets };
    })
    .reduce((games, record) => ({ ...games, ...record }));
};

const mapCubeSet = (record: string): CubeSet =>
  record.split(', ').reduce((set, cubes) => {
    const [count, colour] = cubes.split(' ');
    return { ...set, [colour as Colour]: Number.parseInt(count) };
  }, {});

const validateGames = (games: Games, bag: Bag) => {
  let valid = [];
  for (const id in games) {
    if (games[id].every((set) => validSet(set, bag))) {
      const i = Number.parseInt(id);
      valid.push(i);
    }
  }
  return valid;
};

const validSet = (set: CubeSet, bag: Bag) =>
  (set.red ?? 0) <= bag.red &&
  (set.green ?? 0) <= bag.green &&
  (set.blue ?? 0) <= bag.blue;

run({
  part1: {
    tests: [
      {
        input: `
        Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
        Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
        Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
        Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
        Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
        `,
        expected: 8,
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
