package main

import (
	"fmt"
	"log"

	parse "github.com/dratzinger/Advent-of-Code/2021/util"
)

func main() {
	in := parse.StrLines("input.txt")
	fmt.Println("Day 2 - Pt. 1:", Part1(in))
	fmt.Println("Day 2 - Pt. 2:", Part2(in))
}

func Part1(input []string) int {
	xPos, yPos := 0, 0

	var direction string
	var value int

	for _, line := range input {
		_, err := fmt.Sscanf(line, "%s %d", &direction, &value)

		if err != nil {
			log.Fatal(err)
		}

		switch direction {
		case "forward":
			xPos += value
		case "down":
			yPos += value
		case "up":
			yPos -= value
		}
	}
	return xPos * yPos
}

func Part2(input []string) (count int) {
	return
}
