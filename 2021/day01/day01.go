package main

import (
	"fmt"

	"github.com/dratzinger/Advent-of-Code/2021/util/parse"
)

func main() {
	in := parse.IntLines("input.txt")
	fmt.Println("Day 1 - Pt. 1:", Part1(in))
	fmt.Println("Day 1 - Pt. 2:", Part2(in))
}

func Part1(input []int) (count int) {
	prev := 0
	for i, val := range input {
		if i > 0 && val > prev {
			count++
		}
		prev = val
	}
	return count
}

func Part2(input []int) int {
	windows := []int{}
	for i := 0; i+2 < len(input); i++ {
		sum := input[i] + input[i+1] + input[i+2]
		windows = append(windows, sum)
	}
	return Part1(windows)
}
