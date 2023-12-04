import run from 'aocrunner';

const parseInput = (rawInput: string) => rawInput;

const part1 = (rawInput: string) => {
  const input = parseInput(rawInput);
  const points = readCards(input).flatMap(([winning, nums]) => {
    const winningSet = new Set(winning);
    const scores = nums
      .map((n) => winningSet.has(n))
      .filter(Boolean)
      .map((_, i): number => (i === 0 ? 1 : 2));
    return scores.length < 1
      ? 0
      : scores.reduce((p, multiplier) => p * multiplier, 1);
  });
  return points.reduce((sum, p) => sum + p);
};

const part2 = (rawInput: string) => {
  const input = parseInput(rawInput);
  const points = readCards(input).flatMap(([winning, nums], id) => {
    const winningSet = new Set(winning);
    const wins = nums
      .map((n) => winningSet.has(n))
      .reduce((sum, won) => (won ? sum + 1 : sum), 0);
    return { id, wins };
  });

  const cards = points.map((i) => 1);
  const stack = [...points];

  let current;
  while ((current = stack.pop())) {
    let id = current.id;
    for (let i = current.wins; i > 0; i--) {
      id++;
      cards[id] += 1;
      stack.push(points[id]);
    }
  }
  return cards.reduce((sum, count) => sum + count);
};

const readCards = (input: string) =>
  input
    .split('\n')
    .filter(Boolean)
    .map((l) => l.split(': ')[1].split(' | '))
    .map((c) => c.map((nums) => nums.trim().split(/\ +/)));

const testInput = `
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
`;

run({
  part1: {
    tests: [
      {
        input: testInput,
        expected: 13,
      },
    ],
    solution: part1,
  },
  part2: {
    tests: [
      {
        input: testInput,
        expected: 30,
      },
    ],
    solution: part2,
  },
  trimTestInputs: true,
  onlyTests: false,
});
