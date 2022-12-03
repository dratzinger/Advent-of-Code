package main

import (
	"fmt"
	"strings"

	"github.com/dratzinger/Advent-of-Code/2022/util/integers"
	"github.com/dratzinger/Advent-of-Code/2022/util/parse"
)

func main() {
	in := parse.StrLines("input.txt")
	fmt.Println("Day 3 - Pt. 1:", Part1(in))
	fmt.Println("Day 3 - Pt. 2:", Part2(in))
}

func Part1(input []string) (count int) {
	priorities := makePriorityMap()
	duplicatePriorities := []int{}
	for _, line := range input {
		if len(line) > 1 {
			itemType := findDuplicate(line)
			itemPriority := priorities[itemType]
			duplicatePriorities = append(duplicatePriorities, itemPriority)
		}
	}
	return integers.Sum(duplicatePriorities...)
}

func makePriorityMap() (list map[rune]int) {
	list = make(map[rune]int)
	letters := "abcdefghijklmnopqrstuvwxyz"
	upper := strings.ToUpper(letters)
	letters = letters + upper
	for i, letter := range letters {
		list[letter] = i + 1
	}
	return list
}

func findDuplicate(input string) rune {
	half := len(input) / 2
	for _, letter := range input[:half] {
		contained := strings.Contains(input[half:], string(letter))
		if contained {
			return letter
		}
	}
	return 0
}

func Part2(input []string) (count int) {
	priorities := makePriorityMap()
	badgePriorities := []int{}
	for i := range input {
		if i%3 == 2 {
			rucksacks := input[i-2 : i+1]
			itemType := findBadge(rucksacks)
			badgePriority := priorities[itemType]
			badgePriorities = append(badgePriorities, badgePriority)
		}
	}
	return integers.Sum(badgePriorities...)
}

func findBadge(input []string) rune {
	for _, letter := range input[0] {
		contained := strings.Contains(input[1], string(letter))
		contained = contained && strings.Contains(input[2], string(letter))
		if contained {
			return letter
		}
	}
	return 0
}
