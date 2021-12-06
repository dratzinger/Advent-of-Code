package main

import (
	"fmt"
	"log"

	"github.com/dratzinger/Advent-of-Code/2021/util/parse"
)

func main() {
	in := parse.StrLines("input.txt")
	fmt.Println("Day 2 - Pt. 1:", Part1(in))
	fmt.Println("Day 2 - Pt. 2:", Part2(in))
}

func Part1(input []string) int {
	return pilotSub(input)
}

func Part2(input []string) (count int) {
	return
}

func pilotSub(input []string) int {
	var horizontal, depth int

	for _, instruction := range input {
		if instruction != "" {
			direction, value := parseInstruction(instruction)

			switch direction {
			case "forward":
				horizontal += value
			case "down":
				depth += value
			case "up":
				depth -= value
			}
		}
	}
	return horizontal * depth
}

func parseInstruction(instruction string) (direction string, value int) {
	_, err := fmt.Sscanf(instruction, "%s %d", &direction, &value)

	if err != nil {
		log.Fatal(err)
	}
	return
}
