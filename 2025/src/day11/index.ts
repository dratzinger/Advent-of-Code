import run from "aocrunner";

const parseInput = (rawInput: string) => {
  const input = rawInput.split("\n").map((line) => line.split(": "));
  return new Map(input.map((pair) => [pair[0], pair[1].split(" ")]));
};

const countPaths = (
  devices: Map<string, string[]>,
  source: string,
  via?: string[],
  target = "out",
) => {
  const trace = (device: string, checkpoints: Map<string, boolean>): number => {
    if (checkpoints.has(device)) {
      checkpoints.set(device, true);
    }
    if (device === target) {
      const checked = Array.from(checkpoints.values());
      const valid = checked.every(Boolean) ? 1 : 0;
      console.log({ device, checkpoints, valid });
      return valid;
    }

    const connections = devices.get(device) ?? [];
    return connections.reduce(
      (count, connection) => (count += trace(connection, new Map(checkpoints))),
      0,
    );
  };

  via ??= [];
  const visited = new Map(via.map((node) => [node, false]));
  return trace(source, visited);
};

const part1 = (rawInput: string) => {
  const devices = parseInput(rawInput);
  return countPaths(devices, "you");
};

const part2 = (rawInput: string) => {
  const devices = parseInput(rawInput);
  return countPaths(devices, "svr", ["dac", "fft"]);
};

const input1 = `
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

const input2 = `
svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out
`;

run({
  part1: {
    tests: [{ input: input1, expected: 5 }],
    solution: part1,
  },
  part2: {
    tests: [{ input: input2, expected: 2 }],
    solution: part2,
  },
  trimTestInputs: true,
  onlyTests: false,
});
