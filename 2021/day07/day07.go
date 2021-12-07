package main

import (
	"fmt"
	"strings"

	"github.com/dratzinger/Advent-of-Code/2021/util/integers"
	"github.com/dratzinger/Advent-of-Code/2021/util/parse"
)

func main() {
	str := parse.Read("input.txt")
	data := strings.ReplaceAll(str, "\n", "")
	in := strings.Split(data, ",")
	fmt.Println("Day 7 - Pt. 1:", Part1(in))
	fmt.Println("Day 7 - Pt. 2:", Part2(in))
}

func Part1(input []string) int {
	positions := parse.IntSlice(input)
	mean := int(integers.Mean(positions...))
	return bruteMinimize(positions, mean, .25, differences)
}

func Part2(input []string) (count int) {
	positions := parse.IntSlice(input)
	mean := int(integers.Mean(positions...))
	return bruteMinimize(positions, mean, .25, triangularDifferences)
}

type difference func([]int, int) int

func differences(positions []int, val int) (sum int) {
	for _, v := range positions {
		sum += integers.AbsDiff(v, val)
	}
	return sum
}

// cost increases with each step (n-th triangular number)
func triangularDifferences(positions []int, val int) (sum int) {
	triangular := func(n int) int {
		return n * (n + 1) / 2
	}

	for _, v := range positions {
		diff := integers.AbsDiff(v, val)
		sum += triangular(diff)
	}
	return sum
}

// try aligning the positions to a value plus minus a percentage of the data range
// then return the minimum of those tries
func bruteMinimize(positions []int, align int, percentage float64, fn difference) int {
	dataRange := float64(integers.Range(positions...))
	offset := int(dataRange * percentage)
	cost := []int{}
	for val := align - offset; val < align+offset; val++ {
		cost = append(cost, fn(positions, val))
	}
	return integers.Min(cost...)
}
