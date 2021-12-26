package main

import (
	"fmt"

	"github.com/dratzinger/Advent-of-Code/2021/util/parse"
)

func main() {
	in := parse.StrLines("input.txt")
	fmt.Println("Day 11 - Pt. 1:", Part1(in))
	fmt.Println("Day 11 - Pt. 2:", Part2(in))
}

func Part1(input []string) (count int) {
	population := parse.IntMatrix(input)
	return simulate(population, 100)
}

func Part2(input []string) (count int) {
	return
}

func simulate(population [][]int, i int) (flashes int) {

	return flashes
}
