package main

import (
	"fmt"

	"github.com/dratzinger/Advent-of-Code/2021/util/parse"
)

func main() {
	in := parse.StrLines("input.txt")
	in = in[:len(in)-1] // remove empty line
	fmt.Println("Day 3 - Pt. 1:", Part1(in))
	fmt.Println("Day 3 - Pt. 2:", Part2(in))
}

func Part1(input []string) int {
	oxy, epsilon := calcRates(input)
	power := oxy * epsilon
	return power
}

func Part2(input []string) int {
	gamma, scrubber := findRatings(input)
	lifeSupport := gamma * scrubber
	return lifeSupport
}

// find the most common bit in an array by column
func mostCommonBit(input []string, col int) (char byte) {
	charCount := make(map[byte]int)
	for _, line := range input {
		char := line[col]
		charCount[char]++
	}
	if charCount['1'] >= charCount['0'] {
		return '1'
	} else {
		return '0'
	}
}

func leastCommonBit(input []string, col int) (char byte) {
	if mostCommonBit(input, col) == '1' {
		return '0'
	} else {
		return '1'
	}
}

func calcRates(input []string) (gamma, epsilon int) {
	gammaStr := ""
	epsilonStr := ""
	for i := range input[0] {
		gammaStr += string(mostCommonBit(input, i))
		epsilonStr += string(leastCommonBit(input, i))
	}
	gamma = int(parse.Int(gammaStr, 2))
	epsilon = int(parse.Int(epsilonStr, 2))
	return
}

func findRatings(input []string) (oxy, scrubber int) {
	oxyVals, scrubberVals := input, input
	for i := range input[0] {
		if len(oxyVals) > 1 {
			x := leastCommonBit(oxyVals, i)
			oxyVals = removeItems(oxyVals, x, i)
		}

		if len(scrubberVals) > 1 {
			y := mostCommonBit(scrubberVals, i)
			scrubberVals = removeItems(scrubberVals, y, i)
		}
	}
	oxy = int(parse.Int(oxyVals[0], 2))
	scrubber = int(parse.Int(scrubberVals[0], 2))
	return
}

func removeItems(input []string, char byte, atCol int) (output []string) {
	for _, line := range input {
		if line[atCol] == char {
			output = append(output, line)
		}
	}
	return
}
