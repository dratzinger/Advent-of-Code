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
	return bruteMinimize(positions, mean, .25)
}

func Part2(input []string) (count int) {
	return
}

func differences(positions []int, val int) (sum int) {
	for _, v := range positions {
		sum += integers.AbsDiff(v, val)
	}
	return sum
}

// try aligning to a value plus minus a percentage of the data range
// then return the minimum
func bruteMinimize(positions []int, align int, percentage float64) int {
	dataRange := float64(integers.Range(positions...))
	offset := int(dataRange * percentage)
	cost := []int{}
	for val := align - offset; val < align+offset; val++ {
		cost = append(cost, differences(positions, val))
	}
	return integers.Min(cost...)
}
