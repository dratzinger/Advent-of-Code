package main

import (
	"fmt"

	"github.com/dratzinger/Advent-of-Code/2021/util/parse"
)

func main() {
	in := parse.StrLines("input.txt")
	in = in[:len(in)-1]
	fmt.Println("Day 3 - Pt. 1:", Part1(in))
	fmt.Println("Day 3 - Pt. 2:", Part2(in))
}

func Part1(input []string) (count int) {
	gamma, epsilon := calcRates(input)
	power := gamma * epsilon
	return power
}

func Part2(input []string) (count int) {
	return count
}

// find the most common letter in an array by column
func mostCommonInColumn(input []string, col int) (char byte) {
	charCount := make(map[byte]int)
	for _, line := range input {
		charCount[line[col]]++
	}
	max := 0
	for key, val := range charCount {
		if val > max {
			char = key
			max = val
		}
	}
	return
}

func calcRates(input []string) (gamma, epsilon int) {
	gammaStr := ""
	epsilonStr := ""
	for i := 0; i < len(input[0]); i++ {
		bit := string(mostCommonInColumn(input, i))
		if bit == "1" {
			gammaStr += "1"
			epsilonStr += "0"
		} else {
			gammaStr += "0"
			epsilonStr += "1"
		}
	}
	gamma = int(parse.Int(gammaStr, 2))
	epsilon = int(parse.Int(epsilonStr, 2))
	return
}
