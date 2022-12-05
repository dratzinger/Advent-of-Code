package main

import (
	"fmt"
	"strings"

	"github.com/dratzinger/Advent-of-Code/2022/util/collections"
	"github.com/dratzinger/Advent-of-Code/2022/util/parse"
)

func main() {
	in := parse.StrLines("input.txt")
	fmt.Println("Day 5 - Pt. 1:", Part1(in))
	fmt.Println("Day 5 - Pt. 2:", Part2(in))
}

func Part1(input []string) (message string) {
	plan, instructions := prepareInput(input)
	for _, instruction := range instructions {
		plan = executeInstruction(plan, instruction)
	}
	message = topCrates(plan)
	return message
}

func topCrates(plan []collections.Stack) (message string) {
	for _, stack := range plan {
		letter := stack.Peek().(byte)
		message += string(letter)
	}
	return message
}

func executeInstruction(plan []collections.Stack, instruction []int) []collections.Stack {
	count := instruction[0]
	from := instruction[1] - 1
	to := instruction[2] - 1
	for ; count > 0; count-- {
		crate := plan[from].Pop()
		plan[to].Push(crate)
	}
	return plan
}

func prepareInput(input []string) (plan []collections.Stack, instructions [][]int) {
	planFloor := -1
	for i, line := range input {
		if planFloor == -1 {
			if strings.Contains(line, " 1   2 ") {
				planFloor = i
				continue
			}
		}
	}

	rawPlan := input[:planFloor]
	rawInstructions := input[planFloor+2:]

	plan = buildPlan(rawPlan)
	instructions = buildInstructions(rawInstructions)
	return
}

func buildInstructions(rawInstructions []string) (instructions [][]int) {
	for _, line := range rawInstructions {
		if line != "" {
			line = strings.Replace(line, "move ", "", 1)
			line = strings.Replace(line, " from ", "-", 1)
			line = strings.Replace(line, " to ", "-", 1)
			raw := strings.Split(line, "-")
			instruction := parse.IntSlice(raw)
			instructions = append(instructions, instruction)
		}
	}
	return instructions
}

func buildPlan(rawPlan []string) []collections.Stack {
	stacks := ((len(rawPlan[0]) - 3) / 4) + 1
	plan := make([]collections.Stack, stacks)
	for i := len(rawPlan) - 1; i >= 0; i-- {
		cursor := 1
		for j := 0; j < stacks; j++ {
			letter := rawPlan[i][cursor]
			if letter != ' ' {
				plan[j].Push(letter)
			}
			cursor += 4
		}
	}
	return plan
}

func Part2(input []string) (message string) {
	return
}
