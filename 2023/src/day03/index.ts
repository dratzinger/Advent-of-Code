import run from 'aocrunner';

const parseInput = (rawInput: string) => rawInput;

const part1 = (rawInput: string) => {
  const input = parseInput(rawInput);
  const lines = input.split('\n');

  return Array.from(generatePartNumbers(lines, symbol))
    .map((n) => n.value)
    .reduce((sum, num) => (sum += num));
};

const part2 = (rawInput: string) => {
  const input = parseInput(rawInput);
  const lines = input.split('\n');

  const partNumbers = Array.from(generatePartNumbers(lines));
  const gears = Array.from(generateGears(lines, partNumbers));
  return gears.map((g) => g.ratio).reduce((sum, ratio) => (sum += ratio));
};

type Part = {
  row: number;
  start: number; // first digit index
  end?: number; // last digit index
  value?: number;
  raw?: string;
};

type PartNumber = Required<Part>;

type Schematic = {
  width: number; // columns
  height: number; // rows
};

type Coordinate = [x: number, y: number];

type Gear = {
  position: Coordinate;
  ratio: number;
};

const symbol = (char?: string) => Boolean(char?.match(/[^\.]/)?.length);

function* neighbourhood(
  { start, end, row }: Part,
  bounds: Schematic,
): Generator<Coordinate> {
  if (!end) end = start;
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

const check = (
  condition: typeof symbol,
  data: string[],
  coords: Coordinate[],
) => {
  for (const coordinate of coords) {
    const char = data[coordinate[1]]?.at(coordinate[0]);
    if (condition(char)) {
      return true;
    }
  }
  return false;
};

function* generatePartNumbers(lines: string[], condition?: typeof symbol) {
  for (const [row, l] of lines.entries()) {
    const regexp = /\d+/g;
    let match: RegExpExecArray | null;

    const bounds: Schematic = { width: l.length, height: lines.length };

    while ((match = regexp.exec(l)) !== null) {
      const raw = String(match[0]);
      const value = Number.parseInt(raw);
      const start = match.index;
      const end = regexp.lastIndex - 1;

      const partNumber = { start, end, row, value, raw };
      const neighbours = Array.from(neighbourhood(partNumber, bounds));

      if (!condition || check(condition, lines, neighbours)) {
        yield partNumber;
      }
    }
  }
}

function* generateGears(lines: string[], parts: PartNumber[]): Generator<Gear> {
  for (const [row, l] of lines.entries()) {
    const regexp = /\*/g;
    let match: RegExpExecArray | null;

    const bounds: Schematic = { width: l.length, height: lines.length };

    while ((match = regexp.exec(l)) !== null) {
      const col = match.index;

      const neighbours = Array.from(neighbourhood({ start: col, row }, bounds));

      const connected = new Set<PartNumber>();
      for (const [x, y] of neighbours) {
        const adjacent = parts
          .filter((p) => y === p.row)
          .filter((p) => x >= p.start && x <= p.end);

        adjacent.forEach((a) => connected.add(a));
      }

      if (connected.size === 2) {
        const [first, second] = Array.from(connected).map((p) => p.value);
        const ratio = first * second;
        yield { position: [col, row], ratio };
      }
    }
  }
}

const testInput = `
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
`;

run({
  part1: {
    tests: [
      {
        input: testInput,
        expected: 4361,
      },
    ],
    solution: part1,
  },
  part2: {
    tests: [
      {
        input: testInput,
        expected: 467835,
      },
    ],
    solution: part2,
  },
  trimTestInputs: true,
  onlyTests: false,
});
