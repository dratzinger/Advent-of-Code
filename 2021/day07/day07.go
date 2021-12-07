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
	depths := parse.IntSlice(input)
	return alignToMean(depths)
}

func Part2(input []string) (count int) {
	return
}

func alignToMean(depths []int) (sum int) {
	mean := integers.Mean(depths...)
	truncMean := int(mean)
	for _, v := range depths {
		low := integers.AbsDiff(v, truncMean)
		high := integers.AbsDiff(v, truncMean+1)
		minDiff := integers.Min(low, high)
		sum += minDiff
	}
	return sum
}
