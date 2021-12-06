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
	fmt.Println("Day 6 - Pt. 1:", Part1(in))
	fmt.Println("Day 6 - Pt. 2:", Part2(in))
}

func Part1(input []string) int {
	population := parse.IntSlice(input)
	return binnedSim(population, 80)
}

func Part2(input []string) int {
	population := parse.IntSlice(input)
	return binnedSim(population, 256)
}

func binnedSim(population []int, days int) int {
	bins := [9]int{}
	for _, val := range population {
		bins[val]++
	}
	for day := 0; day < days; day++ {
		var spawning int
		for daysLeft, count := range bins {
			if daysLeft == 0 {
				spawning = count
			} else {
				bins[daysLeft-1] = count
			}
			if daysLeft == 8 {
				bins[6] += spawning
				bins[8] = spawning
			}
		}
	}
	return integers.Sum(bins[:]...)
}
