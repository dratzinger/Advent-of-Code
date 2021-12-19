package main

import (
	"fmt"
	"strings"

	"github.com/dratzinger/Advent-of-Code/2021/util/parse"
)

func main() {
	in := parse.Stripped("input.txt")
	fmt.Println("Day 8 - Pt. 1:", Part1(in))
	fmt.Println("Day 8 - Pt. 2:", Part2(in))
}

var unique = map[int]int{
	2: 1,
	3: 7,
	4: 4,
	7: 8,
}

func Part1(input []string) (count int) {
	for _, line := range input {
		_, signal := prepareLine(line)
		for _, segments := range signal {
			_, found := unique[len(segments)]
			if found {
				count++
			}
		}
	}
	return
}

func Part2(input []string) (count int) {
	return
}

func prepareLine(input string) (patterns, value []string) {
	blocks := strings.Split(input, " | ")
	patterns = strings.Split(blocks[0], " ")
	value = strings.Split(blocks[1], " ")
	return
}
