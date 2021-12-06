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
	days := 80
	return len(simulate(population, days, 6))
}

func Part2(input []string) int {
	population := parse.IntSlice(input)
	return binnedSim(population, 256)
}

func simulate(population []int, steps, cycleTime int) []int {
	for i := 0; i < steps; i++ {
		population = simpleSim(population, cycleTime)
	}
	return population
}

func simpleSim(population []int, cycleTime int) (result []int) {
	for _, val := range population {
		if val == 0 {
			result = append(result, cycleTime, cycleTime+2)
		} else {
			result = append(result, val-1)
		}
	}
	return result
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
