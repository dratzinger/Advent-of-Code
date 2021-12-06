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
	return pilotSub(input, false)
}

func Part2(input []string) (count int) {
	return pilotSub(input, true)
}

func pilotSub(input []string, complicated bool) int {
	var horizontal, depth, aim int

	for _, instruction := range input {
		if instruction != "" {
			direction, value := parseInstruction(instruction)

			switch direction {
			case "forward":
				horizontal += value
				if complicated {
					depth += aim * value
				}
			case "down":
				if complicated {
					aim += value
				} else {
					depth += value
				}
			case "up":
				if complicated {
					aim -= value
				} else {
					depth -= value
				}
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
