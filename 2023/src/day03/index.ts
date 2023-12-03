import run from 'aocrunner';

const parseInput = (rawInput: string) => rawInput;

const part1 = (rawInput: string) => {
  const input = parseInput(rawInput);
  const lines = input.split('\n');
  const partNumbers = [] as number[];

  lines.forEach((l, row) => {
    const regexp = /\d+/g;
    let match: RegExpExecArray | null;
    while ((match = regexp.exec(l)) !== null) {
      const raw = String(match[0]);
      const value = Number.parseInt(raw);
      const start = match.index;
      const end = regexp.lastIndex - 1;

      const bounds: Schematic = { width: l.length, height: lines.length };
      const neighbors = Array.from(
        neighborhood({ start, end, row, value, raw }, bounds),
      );

      if (checkForSymbols(lines, neighbors)) {
        partNumbers.push(value);
      }
    }
  });

  return partNumbers.reduce((sum, num) => (sum += num), 0);
};

type PartNumber = {
  start: number; // first digit index
  end: number; // last digit index
  row: number;
  value: number;
  raw: string;
};

type Schematic = {
  width: number; // columns
  height: number; // rows
};

type Coordinate = [x: number, y: number];

function* neighborhood(
  partNum: PartNumber,
  bounds: Schematic,
): Generator<Coordinate> {
  const { start, end, row } = partNum;

  const withInBounds = ([x, y]: Coordinate) =>
    x >= 0 && y >= 0 && x < bounds.width && y < bounds.height;

  for (let y = row - 1; y <= row + 1; y++) {
    for (let x = start - 1; x <= end + 1; x++) {
      if (!withInBounds([x, y])) {
        continue;
      }

      if (y === row) {
        if (x < start || x > end) yield [x, y];
      } else {
        yield [x, y];
      }
    }
  }
}

const symbol = (char?: string) => Boolean(char?.match(/[^\.]/)?.length);

const checkForSymbols = (data: string[], coords: Coordinate[]) => {
  for (const coordinate of coords) {
    const char = data[coordinate[1]]?.at(coordinate[0]);
    if (symbol(char)) {
      return true;
    }
  }
  return false;
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
        467..114..
        ...*......
        ..35..633.
        ......#...
        617*......
        .....+.58.
        ..592.....
        ......755.
        ...$.*....
        .664.598..
        `,
        expected: 4361,
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
