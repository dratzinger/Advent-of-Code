package main

import (
	"fmt"
	"io"
	"os"
)

func main() {
	in := parseInput("input.txt")
	fmt.Println("Day 1 - Pt. 1:", Part1(in))
	fmt.Println("Day 1 - Pt. 2:", Part2(in))
}

func parseInput(filename string) []int {
	file, err := os.Open(filename)

	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}

	var line int
	var nums []int

	for {
		// give a pattern to scan
		_, err := fmt.Fscanf(file, "%d\n", &line)

		if err != nil {
			if err == io.EOF {
				// stop reading the file
				break
			}
			fmt.Println(err)
			os.Exit(1)
		}
		nums = append(nums, line)
	}
	return nums
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
