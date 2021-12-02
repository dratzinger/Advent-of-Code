package main

import "fmt"

func main() {
	in := parseInput("input.txt")
	fmt.Println("Day 1 - Pt. 1:", Part1(in))
}

func parseInput(file string) []int {
	return []int{}
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
