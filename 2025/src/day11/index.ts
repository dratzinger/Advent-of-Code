import run from "aocrunner";

const parseInput = (rawInput: string) =>
  rawInput.split("\n").map((line) => line.split(": "));

const part1 = (rawInput: string) => {
  const input = parseInput(rawInput);
  const devices = new Map(input.map((pair) => [pair[0], pair[1].split(" ")]));
  const paths = trace("you", devices);
  return paths;
};

const trace = (device: string, devices: Map<string, string[]>): number => {
  if (device === "out") return 1;
  const connections = devices.get(device) ?? [];
  return connections.reduce(
    (count, connection) => (count += trace(connection, devices)),
    0,
  );
};

const part2 = (rawInput: string) => {
  const input = parseInput(rawInput);

  return;
};

const input = `
aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out
`;

run({
  part1: {
    tests: [{ input, expected: 5 }],
    solution: part1,
  },
  part2: {
    tests: [{ input, expected: "" }],
    solution: part2,
  },
  trimTestInputs: true,
  onlyTests: true,
});
