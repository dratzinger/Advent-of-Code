package main

import (
	"fmt"

	"github.com/dratzinger/Advent-of-Code/2022/util/parse"
)

func main() {
	in := parse.StrLines("input.txt")
	fmt.Println("Day 1 - Pt. 1:", Part1(in))
	// fmt.Println("Day 1 - Pt. 2:", Part2(in))
}

func Part1(input []string) (count int) {
	max := 0
	sum := 0
	for _, line := range input {
		if line == "" {
			if sum > max {
				max = sum
			}
			sum = 0
			continue
		}
		sum += parse.ToInt(line)
	}
	return max
}

func Part2(input []string) int {
	return -1
}
